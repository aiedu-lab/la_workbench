#!/usr/bin/env python3
"""Regenerate class-wide and per-student exercise completion reports."""

import datetime
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PROJECTS_DIR = REPO_ROOT / "projects"
REPORT_DIR = REPO_ROOT / "miscellaneous" / "report"
STUDENT_DIR = REPORT_DIR / "student"
README_PATH = REPO_ROOT / "README.md"

# Matches an Agenda row: `| # | [**Title**](sessions/slug.md) | Why |`
AGENDA_ROW_RE = re.compile(
  r"^\|\s*[\d–]+\s*\|\s*\[\*\*(?P<title>[^\]]+)\*\*\]"
  r"\(sessions/(?P<slug>[\w-]+)\.md\)\s*\|\s*(?P<why>[^|]+)\|"
)

CONTRIBUTORS_HEADING_RE = re.compile(r"^##\s*Contributors\s*$", re.I)


def parse_agenda() -> dict[str, tuple[str, str]]:
  """Map project slug -> (topic title, short concept description).

  Sourced from README.md's Agenda table so the topic/description
  text stays single-sourced instead of duplicated here.
  """
  topics: dict[str, tuple[str, str]] = {}
  for line in README_PATH.read_text().splitlines():
    match = AGENDA_ROW_RE.match(line)
    if not match:
      continue
    slug = match.group("slug")
    if not (PROJECTS_DIR / slug).is_dir():
      continue
    topics[slug] = (match.group("title").strip(), match.group("why").strip())
  return topics


def parse_contributors(solution_md: Path) -> list[str]:
  """Return the bare GitHub-UserIds in a solution.md's Contributors
  section."""
  userids: list[str] = []
  in_section = False
  for line in solution_md.read_text().splitlines():
    if CONTRIBUTORS_HEADING_RE.match(line.strip()):
      in_section = True
      continue
    if not in_section:
      continue
    if line.strip().startswith("#"):
      break
    userid = line.strip().lstrip("*-").strip()
    if userid:
      userids.append(userid)
  return userids


def collect_completions(
  topics: dict[str, tuple[str, str]],
) -> dict[str, set[str]]:
  """Map project slug -> set of contributor userids with a solution."""
  completions: dict[str, set[str]] = {slug: set() for slug in topics}
  for slug in topics:
    for child in (PROJECTS_DIR / slug).iterdir():
      solution_md = child / "solution.md"
      if child.is_dir() and solution_md.is_file():
        completions[slug].update(parse_contributors(solution_md))
  return completions


_NAME_CACHE: dict[str, str] = {}


def resolve_full_name(userid: str) -> str:
  """Look up a GitHub-UserId's display name via the public Users API.

  Falls back to the raw userid when the API is unreachable or the
  account has no display name set, so report generation never
  hard-fails on a network hiccup.
  """
  if userid in _NAME_CACHE:
    return _NAME_CACHE[userid]
  name = userid
  request = urllib.request.Request(
    f"https://api.github.com/users/{userid}",
    headers={"User-Agent": "la-workbench-report"},
  )
  try:
    with urllib.request.urlopen(request, timeout=10) as response:
      name = json.load(response).get("name") or userid
  except (urllib.error.URLError, TimeoutError, ValueError):
    pass
  _NAME_CACHE[userid] = name
  return name


def write_class_report(
  topics: dict[str, tuple[str, str]],
  completions: dict[str, set[str]],
) -> None:
  """Write the class-wide topic x student completion matrix."""
  userids = sorted({u for users in completions.values() for u in users})
  columns = ["Topic"] + userids
  lines = [
    "# Class Completion Report",
    "",
    "| " + " | ".join(columns) + " |",
    "| " + " | ".join(["---"] * len(columns)) + " |",
  ]
  for slug, (title, _why) in topics.items():
    cells = [f"[{title}](../../sessions/{slug}.md)"]
    cells += ["✅" if u in completions[slug] else "" for u in userids]
    lines.append("| " + " | ".join(cells) + " |")
  REPORT_DIR.mkdir(parents=True, exist_ok=True)
  (REPORT_DIR / "report.md").write_text("\n".join(lines) + "\n")


def student_table(
  topics: dict[str, tuple[str, str]],
  completions: dict[str, set[str]],
  userid: str,
) -> str:
  """Build the Topic/Concept/Completed table body for one student."""
  lines = ["| Topic | Concept | Completed |", "| --- | --- | --- |"]
  for slug, (title, why) in topics.items():
    mark = "✅" if userid in completions[slug] else ""
    lines.append(
      f"| [{title}](../../../sessions/{slug}.md) | {why} | {mark} |"
    )
  return "\n".join(lines)


def write_student_reports(
  topics: dict[str, tuple[str, str]],
  completions: dict[str, set[str]],
) -> None:
  """Write/update each contributor's per-student report.

  Only rewrites (and bumps the date) when the student's completion
  table actually changed, so unrelated re-runs stay idempotent.
  """
  userids = sorted({u for users in completions.values() for u in users})
  STUDENT_DIR.mkdir(parents=True, exist_ok=True)
  for userid in userids:
    table = student_table(topics, completions, userid)
    path = STUDENT_DIR / f"{userid}-report.md"
    if path.is_file():
      existing_table = path.read_text().split("\n\n", 2)[-1].strip()
      if existing_table == table.strip():
        continue
    full_name = resolve_full_name(userid)
    today = datetime.date.today().isoformat()
    content = (
      f"# {full_name} — Completion Report\n\n"
      f"**GitHub-UserId:** {userid}\n"
      f"**Date Last Updated:** {today}\n\n"
      f"{table}\n"
    )
    path.write_text(content)


def main() -> None:
  topics = parse_agenda()
  completions = collect_completions(topics)
  write_class_report(topics, completions)
  write_student_reports(topics, completions)


if __name__ == "__main__":
  main()
