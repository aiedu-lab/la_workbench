# ===================================================================
# tools/scripts/repo_utils/pr_submit.py
# ===================================================================
"""Pushes the current branch and opens a pull request via `gh pr
create`. Deliberately a py_binary, never py_test: this pushes to a
real remote and opens a real PR, so it must only ever run when a
human explicitly invokes it with explicit arguments -- never wired
to a hook, CI, or any other automatic trigger. This matches
AGENTS.md's own §6 ("Branching and Merging"): generating a PR is
always a manual decision, never something Claude triggers itself.

Shares its auth/permission and clean-branch preflight logic with
pr_check.py/pr_approve.py/pr_merge.py/pr_submit_plugin.py via
_pr_utils.py (ported from ../aim's DRY refactor of this file,
itself ported from ../ITDev) so the repeated checks stay identical
and get fixed in one place.

Run via:
  bazel run //:pr_submit -- --title "<title>" --body "<body>"
  bazel run //:pr_submit -- --title "..." --body "..." --base main \
      --draft

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
  check_clean_branch,
)

# GitHub's viewerPermission values, highest to lowest: ADMIN,
# MAINTAIN, WRITE, TRIAGE, READ, NONE. Submitting a PR needs push
# access to open a branch-backed PR.
MIN_PERMISSION = {"WRITE", "MAINTAIN", "ADMIN"}


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--title", required=True)
  parser.add_argument("--body", required=True)
  parser.add_argument("--base", default="main")
  parser.add_argument("--draft", action="store_true")
  return parser.parse_args()


def main():
  args = parse_args()
  workspace_root = find_workspace_root(Path(__file__))

  check_auth_and_permission(workspace_root, MIN_PERMISSION, "pr_submit")
  branch = check_clean_branch(workspace_root, args.base, "pr_submit")

  print(f"pr_submit: pushing '{branch}' to origin...")
  push_result = subprocess.run(
    ["git", "push", "-u", "origin", branch], cwd=workspace_root
  )
  if push_result.returncode != 0:
    sys.exit(push_result.returncode)

  create_cmd = [
    "gh",
    "pr",
    "create",
    "--title",
    args.title,
    "--body",
    args.body,
    "--base",
    args.base,
  ]
  if args.draft:
    create_cmd.append("--draft")
  create_result = subprocess.run(create_cmd, cwd=workspace_root)
  sys.exit(create_result.returncode)


if __name__ == "__main__":
  main()
