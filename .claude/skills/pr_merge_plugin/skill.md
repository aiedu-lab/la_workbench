---
name: pr_merge_plugin
description: >
  Runs a 3-step gated chain that waits for a pull request's checks
  to finish, then merges it -- confirming with a final check that it
  actually landed. The merge step already knows how to retry with
  --admin when a review is required but the caller is exempt via
  branch protection. Use only when explicitly asked to merge a pull
  request. Never invoke automatically -- merging is always a
  manual, explicit decision (see AGENTS.md's git safety protocol and
  merge_pr.py's own docstring).
disable-model-invocation: true
triggers:
  - "merge the pull request"
  - "merge the pr"
  - "merge pr"
  - "pr_merge_plugin"
_path: .claude/skills/pr_merge_plugin/skill.md
---

# PR Merge Plugin

## Overview
Chains together the "wait, then merge, then confirm" steps that
would otherwise be run by hand, one command at a time (or via a
manual polling loop), before merging a pull request. Every step is
a hard gate: if any step fails, the chain halts immediately with no
silent continuation, and no merge is attempted while checks are
still pending.

## Configuration (Bundled)
- **Script:** `skills/pr_merge_plugin/scripts/pr_merge_plugin.py`
  (symlink → `tools/scripts/repo_utils/pr_merge_plugin.py`)

Deliberately **not** a bazel target: it shells out to `bazel run`
itself, and a bazel target that re-invokes `bazel` from inside its
own sandbox is a known anti-pattern -- same reasoning as
`pr_submit_plugin`. It runs directly via `.venv/bin/python3`.

## Execution Steps

The script implements all three steps internally; invoking it runs
the full chain in one command:

1. **Hook** — polls the PR's status checks (via the same
   `fetch_pr_status` helper `check_pr`/`approve_pr`/`merge_pr` share)
   until none are pending, halting immediately if any check fails or
   the poll times out. Deliberately does **not** look at the review
   decision at all -- `merge_pr.py` is the sole authority on whether
   an unsatisfied review blocks the merge or is bypassable via
   admin, so re-deciding that here would just duplicate that logic.
2. **Skill** — runs `bazel run //:merge_pr -- <PR#> [--method ...]
   [--delete-branch]`.
3. **Hook** — runs `gh pr view <PR#> --json state` to confirm the PR
   actually shows as `MERGED` before reporting success.

Run it via:
```
.venv/bin/python3 tools/scripts/repo_utils/pr_merge_plugin.py <PR#>
```
Or via the `/pr_merge_plugin` slash command
(`.claude/commands/pr_merge_plugin.md`), a thin argument-parsing
wrapper around this same script.

Optional: `--method {merge,squash,rebase}` (default `merge`),
`--delete-branch`, `--poll-interval <seconds>` (default 15),
`--timeout <seconds>` (default 1800).

## Constraints
- Never calls `approve_pr.py` — GitHub rejects self-approval
  unconditionally regardless of permission level, and an admin
  bypass (when configured) makes approval unnecessary anyway;
  `merge_pr.py` already knows how to attempt that bypass.
- Never wired to a git hook, CI workflow, or any other automatic
  trigger — always a human-invoked command with an explicit PR
  number.
- Always resolve paths relative to the repo root. Never traverse
  `.venv`, `bazel-out/`, or `external/`.

## Cross-Repo Consistency

This skill (this file, and the script it wraps) is intentionally
duplicated -- not symlinked -- across every sister repo: ITDev,
aim, personal, ai_workbench, la_workbench. Any behavioral change
(a new step, a changed flag, a fixed bug) must be ported to the
same path in every other repo, except for narrow, explicitly
commented repo-specific differences (e.g. a STUB build/test step
where a repo has no bazel oci_image targets yet). Spot-check with:
```
diff .claude/skills/<this-skill>/skill.md \
    ../<other-repo>/.claude/skills/<this-skill>/skill.md
```
