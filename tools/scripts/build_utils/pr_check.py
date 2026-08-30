# ===================================================================
# tools/scripts/build_utils/pr_check.py
# ===================================================================
"""Runs `act` against a GitHub Actions workflow to validate a pull
request will pass CI, against the current local branch tip, before
pushing. Deliberately a py_binary, never py_test: `act` needs Docker
and the real, live working tree (.git, .github/workflows/), neither
of which is a declarable hermetic bazel `data` dependency, so this
intentionally opts out of bazel test's sandboxing model. Being a
py_binary also means `bazel test //...` can never discover it.

Ported from ../aim's version of this file (itself ported from
../ITDev). Targets a stub `.github/workflows/pr-validation.yaml` --
this repo has no real CI gate yet (see README.md's "How to Make
Changes" TODO).

Run via `bazel run //:pr_check` (defaults) or
`bazel run //:pr_check -- --workflow <path> --job <job-id>` to
target a different workflow/job.
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from tools.scripts.build_utils._container_checks import find_workspace_root

DEFAULT_WORKFLOW = ".github/workflows/pr-validation.yaml"
DEFAULT_JOB = "validation"


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    "--workflow",
    default=DEFAULT_WORKFLOW,
    help=f"Workflow file to run (default: {DEFAULT_WORKFLOW}).",
  )
  parser.add_argument(
    "--job",
    default=DEFAULT_JOB,
    help=f"Job id within the workflow to run (default: {DEFAULT_JOB}).",
  )
  return parser.parse_args()


def main():
  args = parse_args()
  if shutil.which("act") is None:
    print(
      "pr_check: 'act' is not on PATH -- install it "
      "(https://github.com/nektos/act) to validate PRs locally.",
      file=sys.stderr,
    )
    sys.exit(1)

  workspace_root = find_workspace_root(Path(__file__))
  cmd = ["act", "pull_request", "-j", args.job, "-W", args.workflow]
  result = subprocess.run(cmd, cwd=workspace_root)
  sys.exit(result.returncode)


if __name__ == "__main__":
  main()
