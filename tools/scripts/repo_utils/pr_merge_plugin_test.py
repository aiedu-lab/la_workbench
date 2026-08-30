# ===================================================================
# tools/scripts/repo_utils/pr_merge_plugin_test.py
# ===================================================================
"""Unit tests for pr_merge_plugin.py's hook/skill control flow, with
subprocess.run and fetch_pr_status fully mocked -- no real git or gh
call ever happens, and no real polling delay (time.sleep is mocked
too). Mirrors pr_submit_plugin_test.py's approach: every branch
(success and halt-on-failure) of every hook/skill is exercised
deterministically here.

Run via:
  python3 tools/scripts/repo_utils/pr_merge_plugin_test.py
"""

import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

import pr_merge_plugin as plugin


def _proc(returncode=0, stdout="", stderr=""):
  return MagicMock(returncode=returncode, stdout=stdout, stderr=stderr)


class HookWaitForChecksTest(unittest.TestCase):
  @patch.object(plugin, "fetch_pr_status")
  def test_not_open_halts(self, mock_fetch):
    mock_fetch.return_value = {
      "state": "CLOSED",
      "pending_checks": [],
      "failed_checks": [],
    }
    with self.assertRaises(SystemExit):
      plugin.hook_wait_for_checks(Path("/repo"), 42, 0.01, 10)

  @patch.object(plugin, "fetch_pr_status")
  def test_failed_check_halts(self, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "pending_checks": [],
      "failed_checks": ["test"],
    }
    with self.assertRaises(SystemExit):
      plugin.hook_wait_for_checks(Path("/repo"), 42, 0.01, 10)

  @patch("time.sleep")
  @patch.object(plugin, "fetch_pr_status")
  def test_polls_until_no_pending(self, mock_fetch, mock_sleep):
    mock_fetch.side_effect = [
      {"state": "OPEN", "pending_checks": ["a"], "failed_checks": []},
      {"state": "OPEN", "pending_checks": [], "failed_checks": []},
    ]
    plugin.hook_wait_for_checks(Path("/repo"), 42, 0.01, 10)  # no raise
    mock_sleep.assert_called_once()

  @patch("time.sleep")
  @patch("time.monotonic")
  @patch.object(plugin, "fetch_pr_status")
  def test_timeout_halts(self, mock_fetch, mock_monotonic, _mock_sleep):
    mock_fetch.return_value = {
      "state": "OPEN",
      "pending_checks": ["a"],
      "failed_checks": [],
    }
    mock_monotonic.side_effect = [0, 100]
    with self.assertRaises(SystemExit):
      plugin.hook_wait_for_checks(Path("/repo"), 42, 0.01, 10)


class SkillMergePrTest(unittest.TestCase):
  @patch.object(plugin.subprocess, "run")
  def test_success(self, mock_run):
    mock_run.return_value = _proc(returncode=0)
    plugin.skill_merge_pr(Path("/repo"), 42, "merge", False)  # no raise
    called_cmd = mock_run.call_args.args[0]
    self.assertIn("merge_pr.py", called_cmd[1])
    self.assertIn("42", called_cmd)

  @patch.object(plugin.subprocess, "run")
  def test_delete_branch_appended(self, mock_run):
    mock_run.return_value = _proc(returncode=0)
    plugin.skill_merge_pr(Path("/repo"), 42, "squash", True)
    called_cmd = mock_run.call_args.args[0]
    self.assertIn("--delete-branch", called_cmd)

  @patch.object(plugin.subprocess, "run")
  def test_failure_halts(self, mock_run):
    mock_run.return_value = _proc(returncode=1)
    with self.assertRaises(SystemExit):
      plugin.skill_merge_pr(Path("/repo"), 42, "merge", False)


class HookConfirmMergedTest(unittest.TestCase):
  @patch.object(plugin.subprocess, "run")
  def test_success(self, mock_run):
    mock_run.return_value = _proc(returncode=0, stdout="MERGED\n")
    plugin.hook_confirm_merged(Path("/repo"), 42)  # must not raise

  @patch.object(plugin.subprocess, "run")
  def test_not_merged_halts(self, mock_run):
    mock_run.return_value = _proc(returncode=0, stdout="OPEN\n")
    with self.assertRaises(SystemExit):
      plugin.hook_confirm_merged(Path("/repo"), 42)

  @patch.object(plugin.subprocess, "run")
  def test_command_failure_halts(self, mock_run):
    mock_run.return_value = _proc(returncode=1, stdout="")
    with self.assertRaises(SystemExit):
      plugin.hook_confirm_merged(Path("/repo"), 42)


class MainEndToEndTest(unittest.TestCase):
  """Verifies the full 3-step call sequence when every step succeeds,
  and that a mid-chain failure stops before any later step runs."""

  @patch.object(plugin, "find_repo_root", return_value=Path("/repo"))
  @patch.object(plugin, "fetch_pr_status")
  @patch.object(plugin.subprocess, "run")
  @patch("sys.argv", ["pr_merge_plugin.py", "42"])
  def test_full_chain_success_order(self, mock_run, mock_fetch, _mock_root):
    mock_fetch.return_value = {
      "state": "OPEN",
      "pending_checks": [],
      "failed_checks": [],
    }
    mock_run.side_effect = [
      _proc(returncode=0),  # [2] merge_pr.py
      _proc(returncode=0, stdout="MERGED\n"),  # [3] gh pr view
    ]
    plugin.main()  # must not raise
    self.assertEqual(mock_run.call_count, 2)

  @patch.object(plugin, "find_repo_root", return_value=Path("/repo"))
  @patch.object(plugin, "fetch_pr_status")
  @patch.object(plugin.subprocess, "run")
  @patch("sys.argv", ["pr_merge_plugin.py", "42"])
  def test_merge_failure_stops_before_confirm(
    self, mock_run, mock_fetch, _mock_root
  ):
    mock_fetch.return_value = {
      "state": "OPEN",
      "pending_checks": [],
      "failed_checks": [],
    }
    mock_run.side_effect = [_proc(returncode=1)]  # [2] merge_pr fails
    with self.assertRaises(SystemExit):
      plugin.main()
    self.assertEqual(mock_run.call_count, 1)  # never reached confirm


if __name__ == "__main__":
  unittest.main()
