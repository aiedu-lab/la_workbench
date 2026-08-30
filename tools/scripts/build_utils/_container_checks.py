# ===================================================================
# tools/scripts/build_utils/_container_checks.py
# ===================================================================
"""Ported from ../aim's version of this file (itself ported from
../ITDev), keeping only `find_workspace_root` -- this repo has no
container/docker tests (yet), so the docker-specific helpers there
don't apply here.
"""

import os
from pathlib import Path


def find_workspace_root(start: Path) -> Path:
  """Return the real, live workspace root -- NOT bazel's execroot.

  WHY not just walk up looking for a MODULE.bazel marker: bazel's
  own execroot mirrors MODULE.bazel too (it's a declared source
  file), so that heuristic is ambiguous and can silently resolve to
  the sandboxed execroot instead of the live checkout. That matters
  here because `git`/`gh` need the real, live repo (`.git`, real
  branch state), not bazel's dependency-closure-only mirror of it.

  `BUILD_WORKSPACE_DIRECTORY` is bazel run's own answer to exactly
  this problem, and since it's a plain env var it survives being
  inherited across subprocess.run([binary, ...]) calls.
  """
  workspace_dir = os.environ.get("BUILD_WORKSPACE_DIRECTORY")
  if workspace_dir:
    return Path(workspace_dir)
  raise EnvironmentError(
    "BUILD_WORKSPACE_DIRECTORY is not set -- this must be invoked "
    "via `bazel run`, not `bazel build`/`bazel test`, or executed "
    f"directly outside of bazel (start={start})."
  )
