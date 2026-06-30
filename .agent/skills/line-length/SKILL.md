---
name: line-length
description: Ensures all files in a PR will pass the CI line length check.
---

# Fix Failed Line Length Checks

<!-- PREREQUISITE: This skill requires `./tools/check-line-length.sh`
     to exist in the repo. It was designed for Go projects. For this
     repo (Python/Markdown), use .agent/rules/always-line-length.md
     as the authoritative rule and enforce via the command there. -->

Run `./tools/check-line-length.sh` and fix all affected lines
without introducing regressions. If there are no lines reported
and the exit code is 0, you are done.

## Restrictions

CRITICAL: If the line length check returns with exit code 0 and no output, stop execution!
CRITICAL: Do not run any git commands!
CRITICAL: Do not check git status!
CRITICAL: Do not look through git history!
CRITICAL: Only deal with files listed by the line check tool.
CRITICAL: Do not run `ls`.
CRITICAL: Do not read the source of `./tools/check-line-length.sh`

## golang

For Go files, run `gofmt` after the line length edits. Then run the line check again.
If `gofmt` causes lines to be longer than 79 characters again, try the following fixes:

1. Break up declarations into individual statements so they do not get vertically aligned in multiple columns.
2. Use type aliases for long, repeated usages of the same type reference.

Iterate between `gofmt` and `./tools/check-line-length.sh` until all lines are less than 79 characters long.
