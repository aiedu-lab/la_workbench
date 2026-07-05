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
REPORT_DIR = REPO_ROOT / "miscellaneous" / "reporting"
STUDENT_DIR = REPORT_DIR / "for_each_student"
README_PATH = REPO_ROOT / "README.md"

# Matches an Agenda row: `| # | [**Title**](sessions/slug.md) | Why |`
AGENDA_ROW_RE = re.compile(
  r"^\|\s*[\d–]+\s*\|\s*\[\*\*(?P<title>[^\]]+)\*\*\]"
  r"\(sessions/(?P<slug>[\w-]+)\.md\)\s*\|\s*(?P<why>[^|]+)\|"
)

CONTRIBUTORS_HEADING_RE = re.compile(r"^##\s*Contributors\s*$", re.I)
SOLUTION_TITLE_RE = re.compile(r"^#\s*Solution:\s*(?P<title>.+)$")


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


def parse_solution_title(solution_md: Path, default: str) -> str:
  """Return a solution.md's exercise title from its leading
  `# Solution: <Title>` heading, falling back to `default` (the
  session's topic title) if the heading is missing."""
  for line in solution_md.read_text().splitlines():
    match = SOLUTION_TITLE_RE.match(line.strip())
    if match:
      return match.group("title").strip()
  return default


def collect_completions(
  topics: dict[str, tuple[str, str]],
) -> dict[str, dict[str, set[str]]]:
  """Map project slug -> exercise title -> contributor userids.

  Each `solution.md` found anywhere under a project slug names its
  own exercise via its `# Solution: <Title>` heading, so a session
  with multiple distinct exercises (e.g. solving the same problem
  two different ways) credits and reports each one separately
  instead of collapsing them into one topic-level checkmark.
  """
  completions: dict[str, dict[str, set[str]]] = {
    slug: {} for slug in topics
  }
  for slug, (title, _why) in topics.items():
    for solution_md in (PROJECTS_DIR / slug).rglob("solution.md"):
      exercise = parse_solution_title(solution_md, title)
      completions[slug].setdefault(exercise, set()).update(
        parse_contributors(solution_md)
      )
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
  completions: dict[str, dict[str, set[str]]],
) -> None:
  """Write the class-wide topic/exercise x student completion
  matrix, one row per exercise so multiple exercises within a
  session are credited separately."""
  userids = sorted(
    {u for exercises in completions.values()
     for users in exercises.values() for u in users}
  )
  columns = ["Topic", "Exercise"] + userids
  lines = [
    "# Class Completion Report",
    "",
    "| " + " | ".join(columns) + " |",
    "| " + " | ".join(["---"] * len(columns)) + " |",
  ]
  for slug, (title, _why) in topics.items():
    link = f"[{title}](../../sessions/{slug}.md)"
    exercises = completions[slug]
    if not exercises:
      cells = [link, ""] + ["" for _ in userids]
      lines.append("| " + " | ".join(cells) + " |")
      continue
    for exercise in sorted(exercises):
      contributors = exercises[exercise]
      cells = [link, exercise]
      cells += ["✅" if u in contributors else "" for u in userids]
      lines.append("| " + " | ".join(cells) + " |")
  REPORT_DIR.mkdir(parents=True, exist_ok=True)
  (REPORT_DIR / "summary_report.md").write_text("\n".join(lines) + "\n")


def student_table(
  topics: dict[str, tuple[str, str]],
  completions: dict[str, dict[str, set[str]]],
  userid: str,
) -> str:
  """Build the Topic/Exercise/Concept/Completed table body for one
  student, one row per exercise."""
  lines = [
    "| Topic | Exercise | Concept | Completed |",
    "| --- | --- | --- | --- |",
  ]
  for slug, (title, why) in topics.items():
    link = f"[{title}](../../../sessions/{slug}.md)"
    exercises = completions[slug]
    if not exercises:
      lines.append(f"| {link} |  | {why} |  |")
      continue
    for exercise in sorted(exercises):
      mark = "✅" if userid in exercises[exercise] else ""
      lines.append(f"| {link} | {exercise} | {why} | {mark} |")
  return "\n".join(lines)


DATE_LINE_RE = re.compile(r"^\*\*Date Last Updated:\*\* .*$", re.M)
DATE_PLACEHOLDER = "**Date Last Updated:** __PLACEHOLDER__"


def write_student_reports(
  topics: dict[str, tuple[str, str]],
  completions: dict[str, dict[str, set[str]]],
) -> None:
  """Write/update each contributor's per-student report.

  Only rewrites (and bumps the date) when the report's content
  actually changed, comparing with the date line normalized out, so
  unrelated re-runs stay idempotent.
  """
  userids = sorted(
    {u for exercises in completions.values()
     for users in exercises.values() for u in users}
  )
  STUDENT_DIR.mkdir(parents=True, exist_ok=True)
  for userid in userids:
    full_name = resolve_full_name(userid)
    table = student_table(topics, completions, userid)
    body = (
      f"# {full_name} — Completion Report\n\n"
      f"**Full Name:** {full_name}\n"
      f"**GitHub-UserId:** {userid}\n"
      f"{DATE_PLACEHOLDER}\n\n"
      f"{table}\n"
    )
    path = STUDENT_DIR / f"{userid}-report.md"
    if path.is_file():
      existing = DATE_LINE_RE.sub(DATE_PLACEHOLDER, path.read_text())
      if existing == body:
        continue
    today = datetime.date.today().isoformat()
    date_line = f"**Date Last Updated:** {today}"
    path.write_text(body.replace(DATE_PLACEHOLDER, date_line))


def main() -> None:
  topics = parse_agenda()
  completions = collect_completions(topics)
  write_class_report(topics, completions)
  write_student_reports(topics, completions)


if __name__ == "__main__":
  main()
