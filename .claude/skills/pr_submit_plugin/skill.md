---
name: pr_submit_plugin
description: >
  Runs a 3-step gated chain that validates the current branch is
  clean and pushed, then submits a pull request -- confirming with a
  final check that it was actually created. This repo has no bazel
  setup, so unlike the coding repos (ITDev, aim, personal) there is
  no build/test/act step here. Use only when explicitly asked to
  submit or open a pull request. Never invoke automatically -- PR
  submission is always a manual, explicit decision (see CLAUDE.md's
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

**This repo has no bazel setup and no build/test to validate**, so
this plugin is deliberately a 3-step chain (branch/tree hook ->
submit -> confirm hook), omitting the build/test and `act`/PR-check
steps that the coding repos' 7-step chain has.

## Configuration (Bundled)
- **Script:** `skills/pr_submit_plugin/scripts/pr_submit_plugin.py`
  (symlink → `tools/scripts/repo_utils/pr_submit_plugin.py`)

Runs directly via `python3` (stdlib only, no third-party deps) --
this repo's `.venv` is unrelated to these scripts and has no bazel
setup either way.

## Execution Steps

The script implements all three steps internally; invoking it runs
the full chain in one command:

1. **Hook** — validates the current branch is not `main`, the
   working tree is clean, and the local branch tip matches its
   pushed `origin/<branch>` tip (fetches first).
2. **Skill** — runs `submit_pr.py --title ... --body ...` (pushes and
   opens the PR), capturing the resulting PR number from its output.
3. **Hook** — runs `gh pr view <PR#>` to confirm the PR actually
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
- Always resolve paths relative to the repo root.
