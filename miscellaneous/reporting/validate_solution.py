#!/usr/bin/env python3
"""Reject solution.md files missing the fields the completion
report depends on: a `# Solution: <Title>` heading and a non-empty,
placeholder-free `## Contributors` section."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_reports import (  # noqa: E402
  PROJECTS_DIR,
  SOLUTION_TITLE_RE,
  parse_contributors,
)


def validate(solution_md: Path) -> list[str]:
  """Return error strings for one solution.md (empty if valid)."""
  errors = []
  lines = solution_md.read_text().splitlines()
  if not any(SOLUTION_TITLE_RE.match(line.strip()) for line in lines):
    errors.append("missing a '# Solution: <Title>' heading")
  contributors = parse_contributors(solution_md)
  if not contributors:
    errors.append("'## Contributors' section is missing or empty")
  elif any("<" in u or ">" in u for u in contributors):
    errors.append(
      "'## Contributors' still has placeholder text ('<' or '>')"
    )
  return errors


def main() -> int:
  paths = [Path(p) for p in sys.argv[1:]] or sorted(
    PROJECTS_DIR.rglob("solution.md")
  )
  failed = False
  for path in paths:
    for error in validate(path):
      print(f"{path}: {error}", file=sys.stderr)
      failed = True
  return 1 if failed else 0


if __name__ == "__main__":
  sys.exit(main())
