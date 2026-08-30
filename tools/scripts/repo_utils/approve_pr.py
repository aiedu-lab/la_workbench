# ===================================================================
# tools/scripts/repo_utils/approve_pr.py
# ===================================================================
"""Approves a pull request as a repo maintainer, via `gh pr review
--approve`. Deliberately human-invoked only: this posts a real
approval review to a real PR, so it must only ever run when a human
explicitly invokes it with an explicit PR number -- never wired to a
hook, CI, or any other automatic trigger.

This repo has no bazel setup, so this runs via plain `python3` --
see _pr_utils.py's docstring for why find_repo_root() walks up from
its own file depth instead of `BUILD_WORKSPACE_DIRECTORY`.

Run via:
  python3 tools/scripts/repo_utils/approve_pr.py 123
  python3 tools/scripts/repo_utils/approve_pr.py 123 --body "LGTM"
"""

import argparse
import subprocess
import sys

from _pr_utils import (
  check_auth_and_permission,
  fetch_pr_status,
  find_repo_root,
  get_viewer_login,
)

# GitHub's viewerPermission values, highest to lowest: ADMIN,
# MAINTAIN, WRITE, TRIAGE, READ, NONE. Approving "as a maintainer"
# requires MAINTAIN or ADMIN, not just WRITE.
MIN_PERMISSION = {"MAINTAIN", "ADMIN"}


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("pr_number", type=int)
  parser.add_argument("--body", default=None)
  return parser.parse_args()


def check_pr_state(workspace_root, pr_number, viewer_login):
  """Surfaces the two most common reasons `gh pr review --approve`
  fails or looks stuck, before making the API call that would
  otherwise report them as a single opaque error:
    1. required checks still running (doesn't block approval, but
       will block merging -- worth flagging so a later failure isn't
       mistaken for a checks-pending issue, and vice versa)
    2. the PR author == viewer: GitHub's REST/GraphQL API rejects
       self-approval unconditionally, for every permission level,
       with no per-repo/org setting to disable it. Detecting this
       upfront avoids a cryptic GraphQL error and points at the
       actual next step instead.
  """
  data = fetch_pr_status(workspace_root, pr_number, "approve_pr")

  if data["state"] != "OPEN":
    print(
      f"approve_pr: PR #{pr_number} is {data['state']}, not OPEN -- "
      "nothing to approve.",
      file=sys.stderr,
    )
    sys.exit(1)

  pending = data["pending_checks"]
  if pending:
    print(
      f"approve_pr: WARNING -- {len(pending)} check(s) still running "
      f"on PR #{pr_number}: {', '.join(pending)}. Approving doesn't "
      "require checks to pass, but merging will stay blocked until "
      "they finish -- so if something below fails, it's likely "
      "unrelated to this.",
      file=sys.stderr,
    )

  if data["author"]["login"] == viewer_login:
    if data["reviewDecision"]:
      next_step = (
        "this repo requires a review, so you'll need a second "
        "collaborator to approve it."
      )
    else:
      next_step = (
        "this repo has no required-review rule on this PR "
        f"(reviewDecision is empty), so no approval is actually "
        f"needed -- merge directly instead: "
        f"`gh pr merge {pr_number} --merge` (or --squash/--rebase), "
        "or use the web UI's Merge button."
      )
    print(
      f"approve_pr: PR #{pr_number} was opened by you ({viewer_login}). "
      "GitHub rejects self-approval unconditionally -- there is no "
      f"permission level or repo/org setting that allows it. {next_step}",
      file=sys.stderr,
    )
    sys.exit(1)


def main():
  args = parse_args()
  workspace_root = find_repo_root()

  check_auth_and_permission(workspace_root, MIN_PERMISSION, "approve_pr")
  viewer_login = get_viewer_login(workspace_root)
  check_pr_state(workspace_root, args.pr_number, viewer_login)

  review_cmd = ["gh", "pr", "review", str(args.pr_number), "--approve"]
  if args.body:
    review_cmd += ["--body", args.body]
  result = subprocess.run(review_cmd, cwd=workspace_root)
  sys.exit(result.returncode)


if __name__ == "__main__":
  main()
