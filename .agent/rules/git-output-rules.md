---
description: Disable paging tools and external diff tools for git commands
---
# Git Output Rules

To ensure command output is rendered cleanly in terminal history and easily captured by agents without manual scrolling or unintended formatting, you MUST ALWAYS disable external pagers and external diff tools.

## The Rule

1. **No Pager**: Whenever executing a `git diff` or `git log` command, you MUST disable the pager. Use the `--no-pager` git flag or prefix the command with `PAGER=cat`.
2. **No External Diff**: Whenever executing a `git diff` command, you MUST NOT use external diff tools. Use the `--no-ext-diff` flag.

## Examples

✅ **Good**:

```bash
PAGER=cat git diff --no-ext-diff
git --no-pager diff --no-ext-diff HEAD^ HEAD
git --no-pager log -n 5
```

❌ **Bad**:

```bash
git diff
git log
git diff --ext-diff
```
