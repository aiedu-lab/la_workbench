#!/usr/bin/env python3
"""Set up the LA Workbench student lab environment.

Steps performed (all idempotent — safe to re-run):
1. Create `.venv` at the repo root if absent.
2. Install pip-tools into the venv.
3. Compile requirements.in -> requirements.txt via pip-compile.
4. Sync the venv to exactly match requirements.txt via pip-sync.
5. Register a Jupyter kernel backed by the venv.
6. Point git at .githooks/ so solution.md submissions are
   validated before commit.

Run from anywhere — paths are resolved relative to this file.
"""
import subprocess
import sys
from pathlib import Path

STUDENT_DIR = Path(__file__).resolve().parent
REPO_ROOT = STUDENT_DIR.parent.parent.parent
VENV = REPO_ROOT / ".venv"
VENV_PYTHON = VENV / "bin" / "python3"
VENV_PIP = VENV / "bin" / "pip"
REQUIREMENTS_IN = STUDENT_DIR / "requirements.in"
REQUIREMENTS_TXT = STUDENT_DIR / "requirements.txt"
KERNEL_NAME = "la-workbench"
KERNEL_DISPLAY_NAME = "Python3 (LA Workbench .venv)"


def _run(cmd: list[str], **kwargs) -> None:
  print(f"  RUN  {' '.join(cmd)}")
  subprocess.run(cmd, check=True, **kwargs)


def _create_venv() -> None:
  if VENV_PYTHON.exists():
    print(f"  OK   venv already exists: {VENV} (skipping)")
    return
  print(f"  VENV creating {VENV} ...")
  _run([sys.executable, "-m", "venv", str(VENV)])
  print("  OK   venv created")


def _install_pip_tools() -> None:
  _run([str(VENV_PIP), "install", "--upgrade", "pip", "pip-tools"])


def _compile_requirements() -> None:
  print(f"  COMPILE {REQUIREMENTS_IN.name} -> {REQUIREMENTS_TXT.name}")
  _run(
    [str(VENV / "bin" / "pip-compile"), REQUIREMENTS_IN.name],
    cwd=str(STUDENT_DIR),
  )


def _sync_venv() -> None:
  print(f"  SYNC venv to match {REQUIREMENTS_TXT.name}")
  _run(
    [str(VENV / "bin" / "pip-sync"), REQUIREMENTS_TXT.name],
    cwd=str(STUDENT_DIR),
  )


def _register_jupyter_kernel() -> None:
  _run(
    [
      str(VENV_PYTHON), "-m", "ipykernel", "install",
      "--user", "--name", KERNEL_NAME,
      "--display-name", KERNEL_DISPLAY_NAME,
    ]
  )
  print(f"  OK   Jupyter kernel registered: {KERNEL_DISPLAY_NAME!r}")


def _configure_git_hooks() -> None:
  _run(
    ["git", "config", "core.hooksPath", ".githooks"],
    cwd=str(REPO_ROOT),
  )
  print("  OK   git hooksPath set to .githooks")


def main() -> None:
  _create_venv()
  _install_pip_tools()
  _compile_requirements()
  _sync_venv()
  _register_jupyter_kernel()
  _configure_git_hooks()
  print(
    "\nEnvironment ready. Activate with:\n"
    f"  source {VENV}/bin/activate\n"
    "Validate with: python3 miscellaneous/setup/student/"
    "preflight_check.py"
  )


if __name__ == "__main__":
  sys.exit(main())
