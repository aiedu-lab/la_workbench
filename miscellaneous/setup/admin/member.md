# Managing Repository Members

One-time reference for admin-level collaborator management via
`gh`. Only users with **admin** permission on the repo can add
collaborators or change their permission level — GitHub returns a
403 otherwise.

---

## Section 1 — Check your own privilege level

```bash
gh api repos/aiedu-lab/la_workbench --jq '.permissions'
```

Expected: a JSON object like `{"admin": true, "maintain": true,
"push": true, "triage": true, "pull": true}`. You need `"admin":
true` to run the mutating commands below.

---

## Section 2 — Check another member's current role

```bash
gh api repos/aiedu-lab/la_workbench/collaborators/<username>/permission \
  --jq '.permission'
```

Expected: one of `read`, `triage`, `write`, `maintain`, `admin`
(the API also accepts/returns `pull`/`push` as aliases for
`read`/`write`).

---

## Section 3 — Add a contributor

Contributor = write access (can push branches, open PRs) without
repo-admin privileges.

```bash
gh api -X PUT repos/aiedu-lab/la_workbench/collaborators/<username> \
  -f permission=push
```

Validation: repeat Section 2's check — expect `write` (or `push`).

---

## Section 4 — Add a maintainer

Maintainer = `maintain` permission (manage issues/PRs and some
settings) without full `admin` (cannot change collaborator roles or
delete the repo).

```bash
gh api -X PUT repos/aiedu-lab/la_workbench/collaborators/<username> \
  -f permission=maintain
```

Validation: expect `maintain`.

---

## Section 5 — Demote a maintainer to contributor

Same endpoint, lower permission — GitHub overwrites the existing
role rather than requiring a separate "remove" step first:

```bash
gh api -X PUT repos/aiedu-lab/la_workbench/collaborators/<username> \
  -f permission=push
```

Validation: expect `write` (or `push`).

---

## Section 6 — Promote a contributor to maintainer

```bash
gh api -X PUT repos/aiedu-lab/la_workbench/collaborators/<username> \
  -f permission=maintain
```

Validation: expect `maintain`.

---

## Reference

GitHub's collaborator-permission levels and the REST endpoints used
above are documented at
[docs.github.com/en/rest/collaborators/collaborators](
  https://docs.github.com/en/rest/collaborators/collaborators
).
