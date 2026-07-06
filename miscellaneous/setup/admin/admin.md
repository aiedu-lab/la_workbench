# Admin Guide

Everything a repo **admin** manages: one-time repo-hygiene setup
(branch protection, CODEOWNERS, CI secrets) and ongoing collaborator
role management. Time required: ~15 minutes for first-time setup.

---

## Section 1 — Validate your admin role

```bash
gh auth status
gh api repos/aiedu-lab/la_workbench --jq '.permissions.admin'
```

Expected: `gh auth status` shows you logged in, and the second
command prints `true` — every mutating command in this file
(branch protection, secrets, collaborator roles) requires `admin`.

---

## Section 2 — Confirm CODEOWNERS is in place

`CODEOWNERS` already exists at `.github/CODEOWNERS` and assigns a
required reviewer (`@asarcar`) for every path. Branch protection
(Section 3) is what makes this enforced rather than advisory.

```bash
cat .github/CODEOWNERS
```

Expected: a default `* @asarcar` rule plus any path-specific rules.

---

## Section 3 — Enable branch protection on `main`

GitHub UI: **Settings → Branches → Add branch protection rule**

- Branch name pattern: `main`
- Require a pull request before merging
  - Require approvals: `0` (write-access contributors, including the
    instructor, may merge their own PRs without a second reviewer)
  - Require review from Code Owners: **unchecked**
  - Dismiss stale pull request approvals when new commits are pushed:
    **checked**
- Require linear history: **checked**
- Do not allow bypassing the above settings
- Restrict who can push to matching branches: **no one** (forces
  all changes through a PR)
- Do **not** allow force pushes
- Do **not** allow deletions

Equivalent via `gh`. The nested `required_pull_request_reviews`
object must be sent as raw JSON via `--input` — `gh api`'s dotted
`-f`/`-F` flattening fails with `"required_pull_request_reviews"
wasn't supplied` on `gh` 2.79.0:

```bash
cat <<'EOF' | gh api -X PUT \
  repos/aiedu-lab/la_workbench/branches/main/protection \
  -H "Accept: application/vnd.github+json" --input -
{
  "required_status_checks": null,
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 0,
    "require_code_owner_reviews": false,
    "dismiss_stale_reviews": true
  },
  "required_linear_history": true,
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
EOF
```

Validation:

```bash
gh api repos/aiedu-lab/la_workbench/branches/main/protection \
  --jq '{
    review_count: .required_pull_request_reviews
                    .required_approving_review_count,
    code_owner_required: .required_pull_request_reviews
                           .require_code_owner_reviews,
    enforce_admins: .enforce_admins.enabled,
    linear_history: .required_linear_history.enabled,
    force_push: .allow_force_pushes.enabled
  }'
```

Expected:

```json
{
  "review_count": 0,
  "code_owner_required": false,
  "enforce_admins": true,
  "linear_history": true,
  "force_push": false
}
```

---

## Section 4 — Claude PR review workflow secrets (optional)

`.github/workflows/claude-review.yml` enables an automated
`@claude review` command on pull requests. It runs **only** in
headless GitHub Actions mode — not during normal interactive `claude`
CLI use, where credentials are read from
`~/.claude/.credentials.json`.

**The repo works fully without these secrets.** Setting them is
only required if you want to activate the `@claude review` PR
workflow.

### Two credential types

| Secret | What it is | When used |
|---|---|---|
| `CLAUDE_CODE_OAUTH_TOKEN` | Long-lived OAuth token tied to your Anthropic account (Pro/Max subscription billed) | Preferred for headless/CI use |
| `ANTHROPIC_API_KEY` | API key from `console.anthropic.com` (pay-per-token) | Fallback when subscription quota is exhausted |

When both are set, `CLAUDE_CODE_OAUTH_TOKEN` takes precedence.

### How to generate the tokens

**`CLAUDE_CODE_OAUTH_TOKEN`** — run once on any machine where a
browser can open (not WSL without workaround):

```bash
claude setup-token
# follow the prompt; outputs a sk-ant-oat01-... token valid ~1 year
```

**`ANTHROPIC_API_KEY`** — create at `console.anthropic.com`:
`API Keys → Create Key`.

### How to set the GitHub repository secrets

**GitHub UI:** **Settings → Secrets and variables → Actions →
New repository secret** → enter name and value.

**`gh` CLI** (value read from stdin — never put the token inline on
the command line where it would appear in shell history):

```bash
# read the token value from stdin
gh secret set CLAUDE_CODE_OAUTH_TOKEN \
  --repo aiedu-lab/la_workbench

gh secret set ANTHROPIC_API_KEY \
  --repo aiedu-lab/la_workbench
```

`gh secret set` prompts interactively for the value, or you can
pipe it: `echo "$TOKEN" | gh secret set ... --body -`.

Validation (names only — values are never shown):

```bash
gh secret list --repo aiedu-lab/la_workbench
```

Expected: both `CLAUDE_CODE_OAUTH_TOKEN` and `ANTHROPIC_API_KEY`
listed (or at minimum `CLAUDE_CODE_OAUTH_TOKEN` if you chose not to
set the API key fallback).

---

## Section 5 — Verify the hygiene end-to-end

1. Create a throwaway branch, push a trivial change, open a PR.
2. Confirm the PR can be merged by the instructor without a second
   approving review (write-access contributors do not need to
   self-review).
3. Confirm a direct `git push origin main` is rejected:

```bash
git push origin main
# Expected: remote rejects with a branch-protection error
```

4. Close/delete the throwaway PR and branch once verified.

---

## Section 6 — Check another member's current role

```bash
gh api repos/aiedu-lab/la_workbench/collaborators/<username>/permission \
  --jq '.permission'
```

Expected: one of `read`, `triage`, `write`, `maintain`, `admin`
(the API also accepts/returns `pull`/`push` as aliases for
`read`/`write`).

---

## Section 7 — Add a contributor

Contributor = write access (can push branches, open PRs) without
repo-admin privileges.

```bash
gh api -X PUT repos/aiedu-lab/la_workbench/collaborators/<username> \
  -f permission=push
```

Validation: repeat Section 6's check — expect `write` (or `push`).

---

## Section 8 — Add a maintainer

Maintainer = `maintain` permission (manage issues/PRs and some
settings) without full `admin` (cannot change collaborator roles or
delete the repo).

```bash
gh api -X PUT repos/aiedu-lab/la_workbench/collaborators/<username> \
  -f permission=maintain
```

Validation: expect `maintain`.

---

## Section 9 — Demote a maintainer to contributor

Same endpoint, lower permission — GitHub overwrites the existing
role rather than requiring a separate "remove" step first:

```bash
gh api -X PUT repos/aiedu-lab/la_workbench/collaborators/<username> \
  -f permission=push
```

Validation: expect `write` (or `push`).

---

## Section 10 — Promote a contributor to maintainer

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
