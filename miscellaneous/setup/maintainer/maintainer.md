# Maintainer Guide

Everything a repo **maintainer** should know, starting with
reviewing and merging pull requests via `gh`. Any collaborator with
`maintain` permission or above is a maintainer under this repo's
branch-protection settings (see [admin.md](../admin/admin.md)) — no
`admin` permission required.

---

## Section 1 — Validate your maintainer role

```bash
gh auth status
gh api repos/aiedu-lab/la_workbench --jq '.permissions.maintain'
```

Expected: `gh auth status` shows you logged in, and the second
command prints `true`.

---

## Section 2 — List and view open PRs

```bash
gh pr list --repo aiedu-lab/la_workbench
```

```bash
gh pr view <number> --repo aiedu-lab/la_workbench
```

Add `--web` to either command to open the same view in a browser.

---

## Section 3 — Approve a PR

```bash
gh pr review <number> --approve \
  --repo aiedu-lab/la_workbench \
  --body "Looks good."
```

Then merge it (squash keeps history linear, matching this repo's
branch-protection setting):

```bash
gh pr merge <number> --squash --delete-branch \
  --repo aiedu-lab/la_workbench
```

---

## Section 4 — Reject a PR (request changes)

```bash
gh pr review <number> --request-changes \
  --repo aiedu-lab/la_workbench \
  --body "Explain what needs to change before this can merge."
```

This does not close the PR — the author pushes fixes to the same
branch and the PR updates in place.

---

## Section 5 — Amend a PR's metadata

Retarget the base branch, rename it, or relabel it without touching
its commits:

```bash
gh pr edit <number> --repo aiedu-lab/la_workbench \
  --title "New title" \
  --base main
```

---

## Section 6 — Close a PR without merging

For a submission that should not be merged at all (duplicate,
withdrawn, out of scope):

```bash
gh pr close <number> --repo aiedu-lab/la_workbench \
  --comment "Closing because ..."
```

---

## Validation

```bash
gh pr list --repo aiedu-lab/la_workbench --state all --limit 5
```

Expected: the PR you just approved/rejected/closed shows the
matching state (`MERGED`, `OPEN` with your review, or `CLOSED`).
