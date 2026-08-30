# PR Approve Plugin

Slash-command entry point for `approve_pr.py` -- posts a real
approval review to a real PR via `gh pr review --approve`.

**Relevance:** only to someone holding MAINTAIN or ADMIN permission
on the repo (`approve_pr.py`'s own `MIN_PERMISSION` gate) -- a plain
WRITE contributor's invocation fails the permission preflight before
`gh` is ever called. It also fails if the invoker is the PR's own
author: GitHub rejects self-approval unconditionally, for every
permission level, with no repo/org setting that overrides it (see
`approve_pr.py`'s own docstring for the exact detection and the
next-step guidance it prints in that case).

## Invocation

```
/pr_approve_plugin <PR#> [review body]
```

## What this does

Invokes:
```
bazel run //:approve_pr -- <PR#> [--body "<review body>"]
```

No gating chain is needed here, unlike submit/merge:
`approve_pr.py` already performs its own auth/permission preflight
and PR-state check before calling `gh`, so this wrapper only parses
`$ARGUMENTS` into a PR number and an optional review body.

## Constraints

- Never invoke automatically -- approving a PR is always an
  explicit, human-invoked action (see AGENTS.md's git safety
  protocol and `approve_pr.py`'s own docstring).
- Never calls `merge_pr.py` -- approving and merging are always
  separate operations, even when the same person is permitted to do
  both.

Sync note: this file is intentionally duplicated (not symlinked)
across every sister repo -- ITDev, aim, personal, ai_workbench,
la_workbench. Any change here must be ported to the same path in
every other repo. Spot-check with:
  diff .claude/commands/pr_approve_plugin.md \
      ../<other-repo>/.claude/commands/pr_approve_plugin.md
