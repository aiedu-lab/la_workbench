# ===================================================================
# tools/scripts/repo_utils/pr_submit_plugin_test.py
# ===================================================================
"""Unit tests for pr_submit_plugin.py's hook/skill control flow, with
`subprocess.run` fully mocked -- no real git, bazel, act, or gh call
ever happens. This is the answer to "how do we validate a script
that must never actually push or open a real PR": every branch
(success and halt-on-failure) of every hook/skill is exercised
deterministically here; the one thing these tests cannot cover is
whether the real `git`/`bazel`/`act`/`gh` commands behave as this
script assumes -- that gap is accepted the same way it already is
for submit_pr.py/approve_pr.py/pr_check.py (verified via --help and
real-but-safe invocations, never a real push or PR).
"""

import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from tools.scripts.repo_utils import pr_submit_plugin as plugin


def _proc(returncode=0, stdout="", stderr=""):
  return MagicMock(returncode=returncode, stdout=stdout, stderr=stderr)


class HookCheckBranchStateTest(unittest.TestCase):
  @patch.object(plugin.subprocess, "run")
  def test_detached_head_halts(self, mock_run):
    mock_run.return_value = _proc(stdout="")  # empty branch name
    with self.assertRaises(SystemExit):
      plugin.hook_check_branch_state(Path("/repo"), "main")

  @patch.object(plugin.subprocess, "run")
  def test_main_branch_halts(self, mock_run):
    mock_run.return_value = _proc(stdout="main")
    with self.assertRaises(SystemExit):
      plugin.hook_check_branch_state(Path("/repo"), "main")

  @patch.object(plugin.subprocess, "run")
  def test_dirty_tree_halts(self, mock_run):
    mock_run.side_effect = [
      _proc(stdout="feat/x"),  # branch --show-current
      _proc(stdout=" M some_file.py\n"),  # status --porcelain
    ]
    with self.assertRaises(SystemExit):
      plugin.hook_check_branch_state(Path("/repo"), "main")

  @patch.object(plugin.subprocess, "run")
  def test_fetch_failure_halts(self, mock_run):
    mock_run.side_effect = [
      _proc(stdout="feat/x"),  # branch --show-current
      _proc(stdout=""),  # status --porcelain: clean
      _proc(returncode=1),  # git fetch
    ]
    with self.assertRaises(SystemExit):
      plugin.hook_check_branch_state(Path("/repo"), "main")

  @patch.object(plugin.subprocess, "run")
  def test_no_upstream_halts(self, mock_run):
    mock_run.side_effect = [
      _proc(stdout="feat/x"),  # branch --show-current
      _proc(stdout=""),  # status --porcelain: clean
      _proc(returncode=0),  # git fetch
      _proc(stdout="deadbeef"),  # rev-parse HEAD
      _proc(returncode=1),  # rev-parse origin/feat/x: no upstream
    ]
    with self.assertRaises(SystemExit):
      plugin.hook_check_branch_state(Path("/repo"), "main")

  @patch.object(plugin.subprocess, "run")
  def test_diverged_from_remote_halts(self, mock_run):
    mock_run.side_effect = [
      _proc(stdout="feat/x"),
      _proc(stdout=""),
      _proc(returncode=0),
      _proc(stdout="deadbeef"),
      _proc(returncode=0, stdout="c0ffee"),  # different sha
    ]
    with self.assertRaises(SystemExit):
      plugin.hook_check_branch_state(Path("/repo"), "main")

  @patch.object(plugin.subprocess, "run")
  def test_clean_and_up_to_date_passes(self, mock_run):
    mock_run.side_effect = [
      _proc(stdout="feat/x"),
      _proc(stdout=""),
      _proc(returncode=0),
      _proc(stdout="deadbeef"),
      _proc(returncode=0, stdout="deadbeef"),  # same sha
    ]
    branch = plugin.hook_check_branch_state(Path("/repo"), "main")
    self.assertEqual(branch, "feat/x")


class SkillBuildAndTestTest(unittest.TestCase):
  @patch.object(plugin.subprocess, "run")
  def test_all_commands_run_in_order_on_success(self, mock_run):
    mock_run.return_value = _proc(returncode=0)
    plugin.skill_build_and_test(Path("/repo"))
    self.assertEqual(mock_run.call_count, 4)
    called_cmds = [call.args[0] for call in mock_run.call_args_list]
    self.assertEqual(
      called_cmds,
      [
        ["bazel", "build", "//..."],
        ["bazel", "test", "//..."],
        ["bazel", "run", "//:container_tests"],
        ["bazel", "run", "//:dockerfile_container_tests"],
      ],
    )

  @patch.object(plugin.subprocess, "run")
  def test_first_failure_halts_before_later_commands(self, mock_run):
    mock_run.side_effect = [_proc(returncode=1)]
    with self.assertRaises(SystemExit):
      plugin.skill_build_and_test(Path("/repo"))
    self.assertEqual(mock_run.call_count, 1)  # never reached test/container

  @patch.object(plugin.subprocess, "run")
  def test_third_command_failure_halts_before_fourth(self, mock_run):
    mock_run.side_effect = [
      _proc(returncode=0),
      _proc(returncode=0),
      _proc(returncode=1),  # container_tests fails
    ]
    with self.assertRaises(SystemExit):
      plugin.skill_build_and_test(Path("/repo"))
    self.assertEqual(mock_run.call_count, 3)  # never reached dockerfile


class SkillPrCheckTest(unittest.TestCase):
  @patch.object(plugin.subprocess, "run")
  def test_success(self, mock_run):
    mock_run.return_value = _proc(returncode=0)
    plugin.skill_pr_check(Path("/repo"))  # must not raise

  @patch.object(plugin.subprocess, "run")
  def test_failure_halts(self, mock_run):
    mock_run.return_value = _proc(returncode=1)
    with self.assertRaises(SystemExit):
      plugin.skill_pr_check(Path("/repo"))


class SkillSubmitPrTest(unittest.TestCase):
  @patch.object(plugin.subprocess, "run")
  def test_parses_pr_number_from_url(self, mock_run):
    mock_run.return_value = _proc(
      returncode=0, stdout="https://github.com/o/r/pull/42\n"
    )
    pr_number = plugin.skill_submit_pr(
      Path("/repo"), "title", "body", "main", False
    )
    self.assertEqual(pr_number, "42")

  @patch.object(plugin.subprocess, "run")
  def test_draft_flag_appended_to_command(self, mock_run):
    mock_run.return_value = _proc(
      returncode=0, stdout="https://github.com/o/r/pull/7\n"
    )
    plugin.skill_submit_pr(Path("/repo"), "t", "b", "main", True)
    called_cmd = mock_run.call_args.args[0]
    self.assertIn("--draft", called_cmd)

  @patch.object(plugin.subprocess, "run")
  def test_nonzero_exit_halts(self, mock_run):
    mock_run.return_value = _proc(returncode=1, stdout="", stderr="boom")
    with self.assertRaises(SystemExit):
      plugin.skill_submit_pr(Path("/repo"), "t", "b", "main", False)

  @patch.object(plugin.subprocess, "run")
  def test_missing_pr_url_halts(self, mock_run):
    mock_run.return_value = _proc(returncode=0, stdout="no url here\n")
    with self.assertRaises(SystemExit):
      plugin.skill_submit_pr(Path("/repo"), "t", "b", "main", False)


class HookConfirmPrExistsTest(unittest.TestCase):
  @patch.object(plugin.subprocess, "run")
  def test_success(self, mock_run):
    mock_run.return_value = _proc(returncode=0, stdout="open\n")
    plugin.hook_confirm_pr_exists(Path("/repo"), "42")  # must not raise

  @patch.object(plugin.subprocess, "run")
  def test_failure_halts(self, mock_run):
    mock_run.return_value = _proc(returncode=1)
    with self.assertRaises(SystemExit):
      plugin.hook_confirm_pr_exists(Path("/repo"), "42")


class MainEndToEndTest(unittest.TestCase):
  """Verifies the full 7-step call sequence when every step succeeds,
  and that a mid-chain failure stops before any later step runs."""

  @patch.object(plugin, "find_repo_root", return_value=Path("/repo"))
  @patch.object(plugin.subprocess, "run")
  def test_full_chain_success_order(self, mock_run, _mock_root):
    mock_run.side_effect = [
      _proc(stdout="feat/x"),  # [1] branch
      _proc(stdout=""),  # [1] status
      _proc(returncode=0),  # [1] fetch
      _proc(stdout="deadbeef"),  # [1] rev-parse HEAD
      _proc(returncode=0, stdout="deadbeef"),  # [1] rev-parse origin
      _proc(returncode=0),  # [2] bazel build
      _proc(returncode=0),  # [2] bazel test
      _proc(returncode=0),  # [2] container_tests
      _proc(returncode=0),  # [2] dockerfile_container_tests
      _proc(returncode=0),  # [4] pr_check
      _proc(  # [6] submit_pr
        returncode=0, stdout="https://github.com/o/r/pull/9\n"
      ),
      _proc(returncode=0, stdout="open\n"),  # [7] gh pr view
    ]
    with (
      patch.object(plugin, "parse_args") as mock_args,
      patch("builtins.print"),
    ):
      mock_args.return_value = MagicMock(
        title="t", body="b", base="main", draft=False
      )
      plugin.main()  # must not raise
    self.assertEqual(mock_run.call_count, 12)

  @patch.object(plugin, "find_repo_root", return_value=Path("/repo"))
  @patch.object(plugin.subprocess, "run")
  def test_build_failure_stops_before_submit(self, mock_run, _mock_root):
    mock_run.side_effect = [
      _proc(stdout="feat/x"),
      _proc(stdout=""),
      _proc(returncode=0),
      _proc(stdout="deadbeef"),
      _proc(returncode=0, stdout="deadbeef"),
      _proc(returncode=1),  # bazel build fails
    ]
    with (
      patch.object(plugin, "parse_args") as mock_args,
      patch("builtins.print"),
    ):
      mock_args.return_value = MagicMock(
        title="t", body="b", base="main", draft=False
      )
      with self.assertRaises(SystemExit):
        plugin.main()
    # Exactly the 5 branch-state calls + the 1 failing build call --
    # never reaches pr_check or submit_pr.
    self.assertEqual(mock_run.call_count, 6)


if __name__ == "__main__":
  unittest.main()
