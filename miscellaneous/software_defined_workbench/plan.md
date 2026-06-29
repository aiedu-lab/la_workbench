# Software Driven Specification Plan for creation of LA Workbench

TL;DR
This document captures the specification plan used to craft the course
content delivered by a math, ai, or cs educator. It builds a hands-on 
Linear Algebra (LA) lab for high schoolers and freshman undergraduates, 
teaching them the basics of Linear Algebra as a practitioner.

---

## Phase 1: Repo Bootstrap & Contextualization

### Step 1.1: Contextualize CLAUDE.md/AGENTS.md for LA Workbench

[x] Status

CONTEXT: `CLAUDE.md` (symlinked as `AGENTS.md`) still carries the AI Workbench `PROJECT OVERVIEW` and `PROJECT-SPECIFIC NOTES` sections; the rest of the file (Plan Update Protocol, behavioral invariants, style rules) is repo-agnostic and correct as-is.
ACTION: Edit `CLAUDE.md`'s `PROJECT OVERVIEW` section to describe the Linear Algebra Workbench instead of AI Workbench, and its `PROJECT-SPECIFIC NOTES` section to drop AI-Workbench-only references (e.g. Group Meetup Organizer) in favor of LA Workbench's own session/project naming.
CONSTRAINTS: Do not touch the Plan Update Protocol, Behavioral Invariants, Documentation, Style & Hygiene, or Session Rehydration sections.
OUTPUT: Updated `CLAUDE.md` with an LA-Workbench-specific overview; `AGENTS.md` symlink unchanged.
VERIFY: `grep -i "meetup\|Group Meetup Organizer" CLAUDE.md` → 0 matches.

### Step 1.2: Contextualize instructor.md — keep Discord, drop meetup-organizer content

[x] Status

CONTEXT: `miscellaneous/setup/instructor/instructor.md` was copied verbatim from the sister repo; its Discord and smoke-test sections are built around the Group Meetup Organizer webhook/notifier pipeline, which has no LA Workbench equivalent, but the class still wants a Discord channel for general discussion/coordination.
ACTION: Rewrite the Discord section to set up a general class discussion/coordination channel (drop webhook/`DISCORD_WEBHOOK_URL` automation and the meetup-notification validation script, keep create-server/create-channel/invite/confirm-join steps); remove the meetup-pipeline smoke-test section entirely; renumber remaining sections; update closing Teaching-Philosophy text to reference Linear Algebra instead of Group Meetup Organizer.
CONSTRAINTS: Keep the roster and laptop-preflight sections and the simplified Discord section intact; do not add new Discord automation beyond manual server/channel/invite setup.
OUTPUT: Updated `instructor.md` with Discord retained in simplified form and meetup-organizer-specific content removed.
VERIFY: `grep -i "meetup\|DISCORD_WEBHOOK_URL" miscellaneous/setup/instructor/instructor.md` → 0 matches; `grep -ic "discord" miscellaneous/setup/instructor/instructor.md` → greater than 0.

### Step 1.3: Author repo hygiene doc

[x] Status

CONTEXT: No `miscellaneous/setup/instructor/repo.md` exists yet; the prompt requires documented GitHub settings enforcing "no commits to main, all changes via branch + PR," matching the sister repo's norms already reflected in `.github/CODEOWNERS`.
ACTION: Create `miscellaneous/setup/instructor/repo.md` with step-by-step GitHub UI/CLI instructions to enable branch protection on `main` (require PR, require CODEOWNERS review, disallow direct pushes/force-push), and confirm `.github/CODEOWNERS` and `.github/workflows/claude-review.yml` are active.
CONSTRAINTS: Do not modify `.github/CODEOWNERS` or `.github/workflows/claude-review.yml` — document existing settings only.
OUTPUT: New file `miscellaneous/setup/instructor/repo.md`.
VERIFY: `test -f miscellaneous/setup/instructor/repo.md && echo OK` → `OK`.

### Step 1.4: Update README.md agenda with session cross-links

[ ] Status

CONTEXT: `README.md` has a flat 17-topic Agenda table with no links to `sessions/` or `projects/` files, and no Introduction / Dev Workbench Setup rows, unlike the sister repo's README style.
ACTION: Add an Introduction row and a Development Workbench Setup row to the Agenda table, and convert each of the 17 existing topic names into links of the form `[Topic](sessions/<slug>.md)`, where `<slug>` matches the placeholder filenames created in Step 1.6.
CONSTRAINTS: Do not change the Prerequisites, Teaching Philosophy, or Learning Outcome sections.
OUTPUT: Updated `README.md` Agenda table with working relative links.
VERIFY: `grep -c "](sessions/" README.md` → 19.

### Step 1.5: Create student setup toolchain

[ ] Status

CONTEXT: `miscellaneous/setup/student/` does not exist yet; the prompt asks for `labsetup.py` and `preflight_check.py` (NumPy, PyTorch, Jupyter, common tools) using a `.venv` at repo root with `requirements.in`/`requirements.txt` — narrower scope than the sister repo's meetup-specific `poller.py`/`selector.py`/`notifier.py`.
ACTION: Create `miscellaneous/setup/student/requirements.in` (numpy, torch, jupyter, matplotlib), compile it to `requirements.txt`, and create `labsetup.py` (creates `.venv` at repo root, installs from `requirements.txt`) and `preflight_check.py` (verifies Python version, `.venv` active, and each package importable).
CONSTRAINTS: Do not create `poller.py`, `selector.py`, `notifier.py`, `config.yaml`, or `labenv.yaml` — meetup-organizer-specific and out of scope.
OUTPUT: Four new files under `miscellaneous/setup/student/`.
VERIFY: `python3 miscellaneous/setup/student/preflight_check.py` → all checks `PASS` after `labsetup.py` has been run once.

### Step 1.6: Create placeholder sessions and matching project dirs

[ ] Status

CONTEXT: `sessions/` and `projects/` are both empty; the README Agenda (Step 1.4) lists 17 LA topics plus Introduction and Dev Workbench Setup, each needing a session placeholder, with hands-on exercises also needing a matching `projects/<slug>/` directory.
ACTION: Create one placeholder file per agenda row in `sessions/` (one-line title plus a `<!-- TODO: content -->` marker), and matching empty `projects/<slug>/` directories with a placeholder `README.md` only for hands-on exercise rows.
CONSTRAINTS: Placeholders only, no actual lesson content; do not rename or reorder the 17 agenda rows from Step 1.4.
OUTPUT: 19 new files under `sessions/`; one `projects/<slug>/` per exercise row.
VERIFY: `ls sessions/*.md | wc -l` → `19`.

### Step 1.8: Cross-link la_workbench and ai_workbench READMEs

[ ] Status

CONTEXT: Neither `README.md` currently mentions the other repo; `la_workbench` is independent of `ai_workbench` but a companion curriculum — LA fundamentals help students grok the AI Workbench exercises, and LA mechanics are the engine under those exercises.
ACTION: Add a "Companion Repository" callout to `la_workbench/README.md` (after Objective) linking to `ai_workbench`, and a symmetric callout to `../ai_workbench/README.md` (after its Objective) linking back to `la_workbench`.
CONSTRAINTS: This step touches `../ai_workbench/README.md`, a separate git repository with its own history/remote — get explicit confirmation before committing/pushing there. Do not alter either README's Agenda table or other sections.
OUTPUT: Two updated `README.md` files, one per repo, each referencing the other by name and GitHub URL.
VERIFY: `grep -i "ai_workbench" README.md` (la_workbench) → match; `grep -i "la_workbench" ../ai_workbench/README.md` → match.

### Step 1.9: Mark Phase 1 complete

[ ] Status

CONTEXT: Steps 1.1–1.8 are committed and verified individually.
ACTION: Flip every `[ ] Status` → `[x] Status` in the Phase 1 block of this file.
CONSTRAINTS: Do not modify step content, only status lines.
OUTPUT: All Phase 1 steps show `[x] Status`.
VERIFY: `grep -A1 "### Step 1\." miscellaneous/software_defined_workbench/plan.md | grep "\[ \] Status"` → 0 matches. Commit all changed files and tag `v1.9-bootstrap-contextualization-step-completed`.

---
