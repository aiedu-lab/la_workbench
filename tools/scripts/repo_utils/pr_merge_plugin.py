# ===================================================================
# tools/scripts/repo_utils/pr_merge_plugin.py
# ===================================================================
"""Runs a "wait for checks, then merge" chain: polls the PR's status
checks until none are pending (or a timeout elapses), then merges it
via //:merge_pr -- which already knows how to retry with --admin
when a review is required but the caller is exempt -- confirming
with a final hook that it actually landed. Deliberately NOT a bazel
target, for the same reason pr_submit_plugin.py isn't: it shells out
to `bazel run` itself, and a bazel target re-invoking bazel from
inside its own sandbox is a known anti-pattern.

Never wired to a hook, CI, or any other automatic trigger -- merging
a PR is always an explicit, human-invoked action. Never calls
approve_pr.py: this chain never attempts to approve its own PR --
see merge_pr.py's own docstring for why that's fundamentally
impossible (GitHub rejects self-approval unconditionally) and,
separately, unnecessary whenever an admin bypass applies.

Deliberately does NOT look at reviewDecision at all: merge_pr.py
itself is the sole authority on whether an unsatisfied review blocks
the merge or is bypassable, so re-deciding that here would just
duplicate (and risk drifting from) that logic.

Run via:
  python3 tools/scripts/repo_utils/pr_merge_plugin.py 123
  python3 tools/scripts/repo_utils/pr_merge_plugin.py 123 \
      --method squash --delete-branch --timeout 900
"""

import argparse
import subprocess
import sys
import time
from pathlib import Path

# This script always runs directly (never via `bazel run`), so
# BUILD_WORKSPACE_DIRECTORY is never set -- see pr_submit_plugin.py's
# docstring for why the repo root is inserted into sys.path here
# before a package-qualified import, rather than walking up and
# using a bare same-directory import: this file is also imported as
# a plain module by pr_merge_plugin_test.py via bazel's py_test.
_REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(_REPO_ROOT))

from tools.scripts.repo_utils._pr_utils import fetch_pr_status  # noqa: E402


def find_repo_root() -> Path:
  return _REPO_ROOT


def fail(message: str) -> None:
  print(f"pr_merge_plugin: FAIL -- {message}", file=sys.stderr)
  sys.exit(1)


def hook_wait_for_checks(
  repo_root: Path, pr_number: int, poll_interval: float, timeout: float
) -> None:
  """Step 1 (hook): poll until no checks are pending, or fail if any
  have failed or the timeout elapses.
  """
  deadline = time.monotonic() + timeout
  while True:
    data = fetch_pr_status(repo_root, pr_number, "pr_merge_plugin")
    if data["state"] != "OPEN":
      fail(f"PR #{pr_number} is {data['state']}, not OPEN.")

    if not data["pending_checks"]:
      if data["failed_checks"]:
        fail(
          f"check(s) failed on PR #{pr_number}: "
          f"{', '.join(data['failed_checks'])} -- fix them before "
          "merging."
        )
      return

    if time.monotonic() >= deadline:
      fail(
        f"timed out after {timeout:.0f}s waiting on PR #{pr_number}: "
        f"{', '.join(data['pending_checks'])}."
      )
    print(
      f"pr_merge_plugin: waiting on {', '.join(data['pending_checks'])} "
      f"(retrying in {poll_interval:.0f}s)..."
    )
    time.sleep(poll_interval)


def skill_merge_pr(
  repo_root: Path, pr_number: int, method: str, delete_branch: bool
) -> None:
  """Step 2 (skill): //:merge_pr."""
  cmd = [
    "bazel",
    "run",
    "//:merge_pr",
    "--",
    str(pr_number),
    "--method",
    method,
  ]
  if delete_branch:
    cmd.append("--delete-branch")
  print(f"pr_merge_plugin: running `{' '.join(cmd)}` ...")
  result = subprocess.run(cmd, cwd=repo_root)
  if result.returncode != 0:
    fail(f"`//:merge_pr` failed (exit {result.returncode}).")


def hook_confirm_merged(repo_root: Path, pr_number: int) -> None:
  """Step 3 (hook): confirm state == MERGED via `gh pr view`."""
  result = subprocess.run(
    ["gh", "pr", "view", str(pr_number), "--json", "state", "-q", ".state"],
    cwd=repo_root,
    capture_output=True,
    text=True,
  )
  state = result.stdout.strip()
  if result.returncode != 0 or state != "MERGED":
    fail(f"PR #{pr_number} does not show as MERGED (state={state!r}).")
  print(f"pr_merge_plugin: confirmed PR #{pr_number} is MERGED.")


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("pr_number", type=int)
  parser.add_argument(
    "--method", choices=["merge", "squash", "rebase"], default="merge"
  )
  parser.add_argument("--delete-branch", action="store_true")
  parser.add_argument("--poll-interval", type=float, default=15.0)
  parser.add_argument("--timeout", type=float, default=1800.0)
  return parser.parse_args()


def main():
  args = parse_args()
  repo_root = find_repo_root()

  print(
    f"pr_merge_plugin: [1/3] hook - waiting for checks on PR "
    f"#{args.pr_number}..."
  )
  hook_wait_for_checks(
    repo_root, args.pr_number, args.poll_interval, args.timeout
  )

  print("pr_merge_plugin: [2/3] skill - merging the pull request...")
  skill_merge_pr(
    repo_root, args.pr_number, args.method, args.delete_branch
  )

  print("pr_merge_plugin: [3/3] hook - confirming the PR merged...")
  hook_confirm_merged(repo_root, args.pr_number)

  print(f"pr_merge_plugin: SUCCESS -- PR #{args.pr_number} merged.")


if __name__ == "__main__":
  main()
