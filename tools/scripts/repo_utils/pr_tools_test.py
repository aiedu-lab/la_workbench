# ===================================================================
# tools/scripts/repo_utils/pr_tools_test.py
# ===================================================================
"""Unit tests for _pr_utils.py's shared logic and the
check_pr/submit_pr/approve_pr/merge_pr scripts built on it, with
subprocess.run fully mocked -- no real git or gh command ever runs,
so executing this file never actually checks, submits, approves, or
merges a real PR. Mirrors pr_submit_plugin_test.py's approach (fully
mocked, exercises every success/halt branch deterministically); the
gap this can't cover -- whether the real `git`/`gh` commands behave
as these scripts assume -- is accepted the same way it already is
there, verified instead via --help and real-but-safe invocations.

Run via:
  python3 tools/scripts/repo_utils/pr_tools_test.py
"""

import json
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

import approve_pr
import check_pr
import merge_pr
import submit_pr
import _pr_utils


def _proc(returncode=0, stdout="", stderr=""):
  return MagicMock(returncode=returncode, stdout=stdout, stderr=stderr)


def _pr_json(**overrides):
  base = {
    "state": "OPEN",
    "author": {"login": "someone_else"},
    "reviewDecision": "",
    "statusCheckRollup": [],
  }
  base.update(overrides)
  return json.dumps(base)


class CheckOutcomeTest(unittest.TestCase):
  """_check_outcome must classify both the modern CheckRun shape
  (status + conclusion) and the legacy StatusContext shape (state
  only) identically."""

  def test_pending_checkrun(self):
    outcome = _pr_utils._check_outcome({"name": "t", "status": "IN_PROGRESS"})
    self.assertEqual(outcome, ("pending", "t"))

  def test_passed_checkrun(self):
    check = {"name": "t", "status": "COMPLETED", "conclusion": "SUCCESS"}
    self.assertEqual(_pr_utils._check_outcome(check), ("passed", "t"))

  def test_neutral_conclusion_counts_as_passed(self):
    check = {"name": "t", "status": "COMPLETED", "conclusion": "NEUTRAL"}
    self.assertEqual(_pr_utils._check_outcome(check), ("passed", "t"))

  def test_failed_checkrun(self):
    check = {"name": "t", "status": "COMPLETED", "conclusion": "FAILURE"}
    self.assertEqual(_pr_utils._check_outcome(check), ("failed", "t"))

  def test_pending_legacy_status(self):
    outcome = _pr_utils._check_outcome({"name": "t", "state": "PENDING"})
    self.assertEqual(outcome, ("pending", "t"))

  def test_passed_legacy_status(self):
    outcome = _pr_utils._check_outcome({"name": "t", "state": "SUCCESS"})
    self.assertEqual(outcome, ("passed", "t"))

  def test_failed_legacy_status(self):
    outcome = _pr_utils._check_outcome({"name": "t", "state": "ERROR"})
    self.assertEqual(outcome, ("failed", "t"))


class CheckAuthAndPermissionTest(unittest.TestCase):
  @patch.object(_pr_utils.shutil, "which", return_value=None)
  def test_gh_missing_halts(self, _mock_which):
    with self.assertRaises(SystemExit):
      _pr_utils.check_auth_and_permission(Path("/repo"), {"ADMIN"}, "t")

  @patch.object(_pr_utils, "run")
  @patch.object(_pr_utils.shutil, "which", return_value="/usr/bin/gh")
  def test_not_authenticated_halts(self, _mock_which, mock_run):
    mock_run.side_effect = _pr_utils.subprocess.CalledProcessError(
      1, ["gh", "auth", "status"], stderr="not logged in"
    )
    with self.assertRaises(SystemExit):
      _pr_utils.check_auth_and_permission(Path("/repo"), {"ADMIN"}, "t")

  @patch.object(_pr_utils, "run")
  @patch.object(_pr_utils.shutil, "which", return_value="/usr/bin/gh")
  def test_insufficient_permission_halts(self, _mock_which, mock_run):
    mock_run.side_effect = [_proc(), _proc(stdout="WRITE\n")]
    with self.assertRaises(SystemExit):
      _pr_utils.check_auth_and_permission(Path("/repo"), {"ADMIN"}, "t")

  @patch.object(_pr_utils, "run")
  @patch.object(_pr_utils.shutil, "which", return_value="/usr/bin/gh")
  def test_sufficient_permission_returns_it(self, _mock_which, mock_run):
    mock_run.side_effect = [_proc(), _proc(stdout="ADMIN\n")]
    permission = _pr_utils.check_auth_and_permission(
      Path("/repo"), {"ADMIN"}, "t"
    )
    self.assertEqual(permission, "ADMIN")


class FetchPrStatusTest(unittest.TestCase):
  @patch.object(_pr_utils, "run")
  def test_categorizes_checks(self, mock_run):
    mock_run.return_value = _proc(
      stdout=_pr_json(
        statusCheckRollup=[
          {"name": "a", "status": "COMPLETED", "conclusion": "SUCCESS"},
          {"name": "b", "status": "IN_PROGRESS"},
          {"name": "c", "status": "COMPLETED", "conclusion": "FAILURE"},
        ]
      )
    )
    data = _pr_utils.fetch_pr_status(Path("/repo"), 1, "t")
    self.assertEqual(data["passed_checks"], ["a"])
    self.assertEqual(data["pending_checks"], ["b"])
    self.assertEqual(data["failed_checks"], ["c"])

  @patch.object(_pr_utils, "run")
  def test_lookup_failure_halts(self, mock_run):
    mock_run.side_effect = _pr_utils.subprocess.CalledProcessError(
      1, ["gh", "pr", "view"], stderr="no such PR"
    )
    with self.assertRaises(SystemExit):
      _pr_utils.fetch_pr_status(Path("/repo"), 999, "t")


class CheckCleanBranchTest(unittest.TestCase):
  @patch.object(_pr_utils, "run")
  def test_detached_head_halts(self, mock_run):
    mock_run.return_value = _proc(stdout="")
    with self.assertRaises(SystemExit):
      _pr_utils.check_clean_branch(Path("/repo"), "main", "t")

  @patch.object(_pr_utils, "run")
  def test_same_as_base_halts(self, mock_run):
    mock_run.return_value = _proc(stdout="main")
    with self.assertRaises(SystemExit):
      _pr_utils.check_clean_branch(Path("/repo"), "main", "t")

  @patch.object(_pr_utils, "run")
  def test_dirty_tree_halts(self, mock_run):
    mock_run.side_effect = [
      _proc(stdout="feat/x"),
      _proc(stdout=" M some_file.py\n"),
    ]
    with self.assertRaises(SystemExit):
      _pr_utils.check_clean_branch(Path("/repo"), "main", "t")

  @patch.object(_pr_utils, "run")
  def test_clean_state_returns_branch(self, mock_run):
    mock_run.side_effect = [_proc(stdout="feat/x"), _proc(stdout="")]
    branch = _pr_utils.check_clean_branch(Path("/repo"), "main", "t")
    self.assertEqual(branch, "feat/x")


class CheckPrMainTest(unittest.TestCase):
  @patch.object(check_pr, "fetch_pr_status")
  @patch.object(check_pr, "get_viewer_login", return_value="me")
  @patch.object(check_pr, "check_auth_and_permission")
  @patch("sys.argv", ["check_pr.py", "42"])
  def test_mergeable_does_not_exit(self, _auth, _login, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "author": {"login": "someone_else"},
      "reviewDecision": "",
      "pending_checks": [],
      "passed_checks": ["test"],
      "failed_checks": [],
    }
    check_pr.main()  # falls off the end -- no SystemExit means "mergeable"

  @patch.object(check_pr, "fetch_pr_status")
  @patch.object(check_pr, "get_viewer_login", return_value="me")
  @patch.object(check_pr, "check_auth_and_permission")
  @patch("sys.argv", ["check_pr.py", "42"])
  def test_pending_check_exits_one(self, _auth, _login, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "author": {"login": "someone_else"},
      "reviewDecision": "",
      "pending_checks": ["validation"],
      "passed_checks": [],
      "failed_checks": [],
    }
    with self.assertRaises(SystemExit) as ctx:
      check_pr.main()
    self.assertEqual(ctx.exception.code, 1)

  @patch.object(check_pr, "fetch_pr_status")
  @patch.object(check_pr, "get_viewer_login", return_value="me")
  @patch.object(check_pr, "check_auth_and_permission")
  @patch("sys.argv", ["check_pr.py", "42"])
  def test_unsatisfied_review_exits_one(self, _auth, _login, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "author": {"login": "someone_else"},
      "reviewDecision": "REVIEW_REQUIRED",
      "pending_checks": [],
      "passed_checks": [],
      "failed_checks": [],
    }
    with self.assertRaises(SystemExit) as ctx:
      check_pr.main()
    self.assertEqual(ctx.exception.code, 1)

  @patch.object(check_pr, "fetch_pr_status")
  @patch.object(check_pr, "get_viewer_login", return_value="me")
  @patch.object(check_pr, "check_auth_and_permission")
  @patch("sys.argv", ["check_pr.py", "42"])
  def test_closed_state_exits_one(self, _auth, _login, mock_fetch):
    mock_fetch.return_value = {
      "state": "CLOSED",
      "author": {"login": "someone_else"},
      "reviewDecision": "",
      "pending_checks": [],
      "passed_checks": [],
      "failed_checks": [],
    }
    with self.assertRaises(SystemExit) as ctx:
      check_pr.main()
    self.assertEqual(ctx.exception.code, 1)


class ApprovePrCheckStateTest(unittest.TestCase):
  @patch.object(approve_pr, "fetch_pr_status")
  def test_not_open_halts(self, mock_fetch):
    mock_fetch.return_value = {
      "state": "MERGED",
      "author": {"login": "someone_else"},
      "reviewDecision": "",
      "pending_checks": [],
    }
    with self.assertRaises(SystemExit):
      approve_pr.check_pr_state(Path("/repo"), 42, "me")

  @patch.object(approve_pr, "fetch_pr_status")
  def test_self_authored_no_review_required_halts(self, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "author": {"login": "me"},
      "reviewDecision": "",
      "pending_checks": [],
    }
    with self.assertRaises(SystemExit):
      approve_pr.check_pr_state(Path("/repo"), 42, "me")

  @patch.object(approve_pr, "fetch_pr_status")
  def test_self_authored_review_required_halts(self, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "author": {"login": "me"},
      "reviewDecision": "REVIEW_REQUIRED",
      "pending_checks": [],
    }
    with self.assertRaises(SystemExit):
      approve_pr.check_pr_state(Path("/repo"), 42, "me")

  @patch.object(approve_pr, "fetch_pr_status")
  def test_pending_checks_warn_but_do_not_halt(self, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "author": {"login": "someone_else"},
      "reviewDecision": "",
      "pending_checks": ["validation"],
    }
    approve_pr.check_pr_state(Path("/repo"), 42, "me")  # no raise

  @patch.object(approve_pr, "fetch_pr_status")
  def test_other_author_all_clear_does_not_halt(self, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "author": {"login": "someone_else"},
      "reviewDecision": "APPROVED",
      "pending_checks": [],
    }
    approve_pr.check_pr_state(Path("/repo"), 42, "me")  # no raise


class MergePrCheckMergeableTest(unittest.TestCase):
  @patch.object(merge_pr, "fetch_pr_status")
  def test_not_open_halts(self, mock_fetch):
    mock_fetch.return_value = {"state": "CLOSED"}
    with self.assertRaises(SystemExit):
      merge_pr.check_mergeable(Path("/repo"), 42, is_admin=False)

  @patch.object(merge_pr, "fetch_pr_status")
  def test_pending_checks_halt(self, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "pending_checks": ["validation"],
      "failed_checks": [],
      "reviewDecision": "",
    }
    with self.assertRaises(SystemExit):
      merge_pr.check_mergeable(Path("/repo"), 42, is_admin=False)

  @patch.object(merge_pr, "fetch_pr_status")
  def test_failed_checks_halt(self, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "pending_checks": [],
      "failed_checks": ["test"],
      "reviewDecision": "",
    }
    with self.assertRaises(SystemExit):
      merge_pr.check_mergeable(Path("/repo"), 42, is_admin=False)

  @patch.object(merge_pr, "fetch_pr_status")
  def test_unsatisfied_review_halts_for_non_admin(self, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "pending_checks": [],
      "failed_checks": [],
      "reviewDecision": "REVIEW_REQUIRED",
    }
    with self.assertRaises(SystemExit):
      merge_pr.check_mergeable(Path("/repo"), 42, is_admin=False)

  @patch.object(merge_pr, "fetch_pr_status")
  def test_review_required_signals_admin_bypass(self, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "pending_checks": [],
      "failed_checks": [],
      "reviewDecision": "REVIEW_REQUIRED",
    }
    # admin bypass may apply -- caller should retry with --admin and
    # let GitHub's own merge call be the final word
    use_admin_bypass = merge_pr.check_mergeable(
      Path("/repo"), 42, is_admin=True
    )
    self.assertTrue(use_admin_bypass)

  @patch.object(merge_pr, "fetch_pr_status")
  def test_changes_requested_halts_even_for_admin(self, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "pending_checks": [],
      "failed_checks": [],
      "reviewDecision": "CHANGES_REQUESTED",
    }
    # an explicit human objection isn't silently overridden by admin
    with self.assertRaises(SystemExit):
      merge_pr.check_mergeable(Path("/repo"), 42, is_admin=True)

  @patch.object(merge_pr, "fetch_pr_status")
  def test_no_review_required_does_not_use_admin_bypass(self, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "pending_checks": [],
      "failed_checks": [],
      "reviewDecision": "",
    }
    use_admin_bypass = merge_pr.check_mergeable(
      Path("/repo"), 42, is_admin=False
    )
    self.assertFalse(use_admin_bypass)

  @patch.object(merge_pr, "fetch_pr_status")
  def test_approved_review_does_not_use_admin_bypass(self, mock_fetch):
    mock_fetch.return_value = {
      "state": "OPEN",
      "pending_checks": [],
      "failed_checks": [],
      "reviewDecision": "APPROVED",
    }
    use_admin_bypass = merge_pr.check_mergeable(
      Path("/repo"), 42, is_admin=False
    )
    self.assertFalse(use_admin_bypass)


class SubmitPrGuardTest(unittest.TestCase):
  @patch.object(submit_pr, "check_auth_and_permission")
  @patch.object(submit_pr, "check_clean_branch")
  @patch("sys.argv", ["submit_pr.py", "--title", "t", "--body", "b"])
  def test_delegates_to_check_clean_branch(self, mock_check_branch, _auth):
    mock_check_branch.return_value = "feat/x"
    with patch.object(submit_pr.subprocess, "run") as mock_subprocess_run:
      mock_subprocess_run.side_effect = [
        _proc(returncode=0),  # git push
        _proc(returncode=0),  # gh pr create
      ]
      with self.assertRaises(SystemExit) as ctx:
        submit_pr.main()
    self.assertEqual(ctx.exception.code, 0)
    push_call, create_call = mock_subprocess_run.call_args_list
    self.assertIn("push", push_call.args[0])
    self.assertIn("create", create_call.args[0])


if __name__ == "__main__":
  unittest.main()
