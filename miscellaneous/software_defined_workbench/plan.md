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

[x] Status

CONTEXT: Placeholder; maps to 3Blue1Brown Ep.9 ("Dot products and duality"); no exercise assigned this phase.
ACTION: Write Concept section linking 3Blue1Brown Ep.9 via the topic URL; Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not modify `projects/distance_length_similarity/README.md` (stays placeholder).
OUTPUT: Real Concept content in the session file.
VERIFY: `grep -c "TODO: exercise" sessions/distance_length_similarity.md` → `1`.

### Step 2.7: Author sessions/linear_transformations.md + wire Resize the Rocket and Make It Lean

[x] Status

CONTEXT: Placeholder; maps to 3Blue1Brown Ep.3 ("Linear transformations and matrices"); both "Resize the Rocket" (dilation/determinant) and "Make It Lean" (shear) target this session per the mapping table.
ACTION: Write Concept section linking 3Blue1Brown Ep.3; Exercise section linking `../projects/linear_transformations/` and noting both sub-exercises; port both exercise bodies into `projects/linear_transformations/README.md` as two sequential parts.
CONSTRAINTS: Do not assign these 2 exercises elsewhere; do not touch Matrix Multiplication or Systems of Linear Equations files.
OUTPUT: Both files real, no TODO markers.
VERIFY: `grep -c "TODO" sessions/linear_transformations.md projects/linear_transformations/README.md` → `0`.

### Step 2.8: Author sessions/matrix_multiplication.md + wire Build a Flower with Rotations

[x] Status

CONTEXT: Placeholder; maps to 3Blue1Brown Ep.4 ("Matrix multiplication as composition"); "Build a Flower with Rotations" targets this session.
ACTION: Write Concept section linking 3Blue1Brown Ep.4; Exercise section linking `../projects/matrix_multiplication/`; port the exercise body into `projects/matrix_multiplication/README.md`.
CONSTRAINTS: Do not touch other session/project files.
OUTPUT: Both files real, no TODO markers.
VERIFY: `grep -c "TODO" sessions/matrix_multiplication.md projects/matrix_multiplication/README.md` → `0`.

### Step 2.9: Author sessions/systems_of_linear_equations.md + wire The Snack Bar Mystery

[x] Status

CONTEXT: Placeholder; maps to Strang's "Geometry of linear equations"/"Elimination" lectures; "The Snack Bar Mystery" (Ax=b, singular matrices) targets this session.
ACTION: Write Concept section linking the Strang video-gallery URL with the two lecture titles named in text; Exercise section linking `../projects/systems_of_linear_equations/`; port the exercise body into `projects/systems_of_linear_equations/README.md`.
CONSTRAINTS: Do not touch Column Space/Rank file (next, distinct lecture).
OUTPUT: Both files real, no TODO markers.
VERIFY: `grep -c "TODO" sessions/systems_of_linear_equations.md projects/systems_of_linear_equations/README.md` → `0`.

### Step 2.10: Author sessions/column_space_rank.md

[x] Status

CONTEXT: Placeholder; maps to 3Blue1Brown Ep.7/8 ("Inverse matrices, column space and null space" / "Nonsquare matrices") and Strang's column space/independence lectures; no exercise assigned this phase.
ACTION: Write Concept section linking both 3Blue1Brown chapters and the Strang gallery; Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not modify `projects/column_space_rank/README.md`.
OUTPUT: Real Concept content.
VERIFY: `grep -c "TODO: exercise" sessions/column_space_rank.md` → `1`.

### Step 2.11: Author sessions/basis_change_of_basis.md

[x] Status

CONTEXT: Placeholder; maps to 3Blue1Brown Ep.2 ("Linear combinations, span, and basis vectors") and Ep.13 ("Change of basis"); no exercise assigned this phase.
ACTION: Write Concept section linking both 3Blue1Brown chapters; Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not modify `projects/basis_change_of_basis/README.md`.
OUTPUT: Real Concept content.
VERIFY: `grep -c "TODO: exercise" sessions/basis_change_of_basis.md` → `1`.

### Step 2.12: Author sessions/orthogonality_projections.md

[x] Status

CONTEXT: Placeholder; maps to Strang's "Projections onto subspaces"/"Projection matrices and least squares" lectures; no exercise assigned this phase.
ACTION: Write Concept section linking the Strang gallery with both lecture titles named; Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not modify `projects/orthogonality_projections/README.md`.
OUTPUT: Real Concept content.
VERIFY: `grep -c "TODO: exercise" sessions/orthogonality_projections.md` → `1`.

### Step 2.13: Author sessions/eigenvectors_eigenvalues.md

[x] Status

CONTEXT: Placeholder; maps to 3Blue1Brown Ep.14/15 ("Eigenvectors and eigenvalues" / "A quick trick for computing eigenvalues") and Strang's eigenvalue lecture; no exercise assigned this phase.
ACTION: Write Concept section linking both sources; Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not modify `projects/eigenvectors_eigenvalues/README.md`.
OUTPUT: Real Concept content.
VERIFY: `grep -c "TODO: exercise" sessions/eigenvectors_eigenvalues.md` → `1`.

### Step 2.14: Author sessions/high_dimensional_geometry.md and sessions/embeddings.md

[x] Status

CONTEXT: Both are AI-only sessions with no 3Blue1Brown/Strang counterpart; no exercise assigned this phase.
ACTION: For each file, write a Concept section expanding the Agenda's why/motivation/AI-connection text into prose; Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not add lecture links to either file.
OUTPUT: Both files have real Concept content.
VERIFY: `grep -c "TODO: exercise" sessions/high_dimensional_geometry.md sessions/embeddings.md` → `2`.

### Step 2.15: Author sessions/forward_propagation.md

[x] Status

CONTEXT: AI-only session, no lecture counterpart; no exercise assigned this phase.
ACTION: Write Concept section expanding the Agenda's why/motivation/AI-connection text; Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not add lecture links.
OUTPUT: Real Concept content.
VERIFY: `grep -c "TODO: exercise" sessions/forward_propagation.md` → `1`.

### Step 2.16: Author sessions/gradients_backpropagation.md

[x] Status

CONTEXT: AI-only session, no lecture counterpart; no exercise assigned this phase — the Titanic capstone is now a separate dedicated session (Step 2.17), not part of this file.
ACTION: Write Concept section (gradient descent/backprop, no lecture link); Exercise section is `<!-- TODO: exercise -->`.
CONSTRAINTS: Do not reference Titanic in this file; do not add lecture links.
OUTPUT: Real Concept content.
VERIFY: `grep -c "TODO: exercise" sessions/gradients_backpropagation.md` → `1`.

### Step 2.17: Author the Kaggle Titanic capstone session

[x] Status

CONTEXT: `sessions/kaggle_titanic_capstone.md` and `projects/kaggle_titanic_capstone/README.md` were created as placeholders in Step 2.1; this is the curriculum's final, overarching capstone — distinct from every other session's small toy exercise.
ACTION: Write Concept section framing this as the capstone that ties together vectors, transformations, systems of equations, and gradients/backprop into one end-to-end real-world model; Exercise section linking `../projects/kaggle_titanic_capstone/`; in that project's README, write the full Titanic exercise (link `https://www.kaggle.com/competitions/titanic`, frame it as training a complete model end-to-end, contrasted with the toy per-session exercises elsewhere in the curriculum).
CONSTRAINTS: Do not modify `sessions/gradients_backpropagation.md` or its project dir in this step.
OUTPUT: Both capstone files real; no TODO markers.
VERIFY: `grep -ci "titanic" sessions/kaggle_titanic_capstone.md projects/kaggle_titanic_capstone/README.md` → both `>0`; `grep -c "TODO" sessions/kaggle_titanic_capstone.md projects/kaggle_titanic_capstone/README.md` → `0`.

### Step 2.18: Mark Phase 2 complete

[x] Status

CONTEXT: Steps 2.1–2.17 are committed and verified individually.
ACTION: Flip every `[ ] Status` → `[x] Status` in the Phase 2 block of this file.
CONSTRAINTS: Do not modify step content, only status lines.
OUTPUT: All Phase 2 steps show `[x] Status`.
VERIFY: `grep -A1 "### Step 2\." miscellaneous/software_defined_workbench/plan.md | grep "\[ \] Status"` → 0 matches. Commit all changed files and tag `v2.18-content-phase2-step-completed`, push with `--tags`.

---

## Phase 3: Cleanup — Toy Exercises & Skill Validation

### Step 3.1: Validate replan/execute skill split, commit pending edits

[x] Status

CONTEXT: `.claude/commands/replan.md` was refactored in the working tree (uncommitted) to stop after committing the approved plan and hand off to `/execute`; a new untracked `.claude/commands/execute.md` owns per-step execution (VERIFY, status-flip, commit, final tag/push). Six session files (`dev_workbench.md`, `kaggle_titanic_capstone.md`, `linear_transformations.md`, `matrix_multiplication.md`, `scalars_vectors_matrices.md`, `systems_of_linear_equations.md`) also carry pending, already-made 79-char line-wrap fixes from a prior session.
ACTION: Confirm `replan.md` stops cleanly at the "invoke /execute" handoff with no residual execute-time logic, and `execute.md` fully owns per-step execution with no gaps or duplicated responsibility — both already reviewed as correct, so no text edits are needed. Stage and commit `.claude/commands/replan.md`, `.claude/commands/execute.md`, and the six pending session files together.
CONSTRAINTS: Do not further edit the text of `replan.md`, `execute.md`, or the six session files beyond what is already in the working tree.
OUTPUT: All seven files committed; no unrelated content changes.
VERIFY: `git status --porcelain -- .claude/commands/replan.md .claude/commands/execute.md sessions/dev_workbench.md sessions/kaggle_titanic_capstone.md sessions/linear_transformations.md sessions/matrix_multiplication.md sessions/scalars_vectors_matrices.md sessions/systems_of_linear_equations.md` → empty output.

### Step 3.2: Retrofit Pirate Treasure Walk with Help section

[x] Status

CONTEXT: `projects/scalars_vectors_matrices/README.md` has real content but only a one-line `Handy:` hint and no reusable plotting helper or automated validation, falling short of Cleanup point 5.
ACTION: Add a `## Help` section with a `plot_vectors(vecs, origin=(0,0), colors=None, labels=None)` helper (wraps `plt.quiver` + `plt.gca().set_aspect('equal')`) reusable across all four bullet steps, and a validation snippet `assert np.allclose(final_position, moves.sum(axis=0))` tied to the treasure's final coordinates.
CONSTRAINTS: Do not change the existing Skills/steps/Stretch-goal text, only append the `## Help` section.
OUTPUT: `projects/scalars_vectors_matrices/README.md` has a `## Help` section with helper function + assert-based validation.
VERIFY: `grep -c "## Help" projects/scalars_vectors_matrices/README.md` → `1`; `grep -c "assert" projects/scalars_vectors_matrices/README.md` → `>0`.

### Step 3.3: Retrofit Resize the Rocket / Make It Lean with Help section

[x] Status

CONTEXT: `projects/linear_transformations/README.md` has real content but only a one-line `Handy:` hint and no reusable plotting helper or automated validation, falling short of Cleanup point 5.
ACTION: Add a `## Help` section with a `plot_points(points, ax=None, color='C0', label=None)` helper (scatter/line plot + equal aspect) reusable for both parts, and validation snippets `assert np.isclose(np.linalg.det(A), expected_area_factor)` (Part 1) and `assert np.isclose(np.linalg.det(shear), 1.0)` (Part 2, area preserved).
CONSTRAINTS: Do not change the existing Skills/steps/Stretch-goal text for either part, only append the `## Help` section.
OUTPUT: `projects/linear_transformations/README.md` has a `## Help` section with helper function + assert-based validation.
VERIFY: `grep -c "## Help" projects/linear_transformations/README.md` → `1`; `grep -c "assert" projects/linear_transformations/README.md` → `>0`.

### Step 3.4: Retrofit Build a Flower with Rotations with Help section

[x] Status

CONTEXT: `projects/matrix_multiplication/README.md` has real content but only a one-line `Handy:` hint and no reusable plotting helper or automated validation, falling short of Cleanup point 5.
ACTION: Add a `## Help` section with a `plot_shape(points, ax=None, color='C0')` helper (equal-aspect scatter/line plot of the petal), and a validation snippet `assert np.allclose(rot(30) @ rot(30), rot(60))`.
CONSTRAINTS: Do not change the existing Skills/steps/Stretch-goal text, only append the `## Help` section.
OUTPUT: `projects/matrix_multiplication/README.md` has a `## Help` section with helper function + assert-based validation.
VERIFY: `grep -c "## Help" projects/matrix_multiplication/README.md` → `1`; `grep -c "assert" projects/matrix_multiplication/README.md` → `>0`.

### Step 3.5: Retrofit The Snack Bar Mystery with Help section

[x] Status

CONTEXT: `projects/systems_of_linear_equations/README.md` has real content but only a one-line `Handy:` hint and no reusable plotting helper or automated validation, falling short of Cleanup point 5.
ACTION: Add a `## Help` section with a `plot_lines(A, b, xlim=(-5, 5))` helper (plots both equations as lines + equal aspect), and a validation snippet `assert np.allclose(A @ x, b)` after solving with `np.linalg.solve`.
CONSTRAINTS: Do not change the existing Skills/steps/Stretch-goal text, only append the `## Help` section.
OUTPUT: `projects/systems_of_linear_equations/README.md` has a `## Help` section with helper function + assert-based validation.
VERIFY: `grep -c "## Help" projects/systems_of_linear_equations/README.md` → `1`; `grep -c "assert" projects/systems_of_linear_equations/README.md` → `>0`.

### Step 3.6: Toy exercise for Distance, Length and Similarity

[x] Status

CONTEXT: `sessions/distance_length_similarity.md`'s `## Exercise` is `<!-- TODO: exercise -->`; `projects/distance_length_similarity/README.md` is a one-line placeholder; session maps to 3Blue1Brown Ep.9 (dot products and duality).
ACTION: Author "Song Similarity Mini" in `projects/distance_length_similarity/README.md`: 3-4 songs as small hand-picked 2D/3D feature vectors (e.g. tempo, energy), compute dot product and `numpy.linalg.norm`, derive cosine similarity between pairs, find the "most similar" song to a query vector. Include a `## Help` section with a `plot_vectors(vecs, colors=None, labels=None)` helper (quiver + equal aspect) and a validation snippet `assert np.isclose(cosine_sim(a, b), (a @ b) / (norm(a) * norm(b)))`. Replace the TODO in `sessions/distance_length_similarity.md`'s Exercise section with a paragraph linking `../projects/distance_length_similarity/`.
CONSTRAINTS: Do not modify the Concept section of `sessions/distance_length_similarity.md`; do not touch other sessions/projects.
OUTPUT: Both files have real content, no TODO markers, `## Help` section present with helper + assert.
VERIFY: `grep -c "TODO" sessions/distance_length_similarity.md projects/distance_length_similarity/README.md` → `0`; `grep -c "## Help" projects/distance_length_similarity/README.md` → `1`.

### Step 3.7: Toy exercise for Column Space, Rank and Linear Independence

[x] Status

CONTEXT: `sessions/column_space_rank.md`'s `## Exercise` is `<!-- TODO: exercise -->`; `projects/column_space_rank/README.md` is a placeholder; session maps to 3Blue1Brown Ep.7/8 and Strang's column space/independence lectures.
ACTION: Author "Which Directions Can I Reach?" in `projects/column_space_rank/README.md`: given a small 2x2 and a 3x2 matrix, test whether a target vector `b` lies in the column span using `numpy.linalg.lstsq`/rank comparison, and compute rank via `numpy.linalg.matrix_rank`. Include a `## Help` section with a `plot_span_2d(cols, target=None)` helper (draws the span line/plane and marks the target point) and a validation snippet `assert np.allclose(A @ x_lstsq, b)` when `b` is reachable, else compares `matrix_rank(A)` vs `matrix_rank(np.c_[A, b])`. Replace the TODO in `sessions/column_space_rank.md`'s Exercise section with a paragraph linking `../projects/column_space_rank/`.
CONSTRAINTS: Do not modify the Concept section; do not touch other sessions/projects.
OUTPUT: Both files have real content, no TODO markers, `## Help` section present with helper + assert.
VERIFY: `grep -c "TODO" sessions/column_space_rank.md projects/column_space_rank/README.md` → `0`; `grep -c "## Help" projects/column_space_rank/README.md` → `1`.

### Step 3.8: Toy exercise for Basis and Change of Basis

[x] Status

CONTEXT: `sessions/basis_change_of_basis.md`'s `## Exercise` is `<!-- TODO: exercise -->`; `projects/basis_change_of_basis/README.md` is a placeholder; session maps to 3Blue1Brown Ep.2/13.
ACTION: Author "Describe It In My Coordinates" in `projects/basis_change_of_basis/README.md`: define a custom non-standard 2D basis (two vectors), convert a point's standard coordinates into that basis using `numpy.linalg.inv` and back. Include a `## Help` section with a `plot_basis_grid(basis, extent=5)` helper (draws the custom basis grid lines over the standard grid) and a validation snippet `assert np.allclose(basis @ coords_in_basis, point_standard)`. Replace the TODO in `sessions/basis_change_of_basis.md`'s Exercise section with a paragraph linking `../projects/basis_change_of_basis/`.
CONSTRAINTS: Do not modify the Concept section; do not touch other sessions/projects.
OUTPUT: Both files have real content, no TODO markers, `## Help` section present with helper + assert.
VERIFY: `grep -c "TODO" sessions/basis_change_of_basis.md projects/basis_change_of_basis/README.md` → `0`; `grep -c "## Help" projects/basis_change_of_basis/README.md` → `1`.

### Step 3.9: Toy exercise for Orthogonality and Projections

[x] Status

CONTEXT: `sessions/orthogonality_projections.md`'s `## Exercise` is `<!-- TODO: exercise -->`; `projects/orthogonality_projections/README.md` is a placeholder; session maps to Strang's projections/least-squares lectures.
ACTION: Author "Shadow on the Wall" in `projects/orthogonality_projections/README.md`: project a vector onto a line (another vector) via the projection formula and/or projection matrix, decompose into projection + perpendicular residual. Include a `## Help` section with a `plot_projection(v, a, proj)` helper (draws `v`, the line through `a`, the shadow `proj`, and the residual) and a validation snippet `assert np.isclose(residual @ a, 0)` confirming orthogonality. Replace the TODO in `sessions/orthogonality_projections.md`'s Exercise section with a paragraph linking `../projects/orthogonality_projections/`.
CONSTRAINTS: Do not modify the Concept section; do not touch other sessions/projects.
OUTPUT: Both files have real content, no TODO markers, `## Help` section present with helper + assert.
VERIFY: `grep -c "TODO" sessions/orthogonality_projections.md projects/orthogonality_projections/README.md` → `0`; `grep -c "## Help" projects/orthogonality_projections/README.md` → `1`.

### Step 3.10: Toy exercise for Eigenvectors and Eigenvalues

[x] Status

CONTEXT: `sessions/eigenvectors_eigenvalues.md`'s `## Exercise` is `<!-- TODO: exercise -->`; `projects/eigenvectors_eigenvalues/README.md` is a placeholder; session maps to 3Blue1Brown Ep.14/15 and Strang's eigenvalue lecture.
ACTION: Author "Directions That Don't Turn" in `projects/eigenvectors_eigenvalues/README.md`: pick a small 2x2 matrix, apply it repeatedly to several candidate vectors to visually find which directions don't rotate, then verify with `numpy.linalg.eig`. Include a `## Help` section with a `plot_before_after(vecs, A)` helper (plots each vector and its image under `A`) and a validation snippet `assert np.allclose(A @ eigvec, eigval * eigvec)`. Replace the TODO in `sessions/eigenvectors_eigenvalues.md`'s Exercise section with a paragraph linking `../projects/eigenvectors_eigenvalues/`.
CONSTRAINTS: Do not modify the Concept section; do not touch other sessions/projects.
OUTPUT: Both files have real content, no TODO markers, `## Help` section present with helper + assert.
VERIFY: `grep -c "TODO" sessions/eigenvectors_eigenvalues.md projects/eigenvectors_eigenvalues/README.md` → `0`; `grep -c "## Help" projects/eigenvectors_eigenvalues/README.md` → `1`.

### Step 3.11: Toy exercise for High-Dimensional Geometry

[x] Status

CONTEXT: `sessions/high_dimensional_geometry.md`'s `## Exercise` is `<!-- TODO: exercise -->`; `projects/high_dimensional_geometry/README.md` is a placeholder; AI-only session, no lecture link.
ACTION: Author "Curse of Dimensionality Mini-Lab" in `projects/high_dimensional_geometry/README.md`: generate random points in increasing dimensions (e.g. 2, 3, 10, 100) with `numpy.random`, compute pairwise distances, show they concentrate as dimension grows. Include a `## Help` section with a `plot_distance_histograms(dists_by_dim)` helper (one histogram per dimension via `plt.hist`) and a validation snippet `assert dists_100d.std() / dists_100d.mean() < dists_2d.std() / dists_2d.mean()` confirming relative spread shrinks. Replace the TODO in `sessions/high_dimensional_geometry.md`'s Exercise section with a paragraph linking `../projects/high_dimensional_geometry/`.
CONSTRAINTS: Do not modify the Concept section; do not add lecture links; do not touch other sessions/projects.
OUTPUT: Both files have real content, no TODO markers, `## Help` section present with helper + assert.
VERIFY: `grep -c "TODO" sessions/high_dimensional_geometry.md projects/high_dimensional_geometry/README.md` → `0`; `grep -c "## Help" projects/high_dimensional_geometry/README.md` → `1`.

### Step 3.12: Toy exercise for Embeddings

[x] Status

CONTEXT: `sessions/embeddings.md`'s `## Exercise` is `<!-- TODO: exercise -->`; `projects/embeddings/README.md` is a placeholder; AI-only session, no lecture link.
ACTION: Author "Words as Vectors" in `projects/embeddings/README.md`: a small hand-built toy embedding table (~8 words to hand-picked 2D vectors), compute cosine similarity between word pairs, find the nearest neighbor of a query word. Include a `## Help` section with a `plot_word_vectors(embeddings, labels)` helper (`plt.scatter` + `plt.annotate` for each word) and a validation snippet `assert nearest_neighbor(query, embeddings) == expected_word`. Replace the TODO in `sessions/embeddings.md`'s Exercise section with a paragraph linking `../projects/embeddings/`.
CONSTRAINTS: Do not modify the Concept section; do not add lecture links; do not touch other sessions/projects.
OUTPUT: Both files have real content, no TODO markers, `## Help` section present with helper + assert.
VERIFY: `grep -c "TODO" sessions/embeddings.md projects/embeddings/README.md` → `0`; `grep -c "## Help" projects/embeddings/README.md` → `1`.

### Step 3.13: Toy exercise for Forward Propagation

[x] Status

CONTEXT: `sessions/forward_propagation.md`'s `## Exercise` is `<!-- TODO: exercise -->`; `projects/forward_propagation/README.md` is a placeholder; AI-only session, no lecture link.
ACTION: Author "One Neuron, Step by Step" in `projects/forward_propagation/README.md`: implement a tiny single-layer forward pass by hand with NumPy (input vector, weight matrix, bias, activation function), verify output against a manual hand calculation. Include a `## Help` section with a `plot_activation(fn, xrange=(-5, 5))` helper (plots the activation curve) and a validation snippet `assert np.allclose(forward(x, W, b), manual_expected)`. Replace the TODO in `sessions/forward_propagation.md`'s Exercise section with a paragraph linking `../projects/forward_propagation/`.
CONSTRAINTS: Do not modify the Concept section; do not add lecture links; do not touch other sessions/projects.
OUTPUT: Both files have real content, no TODO markers, `## Help` section present with helper + assert.
VERIFY: `grep -c "TODO" sessions/forward_propagation.md projects/forward_propagation/README.md` → `0`; `grep -c "## Help" projects/forward_propagation/README.md` → `1`.

### Step 3.14: Toy exercise for Gradients and Backpropagation

[x] Status

CONTEXT: `sessions/gradients_backpropagation.md`'s `## Exercise` is `<!-- TODO: exercise -->`; `projects/gradients_backpropagation/README.md` is a placeholder; AI-only session, no lecture link, no Titanic reference (capstone is separate).
ACTION: Author "Rolling Downhill" in `projects/gradients_backpropagation/README.md`: implement basic gradient descent on a toy 1D or 2D quadratic loss function by hand with NumPy, track the descent path across iterations. Include a `## Help` section with a `plot_descent(loss_fn, path)` helper (contour/curve of the loss plus the descent path overlaid) and a validation snippet `assert loss_fn(path[-1]) < loss_fn(path[0])` confirming the loss decreased. Replace the TODO in `sessions/gradients_backpropagation.md`'s Exercise section with a paragraph linking `../projects/gradients_backpropagation/`.
CONSTRAINTS: Do not modify the Concept section; do not reference Titanic; do not add lecture links; do not touch other sessions/projects.
OUTPUT: Both files have real content, no TODO markers, `## Help` section present with helper + assert.
VERIFY: `grep -c "TODO" sessions/gradients_backpropagation.md projects/gradients_backpropagation/README.md` → `0`; `grep -c "## Help" projects/gradients_backpropagation/README.md` → `1`.

### Step 3.15: Delete stale placeholder project directories

[x] Status

CONTEXT: `projects/what_is_a_model/` and `projects/why_linear_algebra/` are placeholder-only (title + `<!-- TODO: content -->`) leftovers from Step 1.6; their sessions are overview sessions with no `## Exercise` section by design, so no session claims either directory.
ACTION: `git rm -r projects/what_is_a_model projects/why_linear_algebra`.
CONSTRAINTS: Do not delete any other `projects/*` directory; do not modify `sessions/what_is_a_model.md` or `sessions/why_linear_algebra.md`.
OUTPUT: `projects/` no longer contains `what_is_a_model/` or `why_linear_algebra/`; 14 project directories remain.
VERIFY: `test -d projects/what_is_a_model -o -d projects/why_linear_algebra && echo FAIL || echo OK` → `OK`; `ls -d projects/*/ | wc -l` → `14`.

### Step 3.16: Mark Phase 3 complete

[x] Status

CONTEXT: Steps 3.1–3.15 are committed and verified individually.
ACTION: Flip every `[ ] Status` → `[x] Status` in the Phase 3 block of this file.
CONSTRAINTS: Do not modify step content, only status lines.
OUTPUT: All Phase 3 steps show `[x] Status`.
VERIFY: `grep -A1 "### Step 3\." miscellaneous/software_defined_workbench/plan.md | grep "\[ \] Status"` → 0 matches. Commit all changed files and tag `v3.16-toy-exercises-cleanup-step-completed`, push with `--tags`.

---

<!-- AI-GENERATED [claude-code:claude-sonnet-5]: Phase 4 (plan_history.md) -->

## Phase 4: Student Contribution & Completion-Report Mechanism

### Step 4.1: Author "Submitting Exercise Solutions" README section

[x] Status

CONTEXT: README.md's existing `# 🤝 Contribution Guidelines` section (README.md:65-76) covers repo-hygiene (branch+PR for content changes) only; no section explains how students record a completed exercise solution.
ACTION: Add a new `# 📤 Submitting Exercise Solutions` section to README.md, placed after `# 🤝 Contribution Guidelines` and before `# Learning Outcome`, documenting: (a) create `projects/<exercise>/<github-userid>/` (any one group member's userid) containing `solution.md` (Contributors: one bare GitHub-UserId per line / Test Cases / Software Installs / Solution Manual sections), source files, and `requirements.in`; (b) open a PR named `project/<exercise>/<github-userid>`; (c) once the maintainer approves and merges, `.github/workflows/report.yml` automatically regenerates `miscellaneous/report/report.md` and each contributor's `miscellaneous/report/student/<github-userid>-report.md`.
CONSTRAINTS: Do not modify the existing "Contribution Guidelines" or "Learning Outcome" sections' text.
OUTPUT: README.md has a new "Submitting Exercise Solutions" section.
VERIFY: `grep -c "Submitting Exercise Solutions" README.md` → `1`.

### Step 4.2: Create report.py and seed report.md

[x] Status

CONTEXT: `miscellaneous/report/` does not exist; no mechanism yet computes which students completed which exercises.
ACTION: Create `miscellaneous/report/report.py` that: (1) scans `projects/*/*/solution.md` for `## Contributors` blocks listing bare GitHub-UserIds; (2) resolves each userid's Full Name via `urllib.request` against `https://api.github.com/users/<userid>`'s `name` field (falls back to the raw userid if `name` is null); (3) writes `miscellaneous/report/report.md` as a Markdown table (rows = the 14 exercise project slugs linked to their session file; columns = distinct contributor userids, alphabetical; cell = ✅); (4) writes/updates `miscellaneous/report/student/<github-userid>-report.md` per contributor — Full Name, GitHub-UserId, Date Last Updated, then a table of the 14 topics (Topic, Concept description sourced from README.md's Agenda "Why it Matters" column, Completed ✅/blank) — rewriting a student's file (and bumping its date) only when that student's completion table content actually changed, so unrelated re-runs leave it untouched. Run it once to generate the initial (empty) `report.md`; no per-student files are created yet since no `solution.md` exists.
CONSTRAINTS: Do not modify any `projects/*/README.md`; use only the Python standard library (no new pip dependency); must be idempotent — re-running with unchanged submissions must not rewrite any file.
OUTPUT: New `miscellaneous/report/report.py`; new `miscellaneous/report/report.md` (all cells blank); new (empty) `miscellaneous/report/student/` directory.
VERIFY: `python3 miscellaneous/report/report.py && test -f miscellaneous/report/report.md && echo OK` → `OK`; running it a second time produces no `git diff`.

### Step 4.3: Add report.yml GitHub Action

[x] Status

CONTEXT: `.github/workflows/claude-review.yml` is the only existing workflow; branch protection on `main` (`miscellaneous/setup/instructor/repo.md` Section 2) blocks all direct pushes, including from Actions, so generated reports cannot be committed straight to `main` after a solution PR merges.
ACTION: Create `.github/workflows/report.yml`, triggered on `pull_request` `closed` events targeting `main` where `github.event.pull_request.merged == true` and the diff touches `projects/*/*/solution.md`; steps: checkout, run `python3 miscellaneous/report/report.py`, and only if `git status --porcelain miscellaneous/report` is non-empty (idempotent no-op guard), commit the changes to a new branch, `gh pr create`, then immediately `gh pr merge --squash --delete-branch` (0 approvals required by branch protection, so the merge completes without waiting).
CONSTRAINTS: Do not modify `.github/workflows/claude-review.yml` or `.github/CODEOWNERS`.
OUTPUT: New `.github/workflows/report.yml`.
VERIFY: `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/report.yml'))" && echo OK` → `OK` (live merge-trigger behavior can only be confirmed on GitHub by the instructor).

### Step 4.4: Record first two students' solutions

[x] Status

CONTEXT: `.tmp/linear_algebra_workbench_solutions/` holds 5 ungraded solution files from Aditya Sarcar (`adisarcar`) and Siddharth Kayath (`sidk256`), who worked together on all of them, submitted before the mechanism (Steps 4.1-4.3) existed; they map to 4 exercises: `thesnackbarmystery.py`→`systems_of_linear_equations`, `ptreasurewalk.py`→`scalars_vectors_matrices`, `rocketDilation.py`+`makeitlean.py`→`linear_transformations` (Parts 1 & 2), `rotationFlower.py`→`matrix_multiplication`.
ACTION: For each of the 4 exercises, create `projects/<exercise>/adisarcar/` containing: `solution.md` (Contributors: bare lines `adisarcar` and `sidk256`; Test Cases; Software Installs; Solution Manual sections), the corresponding `.py` file(s) copied from `.tmp/linear_algebra_workbench_solutions/`, and a `requirements.in` listing `numpy`/`matplotlib`.
CONSTRAINTS: Do not modify the exercises' top-level `README.md` files or any other `projects/*/` directory.
OUTPUT: 4 new `projects/<exercise>/adisarcar/` directories, each with `solution.md`, source file(s), `requirements.in`.
VERIFY: `for d in systems_of_linear_equations scalars_vectors_matrices linear_transformations matrix_multiplication; do test -f projects/$d/adisarcar/solution.md || echo "MISSING $d"; done` → no output.

### Step 4.5: Regenerate reports with the first recording

[x] Status

CONTEXT: Step 4.4 added `adisarcar`/`sidk256` submissions for 4 exercises; the reports from Step 4.2 predate them and show no completions.
ACTION: Re-run `python3 miscellaneous/report/report.py`.
CONSTRAINTS: Do not hand-edit `report.md` or any per-student report; they must be regenerated only by the script.
OUTPUT: `miscellaneous/report/report.md` shows ✅ for both `adisarcar` and `sidk256` on the 4 exercises; `miscellaneous/report/student/adisarcar-report.md` and `.../sidk256-report.md` are created, each showing ✅ against the same 4 topics.
VERIFY: `grep -c "✅" miscellaneous/report/report.md` → `8`; `ls miscellaneous/report/student/*.md | wc -l` → `2`; running `python3 miscellaneous/report/report.py` a second time produces no `git diff` (idempotency check).

### Step 4.6: Reflect mechanism into ai_workbench (edits only)

[x] Status

CONTEXT: `ai_workbench` (`../ai_workbench/`) has no student-solution submission or completion-report mechanism today; it needs the same refined design mirrored end-to-end — including that every merged solution PR (every checkin) regenerates both the class-wide `report.md` and each contributor's per-student report, not the class-wide table alone — plus a record of the change in its own `prompt_history.md`.
ACTION: In `../ai_workbench/`, add a "Submitting Exercise Solutions" README.md section mirroring Step 4.1 (adapted to ai_workbench's project/session naming), create `miscellaneous/report/report.py` + initial `miscellaneous/report/report.md` + empty `miscellaneous/report/student/` mirroring Step 4.2's refined design in full (bare-userid Contributors, GitHub-API name resolution, idempotent rewrite, and per-student report generation/update), add `.github/workflows/report.yml` mirroring Step 4.3 so it stages and commits both `miscellaneous/report/report.md` and any changed `miscellaneous/report/student/<github-userid>-report.md` files on every merged solution PR, and append a new `## Contribution Mechanism Reflected from la_workbench` entry to `../ai_workbench/miscellaneous/software_defined_workbench/prompt_history.md` explicitly listing all four refined requirements from la_workbench's Addendum (bare-userid contributors, GitHub-API name lookup, idempotency, and the per-student report generated/updated on every checkin) and referencing la_workbench's `## Contribution` section.
CONSTRAINTS: This step touches `../ai_workbench/`, a separate git repository with its own history/remote — leave all changes uncommitted and get explicit confirmation before running any `git add` / `commit` / `push` there, matching Step 1.8's precedent. Do not alter any other ai_workbench README section.
OUTPUT: Four new/updated files under `../ai_workbench/` (README.md, `miscellaneous/report/report.py`, `miscellaneous/report/report.md`, `.github/workflows/report.yml`) plus an updated `prompt_history.md` whose new entry names all four refined requirements, all left uncommitted.
VERIFY: `git -C ../ai_workbench status --porcelain` shows the changed/untracked files; `grep -ci "per-student" ../ai_workbench/miscellaneous/software_defined_workbench/prompt_history.md` → `>0`; commit/push deferred to explicit user instruction.

### Step 4.7: Mark Phase 4 complete

[x] Status

CONTEXT: Steps 4.1-4.6 are committed and verified individually (ai_workbench edits from Step 4.6 remain uncommitted pending separate confirmation, per its own constraint).
ACTION: Flip every `[ ] Status` → `[x] Status` in the Phase 4 block of this file.
CONSTRAINTS: Do not modify step content, only status lines; do not commit or push anything in `../ai_workbench/`.
OUTPUT: All Phase 4 steps show `[x] Status`.
VERIFY: `grep -A1 "### Step 4\." miscellaneous/software_defined_workbench/plan.md | grep "\[ \] Status"` → 0 matches. Commit all changed files (la_workbench only) and tag `v4.7-contribution-mechanism-step-completed`, push with `--tags`.

---

<!-- AI-GENERATED [claude-code:claude-sonnet-5]: Phase 5 (plan_history.md) -->

## Phase 5: Cleanup Contribution Mechanism (Restructure)

### Step 5.1: Move student solutions under a `solutions/` subfolder

[x] Status

CONTEXT: `projects/<exercise>/adisarcar/` (4 exercises: `systems_of_linear_equations`, `scalars_vectors_matrices`, `linear_transformations`, `matrix_multiplication`) sits directly under the exercise directory, mixing student solutions with the exercise's own `README.md`/`Help` content.
ACTION: For each of the 4 exercise directories, run `git mv projects/<exercise>/adisarcar projects/<exercise>/solutions/adisarcar`.
CONSTRAINTS: Do not move or rename the exercises' own `README.md` files; do not touch any other `projects/*/` directory.
OUTPUT: `projects/<exercise>/solutions/adisarcar/` exists for all 4 exercises; the old `projects/<exercise>/adisarcar/` path no longer exists.
VERIFY: `for d in systems_of_linear_equations scalars_vectors_matrices linear_transformations matrix_multiplication; do test -f projects/$d/solutions/adisarcar/solution.md || echo "MISSING $d"; test -d projects/$d/adisarcar && echo "STILL EXISTS $d"; done` → no output.

### Step 5.2: Rename report/ to reporting/, report.py to generate_reports.py, report.md to summary_report.md, student/ to for_each_student/

[x] Status

CONTEXT: `miscellaneous/report/report.py`, `miscellaneous/report/report.md`, and `miscellaneous/report/student/` currently hold the reporting mechanism under names the prompt wants renamed.
ACTION: `git mv miscellaneous/report miscellaneous/reporting`; then `git mv miscellaneous/reporting/report.py miscellaneous/reporting/generate_reports.py`; then `git mv miscellaneous/reporting/report.md miscellaneous/reporting/summary_report.md`; then `git mv miscellaneous/reporting/student miscellaneous/reporting/for_each_student`.
CONSTRAINTS: None beyond the four renames above — do not rename anything else under `miscellaneous/reporting/`.
OUTPUT: `miscellaneous/reporting/generate_reports.py`, `miscellaneous/reporting/summary_report.md`, `miscellaneous/reporting/for_each_student/` exist; `miscellaneous/report/` no longer exists.
VERIFY: `test -f miscellaneous/reporting/generate_reports.py && test -f miscellaneous/reporting/summary_report.md && test -d miscellaneous/reporting/for_each_student && test ! -d miscellaneous/report && echo OK` → `OK`.

### Step 5.3: Update generate_reports.py for the new paths and Full Name line

[x] Status

CONTEXT: `generate_reports.py`'s `collect_completions` still scans `projects/*/*/solution.md` (pre-move layout), it still writes `report.md` (pre-rename filename), and per-student reports lack an explicit `Full Name` line (today the full name only appears in the H1 title).
ACTION: Update `collect_completions` to scan `projects/<slug>/solutions/*/solution.md` (skip `slug`s with no `solutions/` directory yet); update `write_class_report` to write `summary_report.md` instead of `report.md`; rename the `STUDENT_DIR` target to `miscellaneous/reporting/for_each_student/`; add a `**Full Name:** <full name>` line (reusing `resolve_full_name`) immediately before `**GitHub-UserId:**` in each per-student report, keeping the existing rewrite-only-on-change idempotency guard intact.
CONSTRAINTS: Do not change the GitHub-API name-resolution logic, the class-wide report's columns/format, or the idempotency guard itself.
OUTPUT: `generate_reports.py` scans the new `solutions/` layout, writes `summary_report.md`, and every per-student report has a `Full Name` line.
VERIFY: `python3 miscellaneous/reporting/generate_reports.py && test -f miscellaneous/reporting/summary_report.md && grep -c "Full Name" miscellaneous/reporting/for_each_student/adisarcar-report.md` → `1`; running it a second time produces no `git diff` (idempotency check).

### Step 5.4: Update README.md and report.yml for the new paths

[x] Status

CONTEXT: README.md's "Submitting Exercise Solutions" section still tells students to create `projects/<exercise>/<github-userid>/` and links `miscellaneous/report/report.md` / `miscellaneous/report/student/<github-userid>-report.md`; `.github/workflows/report.yml` still filters on `projects/*/*/solution.md`, runs `miscellaneous/report/report.py`, and stages `miscellaneous/report`.
ACTION: Update README.md's submission path to `projects/<exercise>/solutions/<github-userid>/` and its links to `miscellaneous/reporting/summary_report.md` and `miscellaneous/reporting/for_each_student/<github-userid>-report.md`; update `.github/workflows/report.yml`'s diff path filter to `projects/*/solutions/*/solution.md`, its run command to `python3 miscellaneous/reporting/generate_reports.py`, and its `git status`/`git add` target to `miscellaneous/reporting`.
CONSTRAINTS: Do not modify any other README.md section or any other workflow file.
OUTPUT: README.md and `report.yml` consistently reference the new `solutions/`/`reporting/`/`generate_reports.py`/`summary_report.md`/`for_each_student/` layout.
VERIFY: `grep -c "projects/<exercise>/solutions/<github-userid>" README.md` → `1`; `grep -c "miscellaneous/reporting" README.md .github/workflows/report.yml` → both `>0`; `grep -c "projects/\*/\*/solution.md" .github/workflows/report.yml` → `0`.

### Step 5.5: Regenerate reports under the new layout

[x] Status

CONTEXT: Steps 5.1-5.4 moved/renamed everything the reporting mechanism depends on; the last-generated `report.md`/per-student reports predate the rename.
ACTION: Re-run `python3 miscellaneous/reporting/generate_reports.py`.
CONSTRAINTS: Do not hand-edit any generated report file.
OUTPUT: `miscellaneous/reporting/summary_report.md` and `miscellaneous/reporting/for_each_student/{adisarcar,sidk256}-report.md` reflect the same 4 completions as before the move, now with a `Full Name` line.
VERIFY: `grep -o "✅" miscellaneous/reporting/summary_report.md | wc -l` → `8`; `grep -c "Full Name" miscellaneous/reporting/for_each_student/sidk256-report.md` → `1`.

### Step 5.6: Reflect the restructure into ai_workbench (edits only)

[x] Status

CONTEXT: `ai_workbench` (`../ai_workbench/`) mirrors the pre-move `report`/`report.py`/`student` layout committed in the prior phase; it has no student solutions yet, so only the mechanism itself needs restructuring, plus a `prompt_history.md` record.
ACTION: In `../ai_workbench/`, apply the same restructure: `git mv miscellaneous/report miscellaneous/reporting`, `git mv miscellaneous/reporting/report.py miscellaneous/reporting/generate_reports.py`, `git mv miscellaneous/reporting/report.md miscellaneous/reporting/summary_report.md`, `git mv miscellaneous/reporting/student miscellaneous/reporting/for_each_student`; update `generate_reports.py`'s scan path to `projects/<slug>/solutions/*/solution.md`, its output filename to `summary_report.md`, and add the `Full Name` line (mirroring Step 5.3); update README.md's submission section and `.github/workflows/report.yml` to match (mirroring Step 5.4); re-run the script; append a new `## Cleanup Contribution Reflected from la_workbench` entry to `../ai_workbench/miscellaneous/software_defined_workbench/prompt_history.md` summarizing the change and referencing la_workbench's `## Cleanup Contribution` section.
CONSTRAINTS: Leave all changes uncommitted and get explicit confirmation before running any `git add`/`commit`/`push` there, matching Step 4.6's precedent. Do not alter any other ai_workbench README section.
OUTPUT: `../ai_workbench/` mirrors the new layout end-to-end, uncommitted.
VERIFY: `git -C ../ai_workbench status --porcelain` shows the changed/untracked/renamed files; `grep -ci "reporting\|generate_reports" ../ai_workbench/miscellaneous/software_defined_workbench/prompt_history.md` → `>0`; commit/push deferred to explicit user instruction.

### Step 5.7: Mark Phase 5 complete

[x] Status

CONTEXT: Steps 5.1-5.6 are committed and verified individually (ai_workbench edits from Step 5.6 remain uncommitted pending separate confirmation, per its own constraint).
ACTION: Flip every `[ ] Status` → `[x] Status` in the Phase 5 block of this file.
CONSTRAINTS: Do not modify step content, only status lines; do not commit or push anything in `../ai_workbench/`.
OUTPUT: All Phase 5 steps show `[x] Status`.
VERIFY: `grep -A1 "### Step 5\." miscellaneous/software_defined_workbench/plan.md | grep "\[ \] Status"` → 0 matches. Commit all changed files (la_workbench only) and tag `v5.7-cleanup-contribution-step-completed`, push with `--tags`.

---

<!-- AI-GENERATED [claude-code:claude-sonnet-5]: Phase 6 (plan_history.md) -->

## Phase 6: Gaussian Elimination

### Step 6.1: Commit pending student-setup script permission fix

[x] Status

CONTEXT: `miscellaneous/setup/student/labsetup.py` and `preflight_check.py` carry an uncommitted mode-only change (100644→100755, executable bit) from a prior session, unrelated to this phase's Gaussian Elimination content but blocking a clean working tree before Phase 6 work begins. ACTION: `git add miscellaneous/setup/student/labsetup.py miscellaneous/setup/student/preflight_check.py` and commit. CONSTRAINTS: Do not edit the scripts' content, only commit the existing mode change. OUTPUT: Both files committed with no working-tree diff remaining. VERIFY: `git status --porcelain -- miscellaneous/setup/student/labsetup.py miscellaneous/setup/student/preflight_check.py` → empty output.

### Step 6.2: Author the Gaussian Elimination exercise in the project README

[x] Status

CONTEXT: `projects/systems_of_linear_equations/README.md` documents only "The Snack Bar Mystery" (`np.linalg.solve`); `solutions/elimination/sidk256/gaussian_elimination.py` already solves a 6-variable system via hand-rolled elimination but no formal exercise describes this second approach. ACTION: Append a new `## Gaussian Elimination` section (Skills line, setup cell, numbered steps: hand-roll forward elimination + back-substitution on the same 2×2 snack-bar system, verify against `np.linalg.solve`, stretch goal extending to a larger system like the 6-variable example in `solutions/elimination/sidk256/`), and extend the existing `## Help` section with a validation snippet asserting the manual result matches `np.linalg.solve(A, b)`. CONSTRAINTS: Do not modify the existing "The Snack Bar Mystery" section text or its `plot_lines` helper; do not give away the elimination algorithm itself in Help, only a validation assert. OUTPUT: `projects/systems_of_linear_equations/README.md` has two exercises and an extended Help section. VERIFY: `grep -c "## Gaussian Elimination" projects/systems_of_linear_equations/README.md` → `1`; `grep -c "assert" projects/systems_of_linear_equations/README.md` → `>1`.

### Step 6.3: Update the session's Exercise section to name both exercises

[x] Status

CONTEXT: `sessions/systems_of_linear_equations.md`'s `## Exercise` section only names "The Snack Bar Mystery"; Step 6.2 added a second exercise to the same project README. ACTION: Edit the Exercise section to name and briefly describe both "The Snack Bar Mystery" (`np.linalg.solve`) and "Gaussian Elimination" (hand-rolled row reduction), still linking to the single `../projects/systems_of_linear_equations/` directory. CONSTRAINTS: Do not modify the Concept section. OUTPUT: Exercise section names both exercises. VERIFY: `grep -c "Gaussian Elimination" sessions/systems_of_linear_equations.md` → `>0`.

### Step 6.4: Document exercise-solution environment setup in dev_workbench.md

[x] Status

CONTEXT: `sessions/dev_workbench.md`'s "Run Lab Setup Script" section documents the root `.venv` created by `labsetup.py` but says nothing about activating it (or a local per-solution `.venv`) before running an exercise or solution script; `projects/systems_of_linear_equations/solutions/elimination/sidk256/solution.md` already documents a local-`.venv` option as a worked example. ACTION: Add a new subsection after "Run Lab Setup Script" (e.g. "Running Exercise Solutions") documenting: activate the repo-root `.venv` before running any exercise script, or — if a solution's `requirements.in` needs isolated installs — create a local `.venv` inside that solution's own directory instead, referencing the elimination solution above as the worked example. CONSTRAINTS: Do not modify the existing "Sign Up for Google Colab", "VSCode & Claude Code Setup", or "Run Lab Setup Script" content. OUTPUT: `sessions/dev_workbench.md` has a new subsection on environment activation before running solutions. VERIFY: `grep -ci "local .venv" sessions/dev_workbench.md` → `>0`.

### Step 6.5: Fix elimination solution.md documentation clarity

[x] Status

CONTEXT: A review of all 5 existing `solution.md` files found only `projects/systems_of_linear_equations/solutions/elimination/sidk256/solution.md` with clarity issues: a misspelling ("guassian"), a stray unmatched closing parenthesis in the Software Installs bullet, and trailing whitespace on 3 lines; the other 4 solution.md files are already clean. ACTION: Fix the spelling to "Gaussian", remove the stray `)` after `` `requirements.in` ``, and strip trailing whitespace from the affected lines. CONSTRAINTS: Do not change the Test Cases' technical description or the Solution Manual's steps beyond the typo/formatting fixes; do not touch the student's `.py` file (recorded verbatim, per Step 4.4's precedent of preserving submissions as-is). OUTPUT: `solution.md` reads cleanly, no spelling/formatting issues. VERIFY: `grep -c "guassian" projects/systems_of_linear_equations/solutions/elimination/sidk256/solution.md` → `0`; `grep -n ' $' projects/systems_of_linear_equations/solutions/elimination/sidk256/solution.md` → no output.

### Step 6.6: Redesign generate_reports.py to credit per-exercise, not per-topic

[x] Status

CONTEXT: `miscellaneous/reporting/generate_reports.py`'s `collect_completions` only finds contributors one level below a directory literally named `solutions` and collapses everything to one checkmark per session topic — so it both misses the new two-level layout `solutions/elimination/sidk256/solution.md` / `solutions/linalg/adisarcar/solution.md` (confirmed by a test run: the Systems of Linear Equations row went blank for both students; reverted before finalizing this plan) *and*, even once fixed to find them, would wrongly lump two distinct learning objectives ("The Snack Bar Mystery" via `np.linalg.solve` vs "Gaussian Elimination" via hand-rolled row reduction) into a single topic-level ✅ instead of crediting each separately. Every existing `solution.md` already opens with a `# Solution: <Title>` heading naming its exercise (verified across all 5 files), which can serve as the exercise identity without inventing a new naming scheme. ACTION: (1) Add a `SOLUTION_TITLE_RE` (`^#\s*Solution:\s*(?P<title>.+)$`) and `parse_solution_title(solution_md, default)` reading that leading heading (falls back to `default` if a solution.md lacks it); (2) change `collect_completions` to return `dict[str, dict[str, set[str]]]` (slug → exercise title → contributor userids), built via a single `rglob("solution.md")` per slug, keying each match's contributors under `parse_solution_title(solution_md, topics[slug][0])`; (3) update `write_class_report` to add an `Exercise` column between `Topic` and the userid columns, emitting one row per (slug, exercise title) pair, sorted by exercise title for determinism (or one blank-exercise row if a topic has no submissions yet); (4) update `student_table` to match: `Topic | Exercise | Concept | Completed`, one row per (slug, exercise title) pair; (5) update README.md's "Submitting Exercise Solutions" section (README.md:92-97) to document that `solution.md` must open with a `# Solution: <Exercise Title>` heading, since the report now uses it to label and credit each exercise separately. CONSTRAINTS: Do not change `parse_contributors`, `resolve_full_name`, or the rewrite-only-on-change idempotency guard in `write_student_reports`. OUTPUT: Class and per-student reports show one row per exercise (not per topic); README documents the required heading convention. VERIFY: `python3 miscellaneous/reporting/generate_reports.py && grep -c "Gaussian Elimination" miscellaneous/reporting/summary_report.md` → `1`; same grep on `miscellaneous/reporting/for_each_student/sidk256-report.md` → `1`; `grep -c "The Snack Bar Mystery" miscellaneous/reporting/for_each_student/adisarcar-report.md` → `1`; re-running the script produces no `git diff` (idempotency check).

### Step 6.7: Mark Phase 6 complete

[x] Status

CONTEXT: Steps 6.1-6.6 are committed and verified individually. ACTION: Flip every `[ ] Status` → `[x] Status` in the Phase 6 block of this file. CONSTRAINTS: Do not modify step content, only status lines. OUTPUT: All Phase 6 steps show `[x] Status`. VERIFY: `grep -A1 "### Step 6\." miscellaneous/software_defined_workbench/plan.md | grep "\[ \] Status"` → 0 matches. Commit all changed files and tag `v6.7-gaussian-elimination-step-completed`, push with `--tags`.

---

<!-- AI-GENERATED [claude-code:claude-sonnet-5]: Phase 7 (plan_history.md) -->

## Phase 7: Cleanup Solutioning

### Step 7.1: Move repo.md into a new admin/ directory

[x] Status

CONTEXT: `miscellaneous/setup/instructor/repo.md` documents branch-protection/admin GitHub settings but currently lives under `instructor/`, mixed in with generic teaching content; no `miscellaneous/setup/admin/` directory exists yet; `README.md:70` links to the current path. ACTION: `git mv miscellaneous/setup/instructor/repo.md miscellaneous/setup/admin/repo.md`; update the link in README.md's Contribution Guidelines section (README.md:70) to the new path. CONSTRAINTS: Do not edit repo.md's content beyond the move; do not touch `instructor.md`. OUTPUT: `miscellaneous/setup/admin/repo.md` exists; old path gone; README link updated. VERIFY: `test -f miscellaneous/setup/admin/repo.md && test ! -f miscellaneous/setup/instructor/repo.md && echo OK` → `OK`; `grep -c "setup/admin/repo.md" README.md` → `1`.

### Step 7.2: Author miscellaneous/setup/admin/member.md

[x] Status

CONTEXT: No doc exists for managing collaborator roles via `gh`; the prompt asks for commands to add a contributor, add a maintainer, demote maintainer→contributor, promote contributor→maintainer, plus how to check your own privilege level and what privilege the mutating commands require. ACTION: Create `miscellaneous/setup/admin/member.md`, mirroring repo.md's section-per-task style: a "check your own role" section (`gh api repos/aiedu-lab/la_workbench/collaborators/<you>/permission --jq .permission`), then the four role-change operations via `gh api -X PUT repos/aiedu-lab/la_workbench/collaborators/<username> -f permission=push|maintain`, and a note that these mutations require `admin` permission on the repo (with a link to GitHub's REST API collaborators docs). CONSTRAINTS: Do not modify repo.md or instructor.md. OUTPUT: New `miscellaneous/setup/admin/member.md`. VERIFY: `test -f miscellaneous/setup/admin/member.md && echo OK` → `OK`; `grep -c "gh api" miscellaneous/setup/admin/member.md` → `>0`.

### Step 7.3: Author miscellaneous/setup/maintainer/pull_request.md

[x] Status

CONTEXT: No doc exists for maintainer-side PR triage; the prompt asks for `gh` commands to approve, reject, and amend PRs. ACTION: Create `miscellaneous/setup/maintainer/pull_request.md` with `gh pr list`/`gh pr view` (survey), `gh pr review --approve`, `gh pr review --request-changes` (reject), and `gh pr edit` (amend title/base), matching repo.md's style. CONSTRAINTS: Document commands only — do not add automation that runs them. OUTPUT: New `miscellaneous/setup/maintainer/pull_request.md`. VERIFY: `test -f miscellaneous/setup/maintainer/pull_request.md && echo OK` → `OK`; `grep -c "gh pr review" miscellaneous/setup/maintainer/pull_request.md` → `>0`.

### Step 7.4: Clean up solution_template.md and rephrase README's step 3

[x] Status

CONTEXT: `miscellaneous/reporting/solution_template.md` (untracked, pre-existing) has typos ("guassian", "soluton", "exampl"), a garbled `## Contributors` placeholder (mismatched `<...>` brackets), and trailing whitespace; README.md's Submitting Exercise Solutions step 3 still inlines all 4 section names verbosely instead of pointing at this template. ACTION: Fix the typos/whitespace/garbled placeholder in `solution_template.md`, keeping its existing 5-section structure and order (Contributors, Summary, Solution Manual, Test Cases, Software Installs) unchanged; replace README.md's verbose inline section-list bullet under step 3 with a short instruction to copy `miscellaneous/reporting/solution_template.md` and fill in each section, keeping the `# Solution: <Title>` heading and `## Contributors` section names exactly as given. CONSTRAINTS: Do not add/remove/reorder the template's sections; do not modify the rest of step 3's numbered list. OUTPUT: Clean template; concise README step 3. VERIFY: `grep -c "guassian\|soluton\|exampl>" miscellaneous/reporting/solution_template.md` → `0`; `grep -c "solution_template.md" README.md` → `>0`.

### Step 7.5: Add solution.md validation script and pre-commit hook

[x] Status

CONTEXT: A malformed `solution.md` (missing the `# Solution: <Title>` heading, or an empty `## Contributors` section) currently reaches `main` undetected until the GitHub Action's report silently omits credit; no local guardrail exists. ACTION: Create `miscellaneous/reporting/validate_solution.py`, importing `PROJECTS_DIR`, `SOLUTION_TITLE_RE`, and `parse_contributors` from `generate_reports.py` (same directory) to check each given solution.md has a matching Solution-title line and a non-empty, placeholder-free Contributors list, printing errors to stderr and exiting non-zero on failure (scans every `solution.md` under `PROJECTS_DIR` by default when run with no args); create `.githooks/pre-commit` (executable) that runs this validator against only the staged `solution.md` files (via `git diff --cached --name-only --diff-filter=ACM`); add a `_configure_git_hooks()` step to `labsetup.py` that runs `git config core.hooksPath .githooks` so the hook activates automatically after setup; add one sentence to README's Submitting Exercise Solutions section noting solution.md is validated automatically before commit. CONSTRAINTS: Do not modify `.github/workflows/report.yml`; do not change `generate_reports.py`'s existing functions, only import from it. OUTPUT: New `validate_solution.py`; new executable `.githooks/pre-commit`; updated `labsetup.py` and README.md. VERIFY: `python3 miscellaneous/reporting/validate_solution.py` (no args, scans real tree) → exit `0`; `test -x .githooks/pre-commit && sh -n .githooks/pre-commit && echo OK` → `OK`.

### Step 7.6: Test generate_reports.py resilience against a malformed solution.md

[x] Status

CONTEXT: Step 7.5 added validation, but the reporting pipeline itself (what the GitHub Action actually runs) must also not crash if a malformed file ever slips past the hook (e.g. a direct push by a repo admin, bypassing hooks). ACTION: Temporarily add a deliberately malformed `solution.md` (no `## Contributors` section) under a scratch subdirectory inside an existing project's `solutions/` tree; run `generate_reports.py` and `validate_solution.py` to observe behavior; then remove the scratch file/directory and re-run `generate_reports.py` to confirm the repo returns to its prior, unchanged report output. CONSTRAINTS: The scratch file must not be committed; must be removed before this step's VERIFY runs. OUTPUT: Confirmed `generate_reports.py` does not crash on a malformed solution.md (it simply credits no one for that file, per `parse_contributors`'s existing empty-list behavior); `validate_solution.py` correctly flags it. No residual changes. VERIFY: after cleanup, `git status --porcelain -- projects/ miscellaneous/reporting/summary_report.md miscellaneous/reporting/for_each_student` → empty output.

### Step 7.7: Reflect Cleanup Solutioning into ai_workbench (commit, no push)

[x] Status

CONTEXT: `ai_workbench` has an equivalent `instructor/repo.md`, the same verbose README step 3, and the same `generate_reports.py` shape, but no `solution_template.md` or `.githooks/` yet; this phase's prompt explicitly authorizes committing the mirrored changes there (unlike Phases 4/5/6's "edits only" precedent) — push still left manual. ACTION: In `../ai_workbench/`, mirror Steps 7.1-7.5: move `instructor/repo.md` → `admin/repo.md` (update its README link); author `admin/member.md` and `maintainer/pull_request.md` (adjusting repo owner/name in `gh` commands); create a cleaned `solution_template.md` and rephrase its README step 3 to match; add `validate_solution.py` + `.githooks/pre-commit` + a `_configure_git_hooks()` addition to its own `labsetup.py` (follow that file's existing structure/conventions, which differ from la_workbench's simpler script); append a `## Cleanup Solutioning Reflected from la_workbench` entry to `../ai_workbench/miscellaneous/software_defined_workbench/prompt_history.md` referencing la_workbench's `## Cleanup Solutioning` section; `git add`/`git commit` in `../ai_workbench/` (no push). CONSTRAINTS: Do not push in `../ai_workbench/`; do not alter unrelated ai_workbench content; do not modify its `report.yml`. OUTPUT: `ai_workbench` mirrors the applicable Phase 7 changes, committed locally there. VERIFY: `git -C ../ai_workbench log -1 --stat` shows the new commit; `git -C ../ai_workbench status --porcelain` → clean.

### Step 7.8: Mark Phase 7 complete

[x] Status

CONTEXT: Steps 7.1-7.7 are committed and verified individually. ACTION: Flip every `[ ] Status` → `[x] Status` in the Phase 7 block of this file. CONSTRAINTS: Do not modify step content, only status lines; do not commit or push anything further in `../ai_workbench/` beyond what Step 7.7 already did. OUTPUT: All Phase 7 steps show `[x] Status`. VERIFY: `grep -A1 "### Step 7\." miscellaneous/software_defined_workbench/plan.md | grep "\[ \] Status"` → 0 matches. Commit all changed files (la_workbench only) and tag `v7.8-cleanup-solutioning-step-completed`, push with `--tags`.

---

<!-- AI-GENERATED [claude-code:claude-sonnet-5]: Phase 8 (plan_history.md) -->

## Phase 8: Pull Request

### Step 8.1: Consolidate admin/repo.md + admin/member.md into admin/admin.md

[x] Status

CONTEXT: `miscellaneous/setup/admin/` holds `repo.md` (branch-protection/CODEOWNERS/CI-secrets) and `member.md` (collaborator role management) as two separate files; the prompt asks for one `admin.md` covering both, since an admin needs both skill sets together, plus a role-validation section. ACTION: `git rm miscellaneous/setup/admin/repo.md miscellaneous/setup/admin/member.md`; create `miscellaneous/setup/admin/admin.md` combining both files' content under renumbered `## Section N` headings, prefixed with a new "Section 1 — Validate your admin role" (`gh auth status` + `gh api repos/aiedu-lab/la_workbench --jq '.permissions.admin'`) and dropping member.md's now-redundant original "check your own privilege level" section; keep member.md's trailing `## Reference` section as-is. CONSTRAINTS: Do not change repo.md's/member.md's technical content (commands, JSON payloads, expected outputs) beyond renumbering headings and removing the one redundant self-check section. OUTPUT: `miscellaneous/setup/admin/admin.md` exists with all repo-hygiene + member-management content; `repo.md`/`member.md` no longer exist. VERIFY: `test -f miscellaneous/setup/admin/admin.md && test ! -f miscellaneous/setup/admin/repo.md && test ! -f miscellaneous/setup/admin/member.md && echo OK` → `OK`; `grep -c "## Section" miscellaneous/setup/admin/admin.md` → `>0`.

### Step 8.2: Rename maintainer/pull_request.md to maintainer.md, add role validation

[x] Status

CONTEXT: `miscellaneous/setup/maintainer/pull_request.md` only covers PR review/merge; the prompt wants it renamed to `maintainer.md` (the file for "all information a maintainer should know") with an added role-validation section; its intro links `../admin/repo.md`, which Step 8.1 removed. ACTION: `git mv miscellaneous/setup/maintainer/pull_request.md miscellaneous/setup/maintainer/maintainer.md`; rename its `# Maintainer: Reviewing Pull Requests` H1 to `# Maintainer Guide`; insert a new `## Section 1 — Validate your maintainer role` (`gh auth status` + `gh api repos/aiedu-lab/la_workbench --jq '.permissions.maintain'`) before the existing PR-review sections, renumbering them 2-6; update its `../admin/repo.md` link to `../admin/admin.md`. CONSTRAINTS: Do not change the existing PR-review commands/content beyond renumbering and the link fix. OUTPUT: `miscellaneous/setup/maintainer/maintainer.md` exists with a role-validation section; old `pull_request.md` gone. VERIFY: `test -f miscellaneous/setup/maintainer/maintainer.md && test ! -f miscellaneous/setup/maintainer/pull_request.md && echo OK` → `OK`; `grep -c "admin/admin.md" miscellaneous/setup/maintainer/maintainer.md` → `1`.

### Step 8.3: Author contributor/contributor.md

[x] Status

CONTEXT: No doc exists for contributor-level `gh` commands (submitting a PR, validating contributor access); students/instructors submitting exercise solutions are GitHub "contributors" per the prompt's role taxonomy. ACTION: Create `miscellaneous/setup/contributor/contributor.md` with a "Submit a pull request" section (`gh pr create --repo aiedu-lab/la_workbench --title "projects/<project-name>/solutions/<github-userid>" --base main`) and a "Validate your contributor role" section (`gh auth status` + `gh api repos/aiedu-lab/la_workbench --jq '.permissions.push'`), matching admin.md/maintainer.md's section-per-task style. CONSTRAINTS: Do not modify the "Submitting Exercise Solutions" steps in README.md — this file is supplementary reference, not a replacement for that flow. OUTPUT: New `miscellaneous/setup/contributor/contributor.md`. VERIFY: `test -f miscellaneous/setup/contributor/contributor.md && echo OK` → `OK`; `grep -c "gh pr create" miscellaneous/setup/contributor/contributor.md` → `>0`.

### Step 8.4: Update README.md with role-clarifying note and new Guidelines sections

[x] Status

CONTEXT: README's "Contribution Guidelines" section (README.md:62-72) links the now-deleted `admin/repo.md`; no README section references the new `contributor.md`/`maintainer.md`/`admin.md`, and nothing distinguishes the Student/Instructor education roles from the Contributor/Maintainer/Admin GitHub roles. ACTION: In "Contribution Guidelines", add a short clarifying note (Student/Instructor = education roles describing how you use this course; Contributor/Maintainer/Admin = GitHub permission roles, independent of education role) and replace the `repo.md` link with a link to `contributor.md`; add two new sections after "Submitting Exercise Solutions" — "🧭 Maintainer Guidelines" linking `maintainer.md`, and "🛠️ Admin Guidelines" linking `admin.md`. CONSTRAINTS: Do not modify "Submitting Exercise Solutions", "Agenda", "Prerequisites", "Teaching Philosophy", or "Learning Outcome" sections. OUTPUT: README.md has the role-clarifying note, an updated Contribution Guidelines link, and two new Guidelines sections. VERIFY: `grep -c "setup/contributor/contributor.md" README.md` → `>0`; `grep -c "Maintainer Guidelines" README.md` → `1`; `grep -c "Admin Guidelines" README.md` → `1`; `grep -c "setup/admin/repo.md" README.md` → `0`.

### Step 8.5: Validate all file/directory references after the restructure

[x] Status

CONTEXT: Steps 8.1-8.4 moved/renamed/consolidated `admin/repo.md` + `admin/member.md` → `admin/admin.md`, `maintainer/pull_request.md` → `maintainer/maintainer.md`, and added `contributor/contributor.md`; per `prompt_history.md`'s new `### Validate` subsection, every cross-reference to these files must be checked for correctness before reflecting the restructure into `ai_workbench`. ACTION: Grep the repo for any remaining reference to the three old paths (`setup/admin/repo.md`, `setup/admin/member.md`, `setup/maintainer/pull_request.md`) outside of `plan.md`'s and `prompt_history.md`'s historical step text (which record what was true at the time and are not live links); confirm each of `admin.md`, `maintainer.md`, and `contributor.md`'s internal cross-links to each other resolve to files that actually exist. CONSTRAINTS: Do not modify `plan.md`'s or `prompt_history.md`'s historical entries — they are historical record, not live links. OUTPUT: Confirmed no dangling references anywhere in live (non-historical) content. VERIFY: `grep -rln "setup/admin/repo.md\|setup/admin/member.md\|setup/maintainer/pull_request.md" --include="*.md" . | grep -v "software_defined_workbench/plan.md\|software_defined_workbench/prompt_history.md"` → no output; `test -f miscellaneous/setup/admin/admin.md && test -f miscellaneous/setup/maintainer/maintainer.md && test -f miscellaneous/setup/contributor/contributor.md && echo OK` → `OK`.

### Step 8.6: Reflect Pull Request restructure into ai_workbench (commit, no push)

[x] Status

CONTEXT: `ai_workbench` mirrors the pre-restructure `admin/repo.md` + `admin/member.md` + `maintainer/pull_request.md` layout from Phase 7's reflection; this phase's prompt again explicitly authorizes committing the mirrored changes there — push stays manual. ACTION: In `../ai_workbench/`, mirror Steps 8.1-8.4: consolidate into `admin/admin.md`, rename+extend `maintainer/maintainer.md`, add `contributor/contributor.md` (adjusting repo owner/name in `gh` commands to `aiedu-lab/ai_workbench`), and update its README with the same role-clarifying note + Contributor/Maintainer/Admin Guidelines sections; append a `## Pull Request Reflected from la_workbench` entry to `../ai_workbench/miscellaneous/software_defined_workbench/prompt_history.md`; `git add`/`git commit` in `../ai_workbench/` (no push). CONSTRAINTS: Do not push in `../ai_workbench/`; do not alter unrelated ai_workbench content. OUTPUT: `ai_workbench` mirrors the Phase 8 restructure, committed locally there. VERIFY: `git -C ../ai_workbench log -1 --stat` shows the new commit; `git -C ../ai_workbench status --porcelain` → clean.

### Step 8.7: Mark Phase 8 complete

[x] Status

CONTEXT: Steps 8.1-8.6 are committed and verified individually. ACTION: Flip every `[ ] Status` → `[x] Status` in the Phase 8 block of this file. CONSTRAINTS: Do not modify step content, only status lines; do not commit or push anything further in `../ai_workbench/` beyond what Step 8.6 already did. OUTPUT: All Phase 8 steps show `[x] Status`. VERIFY: `grep -A1 "### Step 8\." miscellaneous/software_defined_workbench/plan.md | grep "\[ \] Status"` → 0 matches. Commit all changed files (la_workbench only) and tag `v8.7-pull-request-roles-step-completed`, push with `--tags`.

---

<!-- AI-GENERATED [claude-code:claude-sonnet-5]: Phase 9 (plan_history.md) -->

## Phase 9: Test One

### Step 9.1: Author the "Scalars to Linear Equations" test

[x] Status

CONTEXT: No `tests/` directory exists yet; Agenda rows 3-7 (`scalars_vectors_matrices.md` through `systems_of_linear_equations.md`) cover the concept range the prompt asks to test — vectors, distance/similarity, linear transformations, matrix multiplication, systems of equations. ACTION: Create `tests/test-scalars-to-linear-equations.md`: an intro paragraph stating the 1-hour time box, that collaboration is encouraged, and that for each question students must mark the correct option(s) and write a ≤100-word explanation of the concept/approach/visual intuition used; then 12 MCQ questions (`**Q1.**`-`**Q12.**`, each labeled `_(Basic)_`/`_(Medium)_`/`_(High)_`, 4 of each, options `A.`-`D.` with one or more correct), conceptual/visual-intuition focused, no heavy numerical computation. CONSTRAINTS: Do not include AP Calculus content; do not create the solutions file yet (Step 9.2); do not modify any session/project file. OUTPUT: New `tests/test-scalars-to-linear-equations.md` with 12 labeled questions. VERIFY: `grep -c "^\*\*Q" tests/test-scalars-to-linear-equations.md` → `12`.

### Step 9.2: Author the solution key for the Linear Algebra test

[x] Status

CONTEXT: Step 9.1 created the 12-question test; no answer key exists. ACTION: Create `tests/solutions/soln-scalars-to-linear-equations.md` mirroring the test's `**Q1.**`-`**Q12.**` numbering; for each, state the correct option letter(s) plus a ≤100-word reference explanation of the concept/approach/visual intuition. CONSTRAINTS: Do not modify `test-scalars-to-linear-equations.md`; keep every explanation ≤100 words. OUTPUT: New `tests/solutions/soln-scalars-to-linear-equations.md`. VERIFY: `grep -c "^\*\*Q" tests/solutions/soln-scalars-to-linear-equations.md` → `12`.

### Step 9.3: Wire the Linear Algebra test into the Agenda

[x] Status

CONTEXT: README.md's Agenda table (README.md:16-34) numbers topic rows 1-16; `Systems of Linear Equations` is row 7; the prompt asks for the test to appear immediately after it, cross-linking both the test and its solution. ACTION: Insert a new `–`-numbered Agenda row immediately after row 7, titled `Test: Scalars to Linear Equations`, linking `tests/test-scalars-to-linear-equations.md`, with its solution linked in the same row's `Why it Matters` cell as `([solution](tests/solutions/soln-scalars-to-linear-equations.md))`. CONSTRAINTS: Do not renumber or reword any existing row (1-16 stay as-is). OUTPUT: README.md Agenda has one new `–` row between rows 7 and 8, linking both files. VERIFY: `grep -c "tests/test-scalars-to-linear-equations.md\|tests/solutions/soln-scalars-to-linear-equations.md" README.md` → `2`.

### Step 9.4: Author the AP Calculus BC test

[x] Status

CONTEXT: The approved prompt asks for a second test spanning AP Calculus BC Units 1-5 (Limits/Continuity through Analytical Applications of Differentiation) per the College Board course description, justified as calculus underlying parts of the LA/AI curriculum even though it isn't itself a Linear Algebra topic. ACTION: Create `tests/test-limits-continuity-to-analytical-apps-of-diff.md` in the same format as Step 9.1 (intro paragraph, 12 `**Q1.**`-`**Q12.**` questions, 4 Basic/4 Medium/4 High, options `A.`-`D.`), scoped to AP Calculus BC Units 1-5 only, conceptual/visual-intuition focused. CONSTRAINTS: Do not include Units 6-10 (BC-exclusive integration/series topics); do not modify the Linear Algebra test files. OUTPUT: New `tests/test-limits-continuity-to-analytical-apps-of-diff.md` with 12 labeled questions. VERIFY: `grep -c "^\*\*Q" tests/test-limits-continuity-to-analytical-apps-of-diff.md` → `12`.

### Step 9.5: Author the solution key for the AP Calculus BC test

[x] Status

CONTEXT: Step 9.4 created the 12-question Calculus test; no answer key exists. ACTION: Create `tests/solutions/soln-limits-continuity-to-analytical-apps-of-diff.md` mirroring the test's numbering, each with the correct option letter(s) plus a ≤100-word reference explanation. CONSTRAINTS: Do not modify `test-limits-continuity-to-analytical-apps-of-diff.md`; keep every explanation ≤100 words. OUTPUT: New `tests/solutions/soln-limits-continuity-to-analytical-apps-of-diff.md`. VERIFY: `grep -c "^\*\*Q" tests/solutions/soln-limits-continuity-to-analytical-apps-of-diff.md` → `12`.

### Step 9.6: Wire the AP Calculus BC test into the Agenda with an LA-connection note

[x] Status

CONTEXT: Step 9.3 inserted the Linear Algebra test as a `–` row after row 7; per the prompt this second test belongs immediately after that row, and per the user's clarification it must carry a short note explaining why a Calculus test appears in a Linear-Algebra course. ACTION: Insert a new `–`-numbered Agenda row immediately after the Linear Algebra test row, titled `Test: AP Calculus BC (Units 1-5)`, linking `tests/test-limits-continuity-to-analytical-apps-of-diff.md` with its solution linked the same way as Step 9.3 (`([solution](tests/solutions/soln-limits-continuity-to-analytical-apps-of-diff.md))`); its `Why it Matters` cell must note that differential calculus (limits, derivatives) underlies Linear-Algebra-adjacent AI machinery — projection-matrix derivations, multivariable Taylor expansions, and gradient-based error minimization in ML/DL training. CONSTRAINTS: Do not alter the wording of any other Agenda row. OUTPUT: README.md Agenda has a second new `–` row, cross-linking both Calculus test files and carrying the LA-connection note. VERIFY: `grep -c "tests/test-limits-continuity-to-analytical-apps-of-diff.md\|tests/solutions/soln-limits-continuity-to-analytical-apps-of-diff.md" README.md` → `2`; `grep -ci "gradient\|projection\|taylor" README.md` → `>0`.

### Step 9.7: Mark Phase 9 complete

[x] Status

CONTEXT: Steps 9.1-9.6 are committed and verified individually. ACTION: Flip every `[ ] Status` → `[x] Status` in the Phase 9 block of this file. CONSTRAINTS: Do not modify step content, only status lines. OUTPUT: All Phase 9 steps show `[x] Status`. VERIFY: `grep -A1 "### Step 9\." miscellaneous/software_defined_workbench/plan.md | grep "\[ \] Status"` → 0 matches. Commit all changed files and tag `v9.7-test-one-step-completed`, push with `--tags`.

---

<!-- AI-GENERATED [claude-code:claude-sonnet-5]: Phase 10 (plan_history.md) -->

## Phase 10: Single-Variable Calculus & Partial Derivatives

### Step 10.1: Author sessions/single_variable_calculus.md

[x] Status

CONTEXT: No such session exists; the prompt asks for an intuition-building session on single-variable functions and optimization, positioned immediately before the new Partial Derivatives session so students generalize from one variable to several. ACTION: Create `sessions/single_variable_calculus.md` with a Concept section covering: a function `y = f(x)` and its derivative `f'(x)` as the slope/rate of change; using `f'(x) = 0` to find critical points and `f''(x)`'s sign to classify them as a min or max; and framing the derivative as a 1D "gradient" that points downhill/uphill, the seed idea `gradients_backpropagation.md` later generalizes; an Exercise section linking `../projects/single_variable_calculus/`. Use ASCII-art diagrams where helpful (e.g. a simple curve sketch), not Mermaid; no `## Reference` section (no matching 18.02 lecture — that course is multivariable-only). CONSTRAINTS: Do not modify `gradients_backpropagation.md` or any other existing session; no Mermaid diagrams. OUTPUT: New `sessions/single_variable_calculus.md`, no TODO markers. VERIFY: `grep -c "TODO" sessions/single_variable_calculus.md` → `0`.

### Step 10.2: Author the single-variable paper-and-code exercise

[x] Status

CONTEXT: No `projects/single_variable_calculus/` exists; the exercise must mirror `projects/column_space_rank/README.md`'s template and include a paper problem, a curve-visualization coding exercise, and a gradient-descent-style minimum-finder in 1D that the later Partial Derivatives exercise generalizes to 2D. ACTION: Create `projects/single_variable_calculus/README.md`: a paper problem using `f(x) = x^2 - 4x + 3` asking students to hand-compute `f'(x)`, solve `f'(x) = 0` for the critical point `x = 2`, and confirm via `f''(x) = 2 > 0` that it is a minimum; a coding section that plots the curve, marks the critical point, confirms `f'(2) ≈ 0` and `f''(2) > 0` numerically (e.g. via finite differences or `np.gradient`), and implements a small 1D gradient-descent loop (`x = x - lr * f'(x)`) that converges to `x ≈ 2` from a different starting point; a `## Help` section with a `plot_curve_with_point(f, xr, x_star)` helper and `assert` checks for the derivative-zero, second-derivative-sign, and gradient-descent-convergence claims. CONSTRAINTS: Keep the exercise toy/basic; do not touch any other `projects/*` directory. OUTPUT: New `projects/single_variable_calculus/README.md` with paper-problem, coding, and Help sections. VERIFY: `grep -c "## Help" projects/single_variable_calculus/README.md` → `1`; `grep -c "assert" projects/single_variable_calculus/README.md` → `>0`.

### Step 10.3: Author sessions/partial_derivatives_multivariate_calculus.md

[x] Status

CONTEXT: No such session exists; `.tmp/partial_derivatives_and_multivariate_calculus.md` holds prior draft content (ASCII diagrams) introducing partial derivatives, the total differential, and the gradient as a vector whose dot product with a direction gives the total differential — groundwork the prompt explicitly defers using for Taylor expansion and gradient-based error minimization in later phases; MIT 18.02 *Multivariable Calculus* (Fall 2007)'s Lectures 8-12 map onto exactly this content (partial derivatives/tangent plane, max-min problems, the second-derivative test, differentials/chain rule, gradient/directional derivative). ACTION: Create `sessions/partial_derivatives_multivariate_calculus.md` with a Concept section adapting the `.tmp` file's content and its ASCII-art diagrams as-is (partial derivative = freeze one variable and measure slope; total derivative = both vary at once; the gradient `∇f` collects the partials into a vector; the total differential `dz = ∇f · dx` is a dot product); a `## Reference` section linking the [18.02 video gallery](https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/video_galleries/video-lectures/) and naming Lectures 8-12 with their topics; an Exercise section linking `../projects/partial_derivatives_multivariate_calculus/`. CONSTRAINTS: Do not modify `.tmp/partial_derivatives_and_multivariate_calculus.md` or `sessions/gradients_backpropagation.md`; keep the ASCII diagrams, do not convert to Mermaid. OUTPUT: New `sessions/partial_derivatives_multivariate_calculus.md`, no TODO markers, with a populated `## Reference` section. VERIFY: `grep -c "TODO" sessions/partial_derivatives_multivariate_calculus.md` → `0`; `grep -c "## Reference" sessions/partial_derivatives_multivariate_calculus.md` → `1`; `grep -c "18-02-multivariable-calculus" sessions/partial_derivatives_multivariate_calculus.md` → `>0`.

### Step 10.4: Author the partial-derivatives paper-and-code exercise

[x] Status

CONTEXT: No `projects/partial_derivatives_multivariate_calculus/` exists; the prompt asks for a paper problem plus a `np.linalg`-based coding exercise on a 2-variable `f(x, y)` with `y = g(x)` showing the chain rule matches direct substitution, code that visualizes the function including frozen-variable slices, and a max/min-via-partial-derivatives section — following `projects/column_space_rank/README.md`'s template as the named reference. ACTION: Create `projects/partial_derivatives_multivariate_calculus/README.md`: (1) a paper problem using `f(x, y) = x^2 + x*y` with `y = g(x) = 3x - 2` asking students to hand-compute `∂f/∂x`, `∂f/∂y`, the gradient, and `df/dx` both via the chain rule and via direct substitution into `h(x) = f(x, g(x))` (both simplify to `8x - 2`); (2) a coding section that visualizes `f(x, y)` (contour or surface plot) plus two slice plots — `y` frozen while `x` varies, and `x` frozen while `y` varies — to make the partial derivatives visually concrete, and confirms the chain-rule/direct-substitution match numerically, using `np.linalg.norm` for the gradient's steepness magnitude and a dot product for `∇f · dx`; (3) a short "Finding Max/Min via Partial Derivatives" section using the separate simple example `f(x, y) = x^2 + y^2`, showing the critical point where `∇f = (0, 0)` at `(0, 0)` is a minimum; (4) a `## Help` section with plotting helper(s) (e.g. `plot_function_and_slices(f, xr, yr, x0, y0)`) and `assert` checks for the chain-rule/direct-substitution match and the max/min critical point. CONSTRAINTS: Keep the exercise toy/basic; do not touch any other `projects/*` directory. OUTPUT: New `projects/partial_derivatives_multivariate_calculus/README.md` with paper-problem, coding (incl. slice visualizations), max/min, and Help sections. VERIFY: `grep -c "## Help" projects/partial_derivatives_multivariate_calculus/README.md` → `1`; `grep -c "assert" projects/partial_derivatives_multivariate_calculus/README.md` → `>1`; `grep -ci "max/min\|max-min" projects/partial_derivatives_multivariate_calculus/README.md` → `>0`.

### Step 10.5: Wire both new sessions into the Agenda before Column Space, Rank

[x] Status

CONTEXT: README.md's Agenda numbers topic rows 1-16 (Phase 9's `–`-numbered test rows are unaffected); `Column Space, Rank and Linear Independence` is row 8; both new sessions belong immediately before it, in order (Single-Variable Calculus, then Partial Derivatives). ACTION: Insert two new numbered Agenda rows — row 8 for `Single-Variable Calculus` (linking the new session) and row 9 for `Partial Derivatives and Multivariate Calculus` (linking the other new session) — renumbering existing rows 8-16 to 10-18; both new rows' `Why it Matters`/`Real-World Motivation`/`AI Connection` cells describe optimization via derivatives, generalizing to the gradient, as groundwork for Taylor expansion and gradient-based error minimization, previewing rather than duplicating `gradients_backpropagation.md`. CONSTRAINTS: Do not renumber or alter the `–`-numbered test rows from Phase 9; do not reword any existing row beyond the renumbering and the two new rows. OUTPUT: README.md Agenda has 18 numbered rows (was 16); new rows 8-9 link the two new sessions. VERIFY: `grep -c "sessions/single_variable_calculus.md\|sessions/partial_derivatives_multivariate_calculus.md" README.md` → `2`; `grep -c "^| 18 " README.md` → `1`.

### Step 10.6: Mark Phase 10 complete

[ ] Status

CONTEXT: Steps 10.1-10.5 are committed and verified individually. ACTION: Flip every `[ ] Status` → `[x] Status` in the Phase 10 block of this file. CONSTRAINTS: Do not modify step content, only status lines. OUTPUT: All Phase 10 steps show `[x] Status`. VERIFY: `grep -A1 "### Step 10\." miscellaneous/software_defined_workbench/plan.md | grep "\[ \] Status"` → 0 matches. Commit all changed files and tag `v10.6-single-var-partial-derivatives-step-completed`, push with `--tags`.

---
