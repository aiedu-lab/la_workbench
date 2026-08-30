# ===================================================================
# tools/scripts/repo_utils/pr_submit_plugin.py
# ===================================================================
"""Runs the "validate, then submit" PR chain for this non-coding
repo: a hook validates branch/tree state, then a PR is actually
submitted, with a final hook confirming it landed. Deliberately
omits the build/test and `act` steps entirely -- this repo has no
bazel setup and nothing to build or CI-check locally, unlike the
coding repos (ITDev, aim, personal) that run a fuller 7-step chain.

Never wired to a hook, CI, or any other automatic trigger -- PR
submission is always an explicit, human-invoked action (see
submit_pr.py's own docstring and AGENTS.md's git safety protocol).
Never calls approve_pr.py: submitting and approving a PR are always
separate operations, performed by different people.

Run via:
  python3 tools/scripts/repo_utils/pr_submit_plugin.py \
      --title "<title>" --body "<body>"
"""

import argparse
import subprocess
import sys
from pathlib import Path

from _pr_utils import check_clean_branch


def find_repo_root() -> Path:
  # tools/scripts/repo_utils/pr_submit_plugin.py -> repo root.
  return Path(__file__).resolve().parents[3]


def fail(message: str) -> None:
  print(f"pr_submit_plugin: FAIL -- {message}", file=sys.stderr)
  sys.exit(1)


def run(cmd, cwd, **kwargs):
  return subprocess.run(
    cmd, cwd=cwd, text=True, capture_output=True, **kwargs
  )


def hook_check_branch_state(repo_root: Path, base: str) -> str:
  """Step 1 (hook): not base, tree clean, local == pushed remote tip."""
  branch = check_clean_branch(repo_root, base, "pr_submit_plugin")

  fetch = subprocess.run(["git", "fetch", "origin", branch], cwd=repo_root)
  if fetch.returncode != 0:
    fail(f"could not fetch origin/{branch}.")

  local_sha = run(["git", "rev-parse", "HEAD"], repo_root).stdout.strip()
  remote_ref = run(["git", "rev-parse", f"origin/{branch}"], repo_root)
  if remote_ref.returncode != 0:
    fail(f"branch '{branch}' has no upstream on origin -- push it first.")
  remote_sha = remote_ref.stdout.strip()

  if local_sha != remote_sha:
    fail(
      f"local HEAD ({local_sha[:8]}) != origin/{branch} "
      f"({remote_sha[:8]}) -- push or pull to sync first."
    )
  return branch


def skill_submit_pr(
  repo_root: Path, title: str, body: str, base: str, draft: bool
) -> str:
  """Step 2 (skill): submit_pr.py, capturing the resulting PR number."""
  cmd = [
    "python3",
    str(repo_root / "tools/scripts/repo_utils/submit_pr.py"),
    "--title",
    title,
    "--body",
    body,
    "--base",
    base,
  ]
  if draft:
    cmd.append("--draft")
  print(f"pr_submit_plugin: running `{' '.join(cmd)}` ...")
  result = subprocess.run(cmd, cwd=repo_root, capture_output=True, text=True)
  print(result.stdout)
  print(result.stderr, file=sys.stderr)
  if result.returncode != 0:
    fail(f"`submit_pr.py` failed (exit {result.returncode}).")

  pr_number = None
  for line in (result.stdout + result.stderr).splitlines():
    line = line.strip()
    if line.startswith("http") and "/pull/" in line:
      pr_number = line.rsplit("/", 1)[-1]
  if not pr_number:
    fail("could not determine the PR number from submit_pr's output.")
  return pr_number


def hook_confirm_pr_exists(repo_root: Path, pr_number: str) -> None:
  """Step 3 (hook): confirm the PR actually exists via `gh pr view`."""
  result = subprocess.run(
    ["gh", "pr", "view", pr_number],
    cwd=repo_root,
    capture_output=True,
    text=True,
  )
  if result.returncode != 0:
    fail(
      f"`gh pr view {pr_number}` failed -- the PR may not have been "
      "created correctly."
    )
  print(f"pr_submit_plugin: confirmed PR #{pr_number} exists.")
  print(result.stdout)


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--title", required=True)
  parser.add_argument("--body", required=True)
  parser.add_argument("--base", default="main")
  parser.add_argument("--draft", action="store_true")
  return parser.parse_args()


def main():
  args = parse_args()
  repo_root = find_repo_root()

  print("pr_submit_plugin: [1/3] hook - checking branch/tree state...")
  branch = hook_check_branch_state(repo_root, args.base)

  print("pr_submit_plugin: [2/3] skill - submitting the pull request...")
  pr_number = skill_submit_pr(
    repo_root, args.title, args.body, args.base, args.draft
  )

  print("pr_submit_plugin: [3/3] hook - confirming the PR exists...")
  hook_confirm_pr_exists(repo_root, pr_number)

  print(
    f"pr_submit_plugin: SUCCESS -- PR #{pr_number} submitted from "
    f"'{branch}'."
  )


if __name__ == "__main__":
  main()
