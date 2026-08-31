# Check PRs

Slash-command entry point for a read-only summary of every open PR
in this repo. Unlike `/check_pr`, which reports on one PR by
number, this lists all of them at once with a compact status for
each. No underlying script -- trivial enough to run directly via
`gh`.

## Invocation

```
/check_prs
```

## What this does

1. List every open PR in one call:
   ```
   gh pr list --json number,title,author,url,isDraft,reviewDecision,statusCheckRollup
   ```
2. For each PR, tally its `statusCheckRollup` entries into
   passed/pending/failed counts the same way `_pr_utils.py`'s
   `_check_outcome` does: a modern `CheckRun` entry (has `status`)
   is pending unless `status == "COMPLETED"`, then passed only if
   `conclusion` is one of `SUCCESS`/`NEUTRAL`/`SKIPPED`; a legacy
   `StatusContext` entry (`state` only, no `status`) is pending if
   `state == "PENDING"`, else passed only if `state == "SUCCESS"`.
3. Present one row per PR: number, title (truncated to a readable
   width), author, draft marker if `isDraft`, a check tally (e.g.
   `3 passed / 1 pending`), `reviewDecision` (or "none required" if
   empty), and a one-line verdict:
   - all checks passed AND (`reviewDecision` empty or `APPROVED`) →
     **mergeable**
   - any check pending → **blocked: N check(s) pending**
   - any check failed → **blocked: N check(s) failed**
   - `reviewDecision == "REVIEW_REQUIRED"` → **blocked: review
     required** (note if the caller is ADMIN, an admin bypass may
     still apply -- see `/pr_merge`'s own docstring)
   - `reviewDecision == "CHANGES_REQUESTED"` → **blocked: changes
     requested**
4. If there are no open PRs, say so plainly rather than printing an
   empty table.
5. Point at `/check_pr <PR#>` for full detail on any single PR.

## Constraints

- Read-only -- no confirmation needed before running; never mutates
  any PR.

Sync note: this file is intentionally duplicated (not symlinked)
across every sister repo -- ITDev, aim, personal, ai_workbench,
la_workbench. Any change here must be ported to the same path in
every other repo. Spot-check with:
  diff .claude/commands/check_prs.md \
      ../<other-repo>/.claude/commands/check_prs.md
