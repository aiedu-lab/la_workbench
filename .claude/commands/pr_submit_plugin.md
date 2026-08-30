# PR Submit Plugin

Slash-command entry point for the `pr_submit_plugin` gated chain
(see `.claude/skills/pr_submit_plugin/skill.md` for the full
7-step chain this triggers). Thin by design: it adds only the
title/body-drafting step below, then hands off to the existing,
unchanged `pr_submit_plugin.py`.

## Invocation

```
/pr_submit_plugin [extra guidance on emphasis or scope]
```

## What this does

1. **Gather context.** Inspect what is actually in the PR, not just
   the latest commit:
   - `git branch --show-current` and its upstream (`@{u}`)
   - `git log <base>..HEAD --oneline` — every commit being submitted
   - `git diff <base>...HEAD --stat` — every file touched
   Treat `$ARGUMENTS`, if given, as extra guidance on what to
   emphasize -- never as a substitute for reading the actual
   log/diff.

2. **Draft a title and body.**
   - Title: one conventional-commit-style line (`feat:` / `fix:` /
     `docs:` / `refactor:` / `chore:` / ...) summarizing the
     branch's *net effect*, not a recap of the last commit.
   - Body: a `## Summary` bullet list explaining *why*, then a
     `## Test plan` bullet list of what was actually run (bazel
     targets, manual checks) and its outcome.

3. **Confirm before acting.** Show the drafted title/body to the
   user before running anything -- this pushes the branch (if not
   already pushed) and opens a real, visible PR. Proceed only once
   the user confirms or supplies edits.

4. **Invoke the chain:**
   ```
   .venv/bin/python3 tools/scripts/repo_utils/pr_submit_plugin.py \
       --title "<drafted title>" --body "<drafted body>"
   ```
   This runs the full 7-step gated chain (branch/tree hook →
   build+test+container-tests → `//:pr_check` (act) → `//:submit_pr`
   → confirm-exists hook). If any step fails, the chain halts with
   no PR created -- report the failure verbatim; never retry
   silently or attempt to route around a failed gate.

## Constraints

- Never invoke automatically -- PR submission is always an
  explicit, human-invoked action (see AGENTS.md's git safety
  protocol and `pr_submit_plugin.py`'s own docstring).
- Never fabricate the title/body and submit without showing them to
  the user first.
- This file is the slash-command entry point only. The actual gated
  chain lives in `.claude/skills/pr_submit_plugin/` and
  `tools/scripts/repo_utils/pr_submit_plugin.py`, unmodified by
  this wrapper.

Sync note: this file is intentionally duplicated (not symlinked)
across every sister repo -- ITDev, aim, personal, ai_workbench,
la_workbench. Any change here must be ported to the same path in
every other repo. Spot-check with:
  diff .claude/commands/pr_submit_plugin.md \
      ../<other-repo>/.claude/commands/pr_submit_plugin.md
