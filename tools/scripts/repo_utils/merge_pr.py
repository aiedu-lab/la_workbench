# ===================================================================
# tools/scripts/repo_utils/merge_pr.py
# ===================================================================
"""Merges a pull request via `gh pr merge`, after explicitly
confirming it's actually safe to merge rather than trusting gh's own
opaque mergeable/mergeStateStatus fields. Deliberately a py_binary,
never py_test: this merges a real PR into a real branch, so it must
only ever run when a human explicitly invokes it with an explicit PR
number -- never wired to a hook, CI, or any other automatic trigger.

Checks performed before merging:
  a) every check run has finished, and none of them failed
  b) either no review is required (reviewDecision is empty -- the
     common case on a repo that can't turn on required reviews at
     all, e.g. a private repo on GitHub's Free plan), or one is
     required and has already been satisfied (reviewDecision ==
     APPROVED), or one is required but nobody's reviewed yet
     (REVIEW_REQUIRED) and the caller is an ADMIN -- branch
     protection may exempt admins from the requirement, so that case
     is a soft warning, not a hard block: `gh pr merge` is retried
     with `--admin` (confirmed by hand: gh refuses to use an admin
     bypass that's actually configured unless --admin is passed
     explicitly, even though the plain command's own error message
     says the policy prohibits the merge) and GitHub's own API is
     the final word on whether the bypass is real. CHANGES_REQUESTED
     always hard-blocks regardless of permission -- that's an
     explicit human objection, not just "no review yet", and admin
     status shouldn't silently override it.

Run via:
  bazel run //:merge_pr -- 123
  bazel run //:merge_pr -- 123 --method squash --delete-branch

Sync note: this file is intentionally duplicated (not symlinked)
across every sister repo -- ITDev, aim, personal, ai_workbench,
la_workbench -- so each stays a standalone checkout. Any change here
(a bug fix, a new flag, a refactored helper) must be ported to the
same path in every other repo, except for narrow, explicitly
commented repo-specific differences (e.g. a STUB build/test step).
Spot-check with:
  diff <this-file> ../<other-repo>/<same-relative-path>
"""

import argparse
import subprocess
import sys
from pathlib import Path

from tools.scripts.build_utils._container_checks import find_workspace_root
from tools.scripts.repo_utils._pr_utils import (
  check_auth_and_permission,
  fetch_pr_status,
)

MIN_PERMISSION = {"WRITE", "MAINTAIN", "ADMIN"}


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("pr_number", type=int)
  parser.add_argument(
    "--method", choices=["merge", "squash", "rebase"], default="merge"
  )
  parser.add_argument("--delete-branch", action="store_true")
  return parser.parse_args()


def check_mergeable(workspace_root, pr_number, is_admin):
  """Returns True if the merge should be attempted with --admin
  (nobody's reviewed yet, but the caller is ADMIN and branch
  protection may exempt them), False if a plain merge is fine.
  Exits directly for every case that should block the merge outright.
  """
  data = fetch_pr_status(workspace_root, pr_number, "merge_pr")

  if data["state"] != "OPEN":
    print(
      f"merge_pr: PR #{pr_number} is {data['state']}, not OPEN -- "
      "nothing to merge.",
      file=sys.stderr,
    )
    sys.exit(1)

  pending = data["pending_checks"]
  if pending:
    print(
      f"merge_pr: {len(pending)} check(s) still running on PR "
      f"#{pr_number}: {', '.join(pending)} -- wait for them to "
      "finish before merging.",
      file=sys.stderr,
    )
    sys.exit(1)

  failed = data["failed_checks"]
  if failed:
    print(
      f"merge_pr: {len(failed)} check(s) failed on PR #{pr_number}: "
      f"{', '.join(failed)} -- fix them before merging.",
      file=sys.stderr,
    )
    sys.exit(1)

  review_decision = data["reviewDecision"]
  if review_decision == "REVIEW_REQUIRED" and is_admin:
    print(
      f"merge_pr: PR #{pr_number} hasn't been reviewed yet, but "
      "you're ADMIN -- retrying with --admin in case branch "
      "protection exempts you from the requirement. GitHub's own "
      "API has the final word on whether that bypass is real.",
      file=sys.stderr,
    )
    return True
  if review_decision not in ("", "APPROVED"):
    note = ""
    if review_decision == "REVIEW_REQUIRED":
      note = (
        " (note: if you opened this PR, GitHub won't let you "
        "approve your own -- a different collaborator needs to.)"
      )
    print(
      f"merge_pr: PR #{pr_number} requires a review that hasn't "
      f"been satisfied yet (reviewDecision={review_decision}).{note}",
      file=sys.stderr,
    )
    sys.exit(1)
  return False


def main():
  args = parse_args()
  workspace_root = find_workspace_root(Path(__file__))

  permission = check_auth_and_permission(
    workspace_root, MIN_PERMISSION, "merge_pr"
  )
  use_admin_bypass = check_mergeable(
    workspace_root, args.pr_number, is_admin=(permission == "ADMIN")
  )

  merge_cmd = ["gh", "pr", "merge", str(args.pr_number), f"--{args.method}"]
  if args.delete_branch:
    merge_cmd.append("--delete-branch")
  if use_admin_bypass:
    merge_cmd.append("--admin")
  result = subprocess.run(merge_cmd, cwd=workspace_root)
  sys.exit(result.returncode)


if __name__ == "__main__":
  main()
