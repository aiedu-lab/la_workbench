# PR Check

Slash-command entry point for `check_pr.py` -- a read-only report
of one PR's state/checks/review-decision. Exits 0 only if the PR
looks mergeable right now. Never mutates the PR, safe to run any
time.

**Not to be confused with** `bazel run //:pr_check` (the local
`act`-based CI validator invoked by `/pr_submit` -- an unrelated
target that happens to share half its name). This command wraps
`//:check_pr`, singular-PR-status, a different script entirely.

## Invocation

```
/pr_check <PR#>
```

## What this does

Invokes:
```
bazel run //:check_pr -- <PR#>
```

Trivial by design: `check_pr.py` already does all the work (auth
preflight, PR-status fetch, pass/fail determination) -- this wrapper
only parses `$ARGUMENTS` into a PR number.

## Constraints

- Read-only -- no confirmation needed before running; never mutates
  the PR.

Sync note: this file is intentionally duplicated (not symlinked)
across every sister repo -- ITDev, aim, personal, ai_workbench,
la_workbench. Any change here must be ported to the same path in
every other repo. Spot-check with:
  diff .claude/commands/pr_check.md \
      ../<other-repo>/.claude/commands/pr_check.md
