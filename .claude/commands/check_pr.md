# Check PR

Slash-command entry point for `check_pr.py` -- a read-only report
of one PR's state/checks/review-decision. Exits 0 only if the PR
looks mergeable right now. Never mutates the PR, safe to run any
time.

## Invocation

```
/check_pr <PR#>
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
  diff .claude/commands/check_pr.md \
      ../<other-repo>/.claude/commands/check_pr.md
