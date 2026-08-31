# ===================================================================
# tools/scripts/repo_utils/pr_submit_plugin.py
# ===================================================================
"""Runs the full "validate, then submit" PR chain: a hook validates
branch/tree state, a build+test+container-test pass runs, act
validates the PR workflow, and only then is a PR actually submitted
-- with a final hook confirming it landed. Deliberately NOT a bazel
target: it shells out to `bazel build`/`bazel test`/`bazel run`
itself, and a bazel target that re-invokes `bazel` from inside its
own sandbox is a known anti-pattern (see Step 2.1's coverage fix) --
sandbox restrictions and bazel-server lock contention. This script
lives outside bazel instead, the same way the root Makefile's
meta-targets (lint_fix, coverage, ...) do.

Never wired to a hook, CI, or any other automatic trigger --
PR submission is always an explicit, human-invoked action (see
submit_pr.py's own docstring and CLAUDE.md's git safety protocol).
Never calls approve_pr.py: submitting and approving a PR are always
separate operations, performed by different people.

Run via:
  python3 tools/scripts/repo_utils/pr_submit_plugin.py \
      --title "<title>" --body "<body>"
Or via the `/pr_submit` slash command
(`.claude/commands/pr_submit.md`), which drafts the title and
body from the branch's actual content before invoking this script.

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

# This script always runs directly (never via `bazel run`), so
# BUILD_WORKSPACE_DIRECTORY is never set -- unlike the bazel
# py_binary scripts, walk up from this file's own known depth
# instead: tools/scripts/repo_utils/pr_submit_plugin.py -> repo root.
# It's also imported as a plain module by pr_submit_plugin_test.py
# via bazel's py_test, where sys.path is set up for package-qualified
# imports but not for a bare same-directory one -- inserting the
# repo root here, unconditionally, before importing _pr_utils makes
# the package-qualified form resolve correctly in both contexts
# (walking up 3 parents lands at the repo root either way: the real
# one for a direct invocation, bazel's runfiles sandbox root for the
# test).
_REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(_REPO_ROOT))

from tools.scripts.repo_utils._pr_utils import check_clean_branch  # noqa: E402


def find_repo_root() -> Path:
  return _REPO_ROOT


def fail(message: str) -> None:
  print(f"pr_submit_plugin: FAIL -- {message}", file=sys.stderr)
  sys.exit(1)


def run(cmd, cwd, **kwargs):
  return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, **kwargs)


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


def skill_build_and_test(repo_root: Path) -> None:
  """Step 2 (skill) + Step 3 (hook): build, test, container tests."""
  commands = [
    ["bazel", "build", "//..."],
    ["bazel", "test", "//..."],
    ["bazel", "run", "//:container_tests"],
    ["bazel", "run", "//:dockerfile_container_tests"],
  ]
  for cmd in commands:
    print(f"pr_submit_plugin: running `{' '.join(cmd)}` ...")
    result = subprocess.run(cmd, cwd=repo_root)
    if result.returncode != 0:
      fail(f"`{' '.join(cmd)}` failed (exit {result.returncode}).")


def skill_act_check(repo_root: Path) -> None:
  """Step 4 (skill) + Step 5 (hook): act via //:act_check."""
  cmd = ["bazel", "run", "//:act_check"]
  print(f"pr_submit_plugin: running `{' '.join(cmd)}` ...")
  result = subprocess.run(cmd, cwd=repo_root)
  if result.returncode != 0:
    fail(
      f"`{' '.join(cmd)}` failed (exit {result.returncode}) -- act "
      "reported the PR workflow would not pass CI."
    )


def skill_submit_pr(
  repo_root: Path, title: str, body: str, base: str, draft: bool
) -> str:
  """Step 6 (skill): submit_pr.py, capturing the resulting PR number."""
  cmd = [
    "bazel",
    "run",
    "//:submit_pr",
    "--",
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
    fail(f"`//:submit_pr` failed (exit {result.returncode}).")

  pr_number = None
  for line in (result.stdout + result.stderr).splitlines():
    line = line.strip()
    if line.startswith("http") and "/pull/" in line:
      pr_number = line.rsplit("/", 1)[-1]
  if not pr_number:
    fail("could not determine the PR number from submit_pr's output.")
  return pr_number


def hook_confirm_pr_exists(repo_root: Path, pr_number: str) -> None:
  """Step 7 (hook): confirm the PR actually exists via `gh pr view`."""
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

  print("pr_submit_plugin: [1/7] hook - checking branch/tree state...")
  branch = hook_check_branch_state(repo_root, args.base)

  print("pr_submit_plugin: [2/7] skill - build + test + container tests...")
  skill_build_and_test(repo_root)
  print("pr_submit_plugin: [3/7] hook - build/test passed cleanly.")

  print("pr_submit_plugin: [4/7] skill - running //:act_check...")
  skill_act_check(repo_root)
  print("pr_submit_plugin: [5/7] hook - act passed cleanly.")

  print("pr_submit_plugin: [6/7] skill - submitting the pull request...")
  pr_number = skill_submit_pr(
    repo_root, args.title, args.body, args.base, args.draft
  )

  print("pr_submit_plugin: [7/7] hook - confirming the PR exists...")
  hook_confirm_pr_exists(repo_root, pr_number)

  print(
    f"pr_submit_plugin: SUCCESS -- PR #{pr_number} submitted from "
    f"'{branch}'."
  )


if __name__ == "__main__":
  main()
