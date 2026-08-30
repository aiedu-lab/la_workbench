---
name: pr_submit_plugin
description: >
  Runs a 7-step gated chain that validates the current branch is
  clean and pushed, builds and tests it, validates the PR workflow
  locally via act, and only then submits a pull request -- confirming
  with a final check that it was actually created. STUB: the
  build/test step is mocked pending la_workbench's real codebase (no
  container-test targets exist yet). Use only when explicitly asked
  to submit or open a pull request. Never invoke automatically -- PR
  submission is always a manual, explicit decision (see AGENTS.md's
  git safety protocol and submit_pr.py's own docstring).
disable-model-invocation: true
triggers:
  - "submit a pull request"
  - "open a pr"
  - "submit pr"
  - "pr_submit_plugin"
_path: .claude/skills/pr_submit_plugin/skill.md
---

# PR Submit Plugin

## Overview
Chains together the validation and submission steps that would
otherwise be run by hand, one command at a time, before opening a
pull request. Every step is a hard gate: if any step fails, the
chain halts immediately with no silent continuation, and no pull
request is created.

**STUB (mock, pending la_workbench's real codebase):** the
build+test skill step below only runs `bazel build //...` / `bazel
test //...` — no container-test commands, since la_workbench has no
bazel oci_image targets yet. Extend `pr_submit_plugin.py`'s
`skill_build_and_test` once it does.

## Configuration (Bundled)
- **Script:** `skills/pr_submit_plugin/scripts/pr_submit_plugin.py`
  (symlink → `tools/scripts/repo_utils/pr_submit_plugin.py`)

Deliberately **not** a bazel target: it shells out to `bazel
build`/`bazel test`/`bazel run` itself, and a bazel target that
re-invokes `bazel` from inside its own sandbox is a known
anti-pattern (sandbox restrictions, bazel-server lock contention).
It runs directly via `python3` (this repo has no `.venv`).

## Execution Steps

The script implements all seven steps internally; invoking it runs
the full chain in one command:

1. **Hook** — validates the current branch is not `main`, the
   working tree is clean, and the local branch tip matches its
   pushed `origin/<branch>` tip (fetches first).
2. **Skill (stub)** — runs `bazel build //...`, `bazel test //...`.
3. **Hook** — implicit in Step 2: any non-zero exit halts
   immediately.
4. **Skill** — runs `bazel run //:pr_check` (wraps `act` against
   the stub PR-validation workflow).
5. **Hook** — implicit in Step 4: a non-zero exit halts
   immediately.
6. **Skill** — runs `bazel run //:submit_pr -- --title ... --body
   ...` (pushes and opens the PR), capturing the resulting PR
   number from its output.
7. **Hook** — runs `gh pr view <PR#>` to confirm the PR actually
   exists before reporting success.

Run it via:
```
python3 skills/pr_submit_plugin/scripts/pr_submit_plugin.py \
  --title "<title>" --body "<body>"
```

Optional: `--base <branch>` (default `main`), `--draft`.

## Constraints
- Never calls `approve_pr.py` — submitting and approving a PR are
  always separate operations performed by different people.
- Never wired to a git hook, CI workflow, or any other automatic
  trigger — always a human-invoked command with explicit arguments.
- Always resolve paths relative to the repo root. Never traverse
  `bazel-out/` or `external/`.
