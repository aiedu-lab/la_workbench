# Line Length (79 Characters Maximum)

**Rule**: Keep all lines to a maximum of 79 characters.
This applies to code, comments, and documentation.

**Critical**: Maximize the use of available space up to the
79-character limit. Do NOT break lines prematurely when space
remains. Fit as many words as possible before wrapping. Only
break to a new line when adding another word would exceed 79.

**Always check**: Can one more word fit? If yes, add it.

**Indentation**: 2 spaces (no hard tabs). Count each space as
1 character towards the 79-char limit.

## Examples

✅ **Good** — wraps only when necessary:
```python
# This comment uses the full 79 characters available on each
# line before wrapping to the next line for continuation.
def organize_files(
  source_dir: Path,
  dry_run: bool,
  verbose: bool,
) -> None:
```

❌ **Bad** — breaks prematurely with space remaining:
```python
# This comment breaks
# prematurely even though
# space is available.
def organize_files(source_dir: Path, dry_run: bool) -> None:
```

## Enforcement

Run before every commit on staged files:

```bash
git diff --name-only HEAD \
  | grep -E '\.(md|py|yaml|yml|sh)$' \
  | xargs awk 'length>79 {
      print FILENAME ":" NR ": " length " chars"
    }' \
  | grep . && echo "FAIL: lines exceed 79 chars" || echo "PASS"
```

## Exemptions

Long strings and URLs are exempt if wrapping would break them.
