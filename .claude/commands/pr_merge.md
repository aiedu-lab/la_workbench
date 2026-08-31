# PR Merge

Slash-command entry point for the `pr_merge_plugin` gated chain
(see `.claude/skills/pr_merge_plugin/skill.md` for the full 3-step
chain this triggers).

**Relevance:** only when the merge is actually allowed to happen.
`merge_pr.py` requires WRITE/MAINTAIN/ADMIN permission, every check
to have finished with none failed, and one of: no review required
(`reviewDecision` empty), the PR already `APPROVED`, or the invoker
is ADMIN and branch protection exempts admins from an unsatisfied
review (retried with `--admin` -- GitHub's own API is the final word
on whether that bypass is actually configured). Any other case --
insufficient permission, a pending/failed check, or
`CHANGES_REQUESTED` -- fails the command outright; it never attempts
a partial or forced merge (see `merge_pr.py`'s own docstring for the
exact decision table).

## Invocation

```
/pr_merge <PR#> [--method squash|rebase] [--delete-branch]
```

## What this does

Invokes:
```
.venv/bin/python3 tools/scripts/repo_utils/pr_merge_plugin.py <PR#> \
    [--method <method>] [--delete-branch]
```

This runs the full 3-step gated chain (wait-for-checks hook →
`//:merge_pr` → confirm-merged hook).

## Constraints

- Never invoke automatically -- merging is always an explicit,
  human-invoked action (see AGENTS.md's git safety protocol and
  `pr_merge_plugin.py`'s own docstring).
- Never calls `approve_pr.py` -- this chain never attempts to
  approve its own PR.

Sync note: this file is intentionally duplicated (not symlinked)
across every sister repo -- ITDev, aim, personal, ai_workbench,
la_workbench. Any change here must be ported to the same path in
every other repo. Spot-check with:
  diff .claude/commands/pr_merge.md \
      ../<other-repo>/.claude/commands/pr_merge.md
