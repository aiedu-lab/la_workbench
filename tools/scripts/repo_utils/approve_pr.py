# ===================================================================
# tools/scripts/repo_utils/approve_pr.py
# ===================================================================
"""Approves a pull request as a repo maintainer, via `gh pr review
--approve`. Deliberately human-invoked only: this posts a real
approval review to a real PR, so it must only ever run when a human
explicitly invokes it with an explicit PR number -- never wired to a
hook, CI, or any other automatic trigger.

This repo has no bazel setup, so this runs via plain `python3`, not
`bazel run` -- see submit_pr.py's docstring for why this resolves
the repo root by walking up from its own file depth rather than via
`BUILD_WORKSPACE_DIRECTORY`.

Run via:
  python3 tools/scripts/repo_utils/approve_pr.py 123
  python3 tools/scripts/repo_utils/approve_pr.py 123 --body "LGTM"
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

# GitHub's viewerPermission values, highest to lowest: ADMIN,
# MAINTAIN, WRITE, TRIAGE, READ, NONE. Approving "as a maintainer"
# requires MAINTAIN or ADMIN, not just WRITE.
MIN_PERMISSION = {"MAINTAIN", "ADMIN"}


def find_repo_root() -> Path:
  # tools/scripts/repo_utils/approve_pr.py -> repo root.
  return Path(__file__).resolve().parents[3]


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("pr_number", type=int)
  parser.add_argument("--body", default=None)
  return parser.parse_args()


def run(cmd, cwd):
  return subprocess.run(
    cmd, cwd=cwd, check=True, text=True, capture_output=True
  )


def check_auth_and_permission(workspace_root, min_permission):
  if shutil.which("gh") is None:
    print(
      "approve_pr: 'gh' is not on PATH -- install the GitHub CLI "
      "(https://cli.github.com/).",
      file=sys.stderr,
    )
    sys.exit(1)

  try:
    run(["gh", "auth", "status"], workspace_root)
  except subprocess.CalledProcessError as e:
    print(
      "approve_pr: not authenticated -- run `gh auth login` first.",
      file=sys.stderr,
    )
    print(e.stderr, file=sys.stderr)
    sys.exit(1)

  try:
    permission = run(
      [
        "gh",
        "repo",
        "view",
        "--json",
        "viewerPermission",
        "-q",
        ".viewerPermission",
      ],
      workspace_root,
    ).stdout.strip()
  except subprocess.CalledProcessError as e:
    print("approve_pr: could not determine repo permission.", file=sys.stderr)
    print(e.stderr, file=sys.stderr)
    sys.exit(1)

  if permission not in min_permission:
    print(
      f"approve_pr: insufficient permission ({permission}) to "
      f"approve a pull request as maintainer -- need one of "
      f"{sorted(min_permission)}.",
      file=sys.stderr,
    )
    sys.exit(1)


def main():
  args = parse_args()
  workspace_root = find_repo_root()

  check_auth_and_permission(workspace_root, MIN_PERMISSION)

  review_cmd = ["gh", "pr", "review", str(args.pr_number), "--approve"]
  if args.body:
    review_cmd += ["--body", args.body]
  result = subprocess.run(review_cmd, cwd=workspace_root)
  sys.exit(result.returncode)


if __name__ == "__main__":
  main()
