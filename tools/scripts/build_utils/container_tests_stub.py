# ===================================================================
# tools/scripts/build_utils/container_tests_stub.py
# ===================================================================
"""Stub for `container_tests`/`dockerfile_container_tests`. Exists
so `pr_submit_plugin.py`'s build+test chain runs the identical
4-command sequence (`bazel build //...`, `bazel test //...`,
`bazel run //:container_tests`, `bazel run
//:dockerfile_container_tests`) in every sister repo, whether or not
that repo has any real bazel oci_image/Dockerfile targets yet.
Exits 0 unconditionally -- there is nothing to validate here.

Objective: the moment this repo gains its first oci_image target,
replace the corresponding `py_binary` stub in BUILD.bazel with a
real `py_binary_tests_suite(...)` (see ITDev's BUILD.bazel and
tools/container_test.bzl for the target shape to copy), and drop
this stub's `args` entry for that suite. Once both suites are real,
delete this file.

Sync note: this file is intentionally duplicated (not symlinked)
across every sister repo that doesn't yet have real container
targets -- aim, personal, ai_workbench, la_workbench. Any change
here must be ported to the same path in the others. Spot-check
with:
  diff <this-file> ../<other-repo>/<same-relative-path>

Run via:
  bazel run //:container_tests
  bazel run //:dockerfile_container_tests
"""

import sys


def main() -> int:
  suite = sys.argv[1] if len(sys.argv) > 1 else "<unknown suite>"
  print(
    f"{suite}: STUB -- no bazel oci_image/Dockerfile targets exist "
    "in this repo yet, nothing to run."
  )
  return 0


if __name__ == "__main__":
  sys.exit(main())
