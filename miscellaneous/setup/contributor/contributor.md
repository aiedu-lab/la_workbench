# Contributor Guide

One-time reference for the `gh` commands behind exercise-solution
submission — see [Submitting Exercise Solutions](
  ../../../README.md#-submitting-exercise-solutions
) for the full step-by-step. Any GitHub collaborator with at least
`write` (push) access is a contributor — no `admin`/`maintain`
permission required.

---

## Section 1 — Validate your contributor role

```bash
gh auth status
gh api repos/aiedu-lab/la_workbench --jq '.permissions.push'
```

Expected: `gh auth status` shows you logged in, and the second
command prints `true` — this repo's submission workflow pushes a
branch directly (no fork), so `write` access is required.

---

## Section 2 — Submit a pull request

After pushing your solutions branch (README step 4):

```bash
gh pr create \
  --repo aiedu-lab/la_workbench \
  --title "projects/<project-name>/solutions/<github-userid>" \
  --body "Solution for <project-name>." \
  --base main
```

Validation:

```bash
gh pr view --repo aiedu-lab/la_workbench --web
```

Expected: your PR opens in the browser, targeting `main`.
