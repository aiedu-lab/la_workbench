# ===================================================================
# tools/scripts/repo_utils/check_pr.py
# ===================================================================
"""Reports a pull request's mergeability status: is it OPEN, have
all checks finished (and did they pass), and is any required review
satisfied. Read-only -- never mutates the PR, so unlike
submit_pr/approve_pr/merge_pr this is safe to run any time.

This repo has no bazel setup, so this runs via plain python3 -- see
_pr_utils.py's docstring for why find_repo_root() walks up from its
own file depth instead of using BUILD_WORKSPACE_DIRECTORY.

Exit code doubles as a yes/no answer for scripting: 0 if the PR
looks safe to merge right now, 1 otherwise (with the specific reason
printed).

Run via:
  python3 tools/scripts/repo_utils/check_pr.py 123
"""

import argparse
import sys

from _pr_utils import (
  check_auth_and_permission,
  fetch_pr_status,
  find_repo_root,
  get_viewer_login,
)

MIN_PERMISSION = {"READ", "TRIAGE", "WRITE", "MAINTAIN", "ADMIN"}


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("pr_number", type=int)
  return parser.parse_args()


def main():
  args = parse_args()
  workspace_root = find_repo_root()

  check_auth_and_permission(workspace_root, MIN_PERMISSION, "check_pr")
  viewer_login = get_viewer_login(workspace_root)
  data = fetch_pr_status(workspace_root, args.pr_number, "check_pr")

  blockers = []

  print(f"check_pr: PR #{args.pr_number} is {data['state']}")
  if data["state"] != "OPEN":
    blockers.append(f"state is {data['state']}, not OPEN")

  if data["passed_checks"]:
    print(f"  passed:  {', '.join(data['passed_checks'])}")
  if data["pending_checks"]:
    print(f"  pending: {', '.join(data['pending_checks'])}")
    blockers.append(f"{len(data['pending_checks'])} check(s) still running")
  if data["failed_checks"]:
    print(f"  failed:  {', '.join(data['failed_checks'])}")
    blockers.append(f"{len(data['failed_checks'])} check(s) failed")

  review_decision = data["reviewDecision"] or "(no review required)"
  print(f"  review:  {review_decision}")
  if data["reviewDecision"] not in ("", "APPROVED"):
    blockers.append(
      f"review not satisfied (reviewDecision={data['reviewDecision']})"
    )

  author_login = data["author"]["login"]
  is_author = author_login == viewer_login
  print(f"  author:  {author_login}" + (" (you)" if is_author else ""))
  if is_author and data["reviewDecision"] == "REVIEW_REQUIRED":
    print(
      "  note: you opened this PR -- GitHub won't let you approve "
      "your own, a different collaborator needs to"
    )

  if blockers:
    print(f"check_pr: NOT mergeable -- {'; '.join(blockers)}", file=sys.stderr)
    sys.exit(1)

  print("check_pr: mergeable")


if __name__ == "__main__":
  main()
