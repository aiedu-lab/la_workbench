# Software Driven Specification Plan for creation of LA Workbench

TL;DR
This document captures the specification plan used to craft the course
content delivered by a math, ai, or cs educator. It builds a hands-on 
Linear Algebra (LA) lab for high schoolers and freshman undergraduates, 
teaching them the basics of Linear Algebra as a practitioner.

---

## Phase 1: Repo Bootstrap & Contextualization

### Step 1.1: Contextualize CLAUDE.md/AGENTS.md for LA Workbench

[x] Status

CONTEXT: `CLAUDE.md` (symlinked as `AGENTS.md`) still carries the AI Workbench `PROJECT OVERVIEW` and `PROJECT-SPECIFIC NOTES` sections; the rest of the file (Plan Update Protocol, behavioral invariants, style rules) is repo-agnostic and correct as-is.
ACTION: Edit `CLAUDE.md`'s `PROJECT OVERVIEW` section to describe the Linear Algebra Workbench instead of AI Workbench, and its `PROJECT-SPECIFIC NOTES` section to drop AI-Workbench-only references (e.g. Group Meetup Organizer) in favor of LA Workbench's own session/project naming.
CONSTRAINTS: Do not touch the Plan Update Protocol, Behavioral Invariants, Documentation, Style & Hygiene, or Session Rehydration sections.
OUTPUT: Updated `CLAUDE.md` with an LA-Workbench-specific overview; `AGENTS.md` symlink unchanged.
VERIFY: `grep -i "meetup\|Group Meetup Organizer" CLAUDE.md` → 0 matches.

### Step 1.2: Contextualize instructor.md — keep Discord, drop meetup-organizer content

[x] Status

CONTEXT: `miscellaneous/setup/instructor/instructor.md` was copied verbatim from the sister repo; its Discord and smoke-test sections are built around the Group Meetup Organizer webhook/notifier pipeline, which has no LA Workbench equivalent, but the class still wants a Discord channel for general discussion/coordination.
ACTION: Rewrite the Discord section to set up a general class discussion/coordination channel (drop webhook/`DISCORD_WEBHOOK_URL` automation and the meetup-notification validation script, keep create-server/create-channel/invite/confirm-join steps); remove the meetup-pipeline smoke-test section entirely; renumber remaining sections; update closing Teaching-Philosophy text to reference Linear Algebra instead of Group Meetup Organizer.
CONSTRAINTS: Keep the roster and laptop-preflight sections and the simplified Discord section intact; do not add new Discord automation beyond manual server/channel/invite setup.
OUTPUT: Updated `instructor.md` with Discord retained in simplified form and meetup-organizer-specific content removed.
VERIFY: `grep -i "meetup\|DISCORD_WEBHOOK_URL" miscellaneous/setup/instructor/instructor.md` → 0 matches; `grep -ic "discord" miscellaneous/setup/instructor/instructor.md` → greater than 0.

### Step 1.3: Author repo hygiene doc

[x] Status

CONTEXT: No `miscellaneous/setup/instructor/repo.md` exists yet; the prompt requires documented GitHub settings enforcing "no commits to main, all changes via branch + PR," matching the sister repo's norms already reflected in `.github/CODEOWNERS`.
ACTION: Create `miscellaneous/setup/instructor/repo.md` with step-by-step GitHub UI/CLI instructions to enable branch protection on `main` (require PR, require CODEOWNERS review, disallow direct pushes/force-push), and confirm `.github/CODEOWNERS` and `.github/workflows/claude-review.yml` are active.
CONSTRAINTS: Do not modify `.github/CODEOWNERS` or `.github/workflows/claude-review.yml` — document existing settings only.
OUTPUT: New file `miscellaneous/setup/instructor/repo.md`.
VERIFY: `test -f miscellaneous/setup/instructor/repo.md && echo OK` → `OK`.

### Step 1.4: Update README.md agenda with session cross-links

[x] Status

CONTEXT: `README.md` has a flat 17-topic Agenda table with no links to `sessions/` or `projects/` files, and no Introduction / Dev Workbench Setup rows, unlike the sister repo's README style.
ACTION: Add an Introduction row and a Development Workbench Setup row to the Agenda table, and convert each of the 17 existing topic names into links of the form `[Topic](sessions/<slug>.md)`, where `<slug>` matches the placeholder filenames created in Step 1.6.
CONSTRAINTS: Do not change the Prerequisites, Teaching Philosophy, or Learning Outcome sections.
OUTPUT: Updated `README.md` Agenda table with working relative links.
VERIFY: `grep -c "](sessions/" README.md` → 19.

### Step 1.5: Create student setup toolchain

[x] Status

CONTEXT: `miscellaneous/setup/student/` does not exist yet; the prompt asks for `labsetup.py` and `preflight_check.py` (NumPy, PyTorch, Jupyter, common tools) using a `.venv` at repo root with `requirements.in`/`requirements.txt` — narrower scope than the sister repo's meetup-specific `poller.py`/`selector.py`/`notifier.py`.
ACTION: Create `miscellaneous/setup/student/requirements.in` (numpy, torch, jupyter, matplotlib), compile it to `requirements.txt`, and create `labsetup.py` (creates `.venv` at repo root, installs from `requirements.txt`) and `preflight_check.py` (verifies Python version, `.venv` active, and each package importable).
CONSTRAINTS: Do not create `poller.py`, `selector.py`, `notifier.py`, `config.yaml`, or `labenv.yaml` — meetup-organizer-specific and out of scope.
OUTPUT: Four new files under `miscellaneous/setup/student/`.
VERIFY: `python3 miscellaneous/setup/student/preflight_check.py` → all checks `PASS` after `labsetup.py` has been run once.

### Step 1.6: Create placeholder sessions and matching project dirs

[x] Status

CONTEXT: `sessions/` and `projects/` are both empty; the README Agenda (Step 1.4) lists 17 LA topics plus Introduction and Dev Workbench Setup, each needing a session placeholder, with hands-on exercises also needing a matching `projects/<slug>/` directory.
ACTION: Create one placeholder file per agenda row in `sessions/` (one-line title plus a `<!-- TODO: content -->` marker), and matching empty `projects/<slug>/` directories with a placeholder `README.md` only for hands-on exercise rows.
CONSTRAINTS: Placeholders only, no actual lesson content; do not rename or reorder the 17 agenda rows from Step 1.4.
OUTPUT: 19 new files under `sessions/`; one `projects/<slug>/` per exercise row.
VERIFY: `ls sessions/*.md | wc -l` → `19`.

### Step 1.8: Cross-link la_workbench and ai_workbench READMEs

[x] Status

CONTEXT: Neither `README.md` currently mentions the other repo; `la_workbench` is independent of `ai_workbench` but a companion curriculum — LA fundamentals help students grok the AI Workbench exercises, and LA mechanics are the engine under those exercises.
ACTION: Add a "Companion Repository" callout to `la_workbench/README.md` (after Objective) linking to `ai_workbench`, and a symmetric callout to `../ai_workbench/README.md` (after its Objective) linking back to `la_workbench`.
CONSTRAINTS: This step touches `../ai_workbench/README.md`, a separate git repository with its own history/remote — get explicit confirmation before committing/pushing there. Do not alter either README's Agenda table or other sections.
OUTPUT: Two updated `README.md` files, one per repo, each referencing the other by name and GitHub URL.
VERIFY: `grep -i "ai_workbench" README.md` (la_workbench) → match; `grep -i "la_workbench" ../ai_workbench/README.md` → match.

### Step 1.9: Mark Phase 1 complete

[ ] Status

CONTEXT: Steps 1.1–1.8 are committed and verified individually.
ACTION: Flip every `[ ] Status` → `[x] Status` in the Phase 1 block of this file.
CONSTRAINTS: Do not modify step content, only status lines.
OUTPUT: All Phase 1 steps show `[x] Status`.
VERIFY: `grep -A1 "### Step 1\." miscellaneous/software_defined_workbench/plan.md | grep "\[ \] Status"` → 0 matches. Commit all changed files and tag `v1.9-bootstrap-contextualization-step-completed`.

---

## Phase 2: Content Authoring — Sessions, Exercises, Capstone

### Step 2.1: Merge overlapping vector sessions, add the Titanic capstone slot, renumber the Agenda

[x] Status

CONTEXT: `scalars_vectors_matrices.md`, `vectors_points_directions.md`, `vector_operations.md` (Agenda rows 3–5) all map to 3Blue1Brown Ep.1; their matching `projects/` dirs are still empty placeholders. The Kaggle Titanic capstone needs a new dedicated Agenda row/session/project at the end of the curriculum, separate from `gradients_backpropagation.md`.
ACTION: Rename `scalars_vectors_matrices.md`'s title to "Scalars, Vectors and Matrices: Definition, Operations, and Geometric Intuition"; delete `sessions/vectors_points_directions.md`, `sessions/vector_operations.md`, `projects/vectors_points_directions/`, `projects/vector_operations/`; create placeholder `sessions/kaggle_titanic_capstone.md` (title + `<!-- TODO: content -->`) and `projects/kaggle_titanic_capstone/README.md` placeholder; in `README.md` Agenda, remove old rows 4–5, merge their why/motivation/AI cell text into row 3, renumber old rows 6–17 down to 4–15, and append a new row 16 "Kaggle Titanic Capstone" linking the two new placeholder files.
CONSTRAINTS: Do not touch Introduction/Dev Workbench Setup rows; do not yet add real body content to the merged or capstone session/project — body content is Step 2.5 (merge) and Step 2.17 (capstone).
OUTPUT: README.md with 16 numbered rows (18 total incl. Introduction/Dev Workbench Setup); `sessions/` has 18 files (was 19: -2 merged, +1 capstone); `projects/` has 16 dirs (was 17: -2 merged, +1 capstone).
VERIFY: `ls sessions/*.md | wc -l` → `18`; `ls -d projects/*/ | wc -l` → `16`; `grep -c "](sessions/" README.md` → `18`.

### Step 2.2: Author sessions/introduction.md

[x] Status

CONTEXT: Placeholder only; no course-orientation content exists.
ACTION: Write Concept section (course arc: LA as the language of AI, how sessions build on each other) and an Output/Logistics section pointing to `sessions/dev_workbench.md` as the next step; no Exercise section (orientation session).
CONSTRAINTS: Do not add lecture links (not a lecture-mapped session); keep to ai_workbench's session header style (`##` Concept, etc.).
OUTPUT: `sessions/introduction.md` with real content, no `<!-- TODO -->` markers.
VERIFY: `grep -c "TODO" sessions/introduction.md` → `0`.

### Step 2.3: Author sessions/dev_workbench.md

[x] Status

CONTEXT: Placeholder only; `miscellaneous/setup/student/labsetup.py` and `preflight_check.py` already exist and do real env setup; ai_workbench's `sessions/dev_workbench.md` is the DRY style template (Platform Overview, tool links, integration test, Additional Setups).
ACTION: Write, as the first section, "Sign Up for Google Colab" — link `https://colab.research.google.com/` and a short why-Colab blurb (zero-configuration browser-based Python, free GPU access, easy sharing, free account with access to popular LLMs and the Gemini API); then VSCode & Claude Code setup (link to `https://github.com/aiedu-lab/ai_workbench` tool guides per DRY, do not duplicate instructions inline), a "Colab" subsection for the VSCode-to-Colab extension, and a "Run Lab Setup Script" section documenting `labsetup.py`/`preflight_check.py` usage and expected PASS output.
CONSTRAINTS: Do not copy ai_workbench's tool-guide content verbatim into this repo — link out instead; do not modify `miscellaneous/setup/student/*`.
OUTPUT: `sessions/dev_workbench.md` with real content, Colab signup as its opening section.
VERIFY: `grep -ci "colab" sessions/dev_workbench.md` → `>0`; `grep -c "TODO" sessions/dev_workbench.md` → `0`.

### Step 2.4: Author sessions/what_is_a_model.md and sessions/why_linear_algebra.md

[x] Status

CONTEXT: Both are AI-framing sessions with no 3Blue1Brown/Strang counterpart; README Agenda already has "why it matters / motivation / AI connection" text to draw from.
ACTION: For each file, write a Concept section expanding the Agenda's why/motivation/AI-connection text into prose, and an Exercise section containing only `<!-- TODO: exercise -->` (deferred, no lecture or exercise mapping exists for these).
CONSTRAINTS: Do not add 3Blue1Brown/Strang links to either file.
OUTPUT: Both files have real Concept content; Exercise section is the explicit TODO placeholder, not the original whole-file TODO.
VERIFY: `grep -c "TODO: exercise" sessions/what_is_a_model.md sessions/why_linear_algebra.md` → `2`.

### Step 2.5: Author the merged Vectors session + wire Pirate Treasure Walk

[x] Status

CONTEXT: `sessions/scalars_vectors_matrices.md` title was updated in Step 2.1 but has no body; `projects/scalars_vectors_matrices/README.md` is a placeholder; "Pirate Treasure Walk" (vector add/scale, magnitude, quiver plotting) is the matching exercise per the mapping table above.
ACTION: Write Concept section linking 3Blue1Brown Ep.1 ("Vectors, what even are they?") via the topic URL; write Exercise section linking `../projects/scalars_vectors_matrices/`; port the Pirate Treasure Walk exercise body (from `.tmp/linear_algebra_python_exercises.txt`) into `projects/scalars_vectors_matrices/README.md` as runnable NumPy exercise instructions.
CONSTRAINTS: Do not touch the other 4 exercises in the `.tmp` file yet.
OUTPUT: Both files have real content; no TODO markers.
VERIFY: `grep -c "TODO" sessions/scalars_vectors_matrices.md projects/scalars_vectors_matrices/README.md` → `0`.

### Step 2.6: Author sessions/distance_length_similarity.md

[ ] Status

CONTEXT: Placeholder; maps to 3Blue1Brown Ep.9 ("Dot products and duality"); no exercise assigned this phase.
ACTION: Write Concept section linking 3Blue1Brown Ep.9 via the topic URL; Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not modify `projects/distance_length_similarity/README.md` (stays placeholder).
OUTPUT: Real Concept content in the session file.
VERIFY: `grep -c "TODO: exercise" sessions/distance_length_similarity.md` → `1`.

### Step 2.7: Author sessions/linear_transformations.md + wire Resize the Rocket and Make It Lean

[ ] Status

CONTEXT: Placeholder; maps to 3Blue1Brown Ep.3 ("Linear transformations and matrices"); both "Resize the Rocket" (dilation/determinant) and "Make It Lean" (shear) target this session per the mapping table.
ACTION: Write Concept section linking 3Blue1Brown Ep.3; Exercise section linking `../projects/linear_transformations/` and noting both sub-exercises; port both exercise bodies into `projects/linear_transformations/README.md` as two sequential parts.
CONSTRAINTS: Do not assign these 2 exercises elsewhere; do not touch Matrix Multiplication or Systems of Linear Equations files.
OUTPUT: Both files real, no TODO markers.
VERIFY: `grep -c "TODO" sessions/linear_transformations.md projects/linear_transformations/README.md` → `0`.

### Step 2.8: Author sessions/matrix_multiplication.md + wire Build a Flower with Rotations

[ ] Status

CONTEXT: Placeholder; maps to 3Blue1Brown Ep.4 ("Matrix multiplication as composition"); "Build a Flower with Rotations" targets this session.
ACTION: Write Concept section linking 3Blue1Brown Ep.4; Exercise section linking `../projects/matrix_multiplication/`; port the exercise body into `projects/matrix_multiplication/README.md`.
CONSTRAINTS: Do not touch other session/project files.
OUTPUT: Both files real, no TODO markers.
VERIFY: `grep -c "TODO" sessions/matrix_multiplication.md projects/matrix_multiplication/README.md` → `0`.

### Step 2.9: Author sessions/systems_of_linear_equations.md + wire The Snack Bar Mystery

[ ] Status

CONTEXT: Placeholder; maps to Strang's "Geometry of linear equations"/"Elimination" lectures; "The Snack Bar Mystery" (Ax=b, singular matrices) targets this session.
ACTION: Write Concept section linking the Strang video-gallery URL with the two lecture titles named in text; Exercise section linking `../projects/systems_of_linear_equations/`; port the exercise body into `projects/systems_of_linear_equations/README.md`.
CONSTRAINTS: Do not touch Column Space/Rank file (next, distinct lecture).
OUTPUT: Both files real, no TODO markers.
VERIFY: `grep -c "TODO" sessions/systems_of_linear_equations.md projects/systems_of_linear_equations/README.md` → `0`.

### Step 2.10: Author sessions/column_space_rank.md

[ ] Status

CONTEXT: Placeholder; maps to 3Blue1Brown Ep.7/8 ("Inverse matrices, column space and null space" / "Nonsquare matrices") and Strang's column space/independence lectures; no exercise assigned this phase.
ACTION: Write Concept section linking both 3Blue1Brown chapters and the Strang gallery; Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not modify `projects/column_space_rank/README.md`.
OUTPUT: Real Concept content.
VERIFY: `grep -c "TODO: exercise" sessions/column_space_rank.md` → `1`.

### Step 2.11: Author sessions/basis_change_of_basis.md

[ ] Status

CONTEXT: Placeholder; maps to 3Blue1Brown Ep.2 ("Linear combinations, span, and basis vectors") and Ep.13 ("Change of basis"); no exercise assigned this phase.
ACTION: Write Concept section linking both 3Blue1Brown chapters; Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not modify `projects/basis_change_of_basis/README.md`.
OUTPUT: Real Concept content.
VERIFY: `grep -c "TODO: exercise" sessions/basis_change_of_basis.md` → `1`.

### Step 2.12: Author sessions/orthogonality_projections.md

[ ] Status

CONTEXT: Placeholder; maps to Strang's "Projections onto subspaces"/"Projection matrices and least squares" lectures; no exercise assigned this phase.
ACTION: Write Concept section linking the Strang gallery with both lecture titles named; Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not modify `projects/orthogonality_projections/README.md`.
OUTPUT: Real Concept content.
VERIFY: `grep -c "TODO: exercise" sessions/orthogonality_projections.md` → `1`.

### Step 2.13: Author sessions/eigenvectors_eigenvalues.md

[ ] Status

CONTEXT: Placeholder; maps to 3Blue1Brown Ep.14/15 ("Eigenvectors and eigenvalues" / "A quick trick for computing eigenvalues") and Strang's eigenvalue lecture; no exercise assigned this phase.
ACTION: Write Concept section linking both sources; Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not modify `projects/eigenvectors_eigenvalues/README.md`.
OUTPUT: Real Concept content.
VERIFY: `grep -c "TODO: exercise" sessions/eigenvectors_eigenvalues.md` → `1`.

### Step 2.14: Author sessions/high_dimensional_geometry.md and sessions/embeddings.md

[ ] Status

CONTEXT: Both are AI-only sessions with no 3Blue1Brown/Strang counterpart; no exercise assigned this phase.
ACTION: For each file, write a Concept section expanding the Agenda's why/motivation/AI-connection text into prose; Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not add lecture links to either file.
OUTPUT: Both files have real Concept content.
VERIFY: `grep -c "TODO: exercise" sessions/high_dimensional_geometry.md sessions/embeddings.md` → `2`.

### Step 2.15: Author sessions/forward_propagation.md

[ ] Status

CONTEXT: AI-only session, no lecture counterpart; no exercise assigned this phase.
ACTION: Write Concept section expanding the Agenda's why/motivation/AI-connection text; Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not add lecture links.
OUTPUT: Real Concept content.
VERIFY: `grep -c "TODO: exercise" sessions/forward_propagation.md` → `1`.

### Step 2.16: Author sessions/gradients_backpropagation.md

[ ] Status

CONTEXT: AI-only session, no lecture counterpart; no exercise assigned this phase — the Titanic capstone is now a separate dedicated session (Step 2.17), not part of this file.
ACTION: Write Concept section (gradient descent/backprop, no lecture link); Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not reference Titanic in this file; do not add lecture links.
OUTPUT: Real Concept content.
VERIFY: `grep -c "TODO: exercise" sessions/gradients_backpropagation.md` → `1`.

### Step 2.17: Author the Kaggle Titanic capstone session

[ ] Status

CONTEXT: `sessions/kaggle_titanic_capstone.md` and `projects/kaggle_titanic_capstone/README.md` were created as placeholders in Step 2.1; this is the curriculum's final, overarching capstone — distinct from every other session's small toy exercise.
ACTION: Write Concept section framing this as the capstone that ties together vectors, transformations, systems of equations, and gradients/backprop into one end-to-end real-world model; Exercise section linking `../projects/kaggle_titanic_capstone/`; in that project's README, write the full Titanic exercise (link `https://www.kaggle.com/competitions/titanic`, frame it as training a complete model end-to-end, contrasted with the toy per-session exercises elsewhere in the curriculum).
CONSTRAINTS: Do not modify `sessions/gradients_backpropagation.md` or its project dir in this step.
OUTPUT: Both capstone files real; no TODO markers.
VERIFY: `grep -ci "titanic" sessions/kaggle_titanic_capstone.md projects/kaggle_titanic_capstone/README.md` → both `>0`; `grep -c "TODO" sessions/kaggle_titanic_capstone.md projects/kaggle_titanic_capstone/README.md` → `0`.

### Step 2.18: Mark Phase 2 complete

[ ] Status

CONTEXT: Steps 2.1–2.17 are committed and verified individually.
ACTION: Flip every `[ ] Status` → `[x] Status` in the Phase 2 block of this file.
CONSTRAINTS: Do not modify step content, only status lines.
OUTPUT: All Phase 2 steps show `[x] Status`.
VERIFY: `grep -A1 "### Step 2\." miscellaneous/software_defined_workbench/plan.md | grep "\[ \] Status"` → 0 matches. Commit all changed files and tag `v2.18-content-phase2-step-completed`, push with `--tags`.

---
