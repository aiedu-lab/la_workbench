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
  # --reuse: on Docker Desktop's WSL2 backend, the vsock-forwarded
  # docker.sock adds enough latency that act's own post-success
  # container-removal call can exceed its internal context deadline
  # -- act then reports the whole run as failed even though the job
  # itself passed. --reuse skips that removal (keeping the container
  # for the next run) and sidesteps the timeout entirely; run
  # `docker container prune` occasionally to reclaim them.
  cmd = [
    "act",
    "pull_request",
    "-j",
    args.job,
    "-W",
    args.workflow,
    "--reuse",
  ]
  result = subprocess.run(cmd, cwd=workspace_root)
  sys.exit(result.returncode)


if __name__ == "__main__":
  main()
