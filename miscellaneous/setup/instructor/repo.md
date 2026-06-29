# Repository Hygiene Setup

One-time GitHub settings so no one can commit directly to `main` —
every change goes through a branch + pull request, matching the
sister repo (`ai_workbench`) norms. Time required: ~10 minutes.

---

## Section 1 — Confirm CODEOWNERS is in place

`CODEOWNERS` already exists at `.github/CODEOWNERS` and assigns a
required reviewer (`@asarcar`) for every path. Branch protection
(Section 2) is what makes this enforced rather than advisory.

```bash
cat .github/CODEOWNERS
```

Expected: a default `* @asarcar` rule plus any path-specific rules.

---

## Section 2 — Enable branch protection on `main`

GitHub UI: **Settings → Branches → Add branch protection rule**

- Branch name pattern: `main`
- Require a pull request before merging
  - Require approvals: `1`
  - Require review from Code Owners: **checked**
- Require status checks to pass before merging (add CI checks here
  once any are configured)
- Do not allow bypassing the above settings
- Restrict who can push to matching branches: **no one** (forces
  all changes through a PR)
- Do **not** allow force pushes
- Do **not** allow deletions

Equivalent via `gh`:

```bash
gh api -X PUT repos/aiedu-lab/la_workbench/branches/main/protection \
  -H "Accept: application/vnd.github+json" \
  -f required_pull_request_reviews.required_approving_review_count=1 \
  -F required_pull_request_reviews.require_code_owner_reviews=true \
  -F enforce_admins=true \
  -F required_status_checks=null \
  -F restrictions=null \
  -F allow_force_pushes=false \
  -F allow_deletions=false
```

Validation:

```bash
gh api repos/aiedu-lab/la_workbench/branches/main/protection \
  --jq '.required_pull_request_reviews.require_code_owner_reviews'
```

Expected: `true`.

---

## Section 3 — Confirm the Claude PR review workflow is active

`.github/workflows/claude-review.yml` runs an automated review
whenever someone comments `@claude review` on a pull request. It
needs two repository secrets set under **Settings → Secrets and
variables → Actions**:

- `CLAUDE_CODE_OAUTH_TOKEN`
- `ANTHROPIC_API_KEY`

Validation:

```bash
gh secret list --repo aiedu-lab/la_workbench
```

Expected: both secret names listed (values are never shown).

---

## Section 4 — Verify the hygiene end-to-end

1. Create a throwaway branch, push a trivial change, open a PR.
2. Confirm the PR cannot be merged without an approving review from
   a Code Owner.
3. Confirm a direct `git push origin main` is rejected:

```bash
git push origin main
# Expected: remote rejects with a branch-protection error
```

4. Close/delete the throwaway PR and branch once verified.
