#!/usr/bin/env python3
"""Validate the LA Workbench student lab environment.

Checks for:
- `.venv` exists at the repo root with a working python3
- requirements.txt exists and is in sync with requirements.in
- numpy, torch, matplotlib, jupyter, ipykernel importable in the venv
- the `la-workbench` Jupyter kernel is registered

Prints PASS or FAIL per item. Always runs all checks.
"""
import subprocess
import sys
from pathlib import Path

STUDENT_DIR = Path(__file__).resolve().parent
REPO_ROOT = STUDENT_DIR.parent.parent.parent
VENV = REPO_ROOT / ".venv"
VENV_PYTHON = VENV / "bin" / "python3"
REQUIREMENTS_IN = STUDENT_DIR / "requirements.in"
REQUIREMENTS_TXT = STUDENT_DIR / "requirements.txt"
KERNEL_NAME = "la-workbench"

REQUIRED_PACKAGES = ("numpy", "torch", "matplotlib", "jupyter", "ipykernel")


def check(label: str, fn) -> None:
  try:
    fn()
    print(f"PASS  {label}")
  except Exception as e:
    print(f"FAIL  {label} — {e}")


def check_venv_exists() -> None:
  if not VENV_PYTHON.exists():
    raise RuntimeError(
      f"{VENV} not found — run "
      "miscellaneous/setup/student/labsetup.py"
    )


def check_requirements_compiled() -> None:
  if not REQUIREMENTS_TXT.exists():
    raise RuntimeError(
      f"{REQUIREMENTS_TXT} not found — run labsetup.py"
    )
  if REQUIREMENTS_IN.stat().st_mtime > REQUIREMENTS_TXT.stat().st_mtime:
    raise RuntimeError(
      "requirements.in is newer than requirements.txt — "
      "re-run labsetup.py to recompile"
    )


def check_package(name: str) -> None:
  result = subprocess.run(
    [str(VENV_PYTHON), "-c", f"import {name}"],
    capture_output=True,
  )
  if result.returncode != 0:
    raise RuntimeError(
      f"{name} not importable in .venv — run labsetup.py"
    )


def check_jupyter_kernel() -> None:
  result = subprocess.run(
    [str(VENV_PYTHON), "-m", "jupyter", "kernelspec", "list"],
    capture_output=True, text=True,
  )
  if result.returncode != 0 or KERNEL_NAME not in result.stdout:
    raise RuntimeError(
      f"Jupyter kernel {KERNEL_NAME!r} not registered — "
      "run labsetup.py"
    )


def main() -> None:
  print("=== Preflight Check ===\n")
  check(".venv exists", check_venv_exists)
  check("requirements.txt up to date", check_requirements_compiled)
  for pkg in REQUIRED_PACKAGES:
    check(f"{pkg} importable", lambda p=pkg: check_package(p))
  check(f"Jupyter kernel {KERNEL_NAME!r} registered", check_jupyter_kernel)
  print("\nAll items must show PASS before the lab begins.")


if __name__ == "__main__":
  main()
