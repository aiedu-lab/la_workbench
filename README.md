# Linear Algebra for AI - Workbench

> **Objective:** Build an intuitive understanding of linear algebra so students are prepared for Gilbert Strang's MIT lectures, 3Blue1Brown's *Essence of Linear Algebra*, and modern AI topics such as embeddings, inference, attention, and neural network training.

> **Companion Repository:** This lab is independent of
> [AI Workbench](https://github.com/aiedu-lab/ai_workbench), but the
> two are designed to be taken together. Linear Algebra is the
> engine under AI Workbench's exercises — grokking vectors,
> matrices, and transformations here is what turns AI Workbench's
> often-abstract AI concepts (embeddings, inference, attention,
> training) into something you can see and reason about.

## Agenda

| #  | Lesson                                                    | Why it Matters                                                                                                       | Real-World Motivation                                                                      | AI Connection                                                                                |
| -- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| –  | [**Introduction**](sessions/introduction.md)               | Orient to the course arc, tools, and how Linear Algebra connects to AI.                                              | —                                                                                            | —                                                                                              |
| –  | [**Development Workbench Setup**](sessions/dev_workbench.md) | Install and verify Python, NumPy, PyTorch, and Jupyter before lab day.                                                | —                                                                                            | —                                                                                              |
| 1  | [**What is a Model?**](sessions/what_is_a_model.md)        | A model is simply a function that maps inputs to outputs. This is the central idea behind machine learning.          | House features → price, email → spam/not spam, image → object label, sentence → next word. | Neural networks are mathematical models that learn these mappings from data.                 |
| 2  | [**Why Linear Algebra?**](sessions/why_linear_algebra.md)  | Computers process numbers. Linear algebra provides a compact language for representing and transforming information. | Images become pixels, music becomes samples, text becomes numbers.                         | Every modern AI model represents information using vectors and matrices.                     |
| 3  | [**Scalars, Vectors and Matrices**](sessions/scalars_vectors_matrices.md) | Learn the vocabulary of linear algebra: scalars, vectors as points/directions, and matrices, plus the operations (addition, scaling) that combine them. | GPS coordinates, RGB colors, shopping lists, spreadsheets, walking across a city, wind velocity, combining forces, adjusting image brightness. | Tokens become vectors, datasets become matrices, embeddings represent words/images/users as vectors, and feature weighting relies on vector addition/scaling. |
| 4  | [**Distance, Length and Similarity**](sessions/distance_length_similarity.md) | Learn how to measure closeness between vectors.                                                                      | Finding similar songs, recommending products, searching documents.                         | Embeddings, cosine similarity, semantic search and recommendation systems.                   |
| 5  | [**Linear Transformations**](sessions/linear_transformations.md) | A matrix is best viewed as a transformation rather than a table of numbers.                                          | Rotating maps, resizing images, changing camera perspectives.                              | Every neural network layer transforms one vector into another.                               |
| 6  | [**Matrix Multiplication**](sessions/matrix_multiplication.md) | Multiple transformations can be composed into one.                                                                   | Factory assembly lines where each station performs one operation.                          | Forward propagation through neural networks and transformers.                                |
| 7  | [**Systems of Linear Equations**](sessions/systems_of_linear_equations.md) | Solve many unknowns simultaneously.                                                                                  | Balancing finances, electrical circuits, logistics planning.                               | Regression, optimization and parameter estimation.                                           |
| –  | [**Test: Scalars to Linear Equations**](tests/test-scalars-to-linear-equations.md) | A 12-question conceptual quiz covering rows 3-7 above ([solution](tests/solutions/soln-scalars-to-linear-equations.md)). | —                                                                                            | —                                                                                              |
| –  | [**Test: AP Calculus BC (Units 1-5)**](tests/test-limits-continuity-to-analytical-apps-of-diff.md) | A 12-question conceptual quiz on differential calculus ([solution](tests/solutions/soln-limits-continuity-to-analytical-apps-of-diff.md)). Differential calculus is the engine under several Linear-Algebra-adjacent AI tools: it derives projection matrices, underlies multivariable Taylor expansions, and drives gradient-based error minimization in ML/DL training. | —                                                                                            | —                                                                                              |
| 8  | [**Single-Variable Calculus**](sessions/single_variable_calculus.md) | A derivative reveals a curve's slope; setting it to zero finds where the curve bottoms out or peaks.                 | Finding the lowest point in a valley, or the peak of a thrown ball's arc.                  | The one-variable rehearsal for gradient descent, generalized to every model parameter later. |
| 9  | [**Partial Derivatives and Multivariate Calculus**](sessions/partial_derivatives_multivariate_calculus.md) | Functions of several inputs need one partial derivative per input; the gradient collects them into a single vector. | Reading a topographic map: which direction from here climbs fastest, and how steep is it?  | The gradient powers gradient-based error minimization and the first-order term of a Taylor expansion. |
| 10 | [**Parameterization**](sessions/parameterization.md) | A multivariable problem with several degrees of freedom can be walked one direction at a time, turning it into a family of ordinary single-variable problems. | Tracing a hiking trail across a mountainside, or animating a camera path through a 3D scene. | Exploring a model's loss surface one direction at a time is the same parameterized-path idea used to probe training dynamics. |
| 11 | [**Critical Points and the Second Derivative Test**](sessions/critical_points.md) | A flat point (zero gradient) could be a minimum, a maximum, or a saddle — the second-derivative test tells them apart. | Reaching the bottom of a valley versus getting stuck on a mountain pass or a false summit. | Distinguishing a true minimum from a saddle point in a model's loss landscape — training that actually converged versus training that merely stalled. |
| 12 | [**Vector Calculus**](sessions/vector_calculus.md) | Gradient, divergence, and curl are the three fundamental ways a scalar or vector field can change from point to point. | Mapping electric and gravitational fields, detecting edges in images, tracking fluid flow and rotation. | Gradient descent walks downhill using exactly the gradient introduced here — the same tool, one more time. |
| 13 | [**Column Space, Rank and Linear Independence**](sessions/column_space_rank.md) | Determine whether information is unique or redundant.                                                                | Multiple sensors measuring the same quantity.                                              | Model capacity, feature redundancy and dimensionality reduction.                             |
| 14 | [**Basis and Change of Basis**](sessions/basis_change_of_basis.md) | The same object can be represented using different coordinate systems.                                               | GPS coordinates vs local street maps.                                                      | Feature spaces, latent representations and embeddings.                                       |
| 15 | [**Orthogonality and Projections**](sessions/orthogonality_projections.md) | Separate signal from noise and find the best approximation.                                                          | Noise-cancelling headphones, shadows, least-error fitting.                                 | Least squares, PCA, attention and regression.                                                |
| 16 | [**Eigenvectors and Eigenvalues (Conceptual)**](sessions/eigenvectors_eigenvalues.md) | Some directions remain unchanged by a transformation.                                                                | Vibrating bridges, Google's PageRank, principal directions in data.                        | PCA, diffusion models and model stability.                                                   |
| 17 | [**High-Dimensional Geometry**](sessions/high_dimensional_geometry.md) | AI routinely works in spaces with hundreds or thousands of dimensions.                                               | Customer profiles, genomes, recommendation systems.                                        | Embeddings with hundreds or thousands of dimensions.                                         |
| 18 | [**Embeddings: Representing Meaning as Vectors**](sessions/embeddings.md) | Similar objects should have nearby vector representations.                                                           | "King" is closer to "Queen" than to "Pizza."                                               | Word embeddings, image embeddings, Retrieval-Augmented Generation (RAG) and semantic search. |
| 19 | [**Forward Propagation (Inference)**](sessions/forward_propagation.md) | Information flows through a sequence of linear transformations and nonlinearities to produce predictions.            | A manufacturing pipeline that gradually transforms raw materials into a finished product.  | Neural network inference, transformers and large language models.                            |
| 20 | [**Learning from Mistakes: Gradients and Backpropagation**](sessions/gradients_backpropagation.md) | Models improve by measuring prediction error and adjusting parameters in the direction that reduces it.              | Learning to throw darts by correcting each miss.                                           | Gradient descent, backpropagation and neural network training.                               |
| 21 | [**Kaggle Titanic Capstone**](sessions/kaggle_titanic_capstone.md) | Apply every concept from this course to train one real model end-to-end, on real data.                              | Predicting survival from passenger records — a classic intro classification dataset.       | Ties together vectors, transformations, systems of equations, and gradient-based training.   |

---

## Prerequisites

* High-school algebra
* Cartesian coordinates
* Basic graphing
* Functions

No calculus is required until the final lesson on backpropagation, where only the intuition behind derivatives is introduced.

---

## Teaching Philosophy

Each lesson follows the same structure:

1. **Start with a real-world problem.**
2. **Explain why the problem is difficult.**
3. **Introduce the mathematical idea that solves it.**
4. **Visualize the concept whenever possible.**
5. **Connect it to modern AI.**
6. **Reinforce the idea with a short NumPy or PyTorch exercise.**

---

## 🤝 Contribution Guidelines

> **Note:** "Student" and "Instructor" ([dev_workbench.md](
> sessions/dev_workbench.md) /
> [instructor.md](miscellaneous/setup/instructor/instructor.md))
> are *education* roles describing how you use this course.
> "Contributor", "Maintainer", and "Admin" below are *GitHub*
> roles describing your repo permissions — an instructor is often
> also a GitHub admin, but doesn't have to be, and the two are
> independent.

All content changes flow through a branch + pull request — no one
commits directly to `main`. Branch protection is configured so that
write-access contributors (including the instructor) do **not** need
a separate reviewer to merge their own PR; a PR is required, but
zero additional approvals are needed.

See [contributor.md](miscellaneous/setup/contributor/contributor.md)
for the `gh` commands to submit a pull request and validate your
contributor access.

---

## 📤 Submitting Exercise Solutions

Once you've completed an exercise or a set of exercises, submit it 
so it becomes a durable record of your work.

1. Ensure you've the latest mainline branch:
   `git switch main && git pull origin main`
2. Create (or Switch to) a branch off of main where you'll make the changes:
   `git switch --create solutions-branch 2>/dev/null || git switch solutions-branch`
3. Create projects/<project-name>/solutions/<github-userid>/ —
   <project-name> is the matching project subfolder for the session
   (e.g. projects/embedding/), and <github-userid> is any one member's
   GitHub user id if you worked in a group. Inside it, add:
   * solution.md — copy [solution_template.md](
       miscellaneous/reporting/solution_template.md
     ) and fill in each section. Keep the `# Solution: <Title>`
     heading and section names exactly as given; the completion
     report depends on them to label and credit your work.
   * your file(s):
     * requirements.in (or equivalent) for any extra installs
     * all source files

   `labsetup.py` wires up a pre-commit hook that validates
   solution.md automatically, rejecting the commit if the heading
   or Contributors section is missing or malformed.
3. If you have spent a lot of time and submitting multiple solutions,
   then prior to pushing your solution to origin please ensure you've
   the latest version or origin/main: `git rebase origin/main`
4. Push your changes to origin: `git push origin solutions-branch`
5. Open a pull request named `projects/<project-name>/solutions/<github-userid>`.
6. Once the maintainer approves and merges your PR,
   [`.github/workflows/report.yml`](.github/workflows/report.yml)
   automatically regenerates [`summary_report.md`](
   miscellaneous/reporting/summary_report.md) (the whole class's
   completion record) and each contributor's own
   `miscellaneous/reporting/for_each_student/<github-userid>-report.md`
   — no manual step needed.

---

## 🧭 Maintainer Guidelines

Reviewing and merging pull requests is a maintainer's job. See
[maintainer.md](miscellaneous/setup/maintainer/maintainer.md) for
the full `gh` command reference.

---

## 🛠️ Admin Guidelines

Repo hygiene (branch protection, CODEOWNERS, CI secrets) and
collaborator-role management are admin tasks. See
[admin.md](miscellaneous/setup/admin/admin.md) for the full `gh`
command reference.

### Repo Tooling

`tools/scripts/repo_utils/` provides four gh-backed PR commands, all
sharing auth/permission and clean-branch preflight logic via
`_pr_utils.py`; see each script's own docstring for its exact
guarantee.

| Script | Purpose | Example |
|---|---|---|
| `check_pr` | Read-only: reports state/checks/review-decision, exits 0 only if the PR looks mergeable right now | `bazel run //:check_pr -- <PR#>` |
| `submit_pr` | Pushes the current branch and opens a PR | `bazel run //:submit_pr -- --title "..." --body "..." --base main --draft` |
| `approve_pr` | Approves a PR (never your own -- GitHub rejects self-approval) | `bazel run //:approve_pr -- <PR#> --body "..."` |
| `merge_pr` | Merges a PR only after confirming checks passed and any required review is satisfied (retries with `--admin` when review is required but exempt via branch protection) | `bazel run //:merge_pr -- <PR#> --method squash --delete-branch` |

`.claude/skills/` chains these into two gated pipelines (never
auto-invoked -- always an explicit, human-triggered decision):

| Skill | Chain |
|---|---|
| `pr_submit_plugin` | branch/tree hook → build+test+container-tests (stub) → `//:pr_check` (act) → `//:submit_pr` → confirm-exists hook |
| `pr_merge_plugin` | wait-for-checks hook → `//:merge_pr` (`--delete-branch` optional) → confirm-merged hook |

See each skill's `skill.md` for exact invocation and flags.
Preferred entry points: `/check_pr <PR#>` and `/check_prs`
(read-only), `/pr_submit` (drafts the title/body from the
branch's actual content, then runs the submit chain),
`/pr_approve` (MAINTAIN/ADMIN only), and `/pr_merge` (WRITE+,
gated on checks passing and review
satisfied/not-required/admin-exempt) -- see
`.claude/commands/{check_pr,check_prs,pr_submit,pr_approve,
pr_merge}.md` for each one's exact scope.

`pr_check.py` passes `act` `--reuse` (keep the job container
between runs instead of removing it) to avoid a container-removal
timeout on Docker Desktop's WSL2 backend -- see `pr_check.py`'s
own comment. Run `docker container prune` occasionally to
reclaim the containers this leaves behind. If the WSL2/Docker
flakiness itself is blocking you (or you know a change doesn't
need a full local act run -- docs/skill-only, say), `touch
.pr_check_skip` at the repo root to skip `act` entirely (exit 0
immediately, no Docker call at all); `rm .pr_check_skip` to
re-enable. Git-ignored, local-machine-only, and only skips the
local act simulation -- real GitHub Actions CI still runs
pr-validation.yaml on every actual push/PR regardless. All 5
repos, including ITDev, support this the same way.
`.claude/skills/model_modernizer/` reports the current model vs.
the latest and recommends only, never auto-switches.

**Cross-repo consistency:** this tooling is intentionally duplicated
(not symlinked) across every sister repo -- ITDev, aim, personal,
ai_workbench, la_workbench. Any change here must be ported to the
same path in every other repo; see each script's own "Sync note".

---

## Learning Outcome

By the end of this course, students should be able to explain:

* What a machine learning model is and how it differs from a traditional program.
* Why vectors are an effective representation of information.
* Why embeddings capture semantic similarity.
* Why cosine similarity is widely used.
* Why a neural network layer is a matrix transformation.
* Why inference consists primarily of repeated matrix multiplication and nonlinear activation functions.
* Why backpropagation computes gradients efficiently.
* Why GPUs and TPUs are optimized for matrix operations.
* How these concepts prepare them for the mathematics presented in Gilbert Strang's lectures and the geometric intuition developed in 3Blue1Brown's *Essence of Linear Algebra*.
