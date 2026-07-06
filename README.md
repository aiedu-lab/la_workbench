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
| 8  | [**Column Space, Rank and Linear Independence**](sessions/column_space_rank.md) | Determine whether information is unique or redundant.                                                                | Multiple sensors measuring the same quantity.                                              | Model capacity, feature redundancy and dimensionality reduction.                             |
| 9  | [**Basis and Change of Basis**](sessions/basis_change_of_basis.md) | The same object can be represented using different coordinate systems.                                               | GPS coordinates vs local street maps.                                                      | Feature spaces, latent representations and embeddings.                                       |
| 10 | [**Orthogonality and Projections**](sessions/orthogonality_projections.md) | Separate signal from noise and find the best approximation.                                                          | Noise-cancelling headphones, shadows, least-error fitting.                                 | Least squares, PCA, attention and regression.                                                |
| 11 | [**Eigenvectors and Eigenvalues (Conceptual)**](sessions/eigenvectors_eigenvalues.md) | Some directions remain unchanged by a transformation.                                                                | Vibrating bridges, Google's PageRank, principal directions in data.                        | PCA, diffusion models and model stability.                                                   |
| 12 | [**High-Dimensional Geometry**](sessions/high_dimensional_geometry.md) | AI routinely works in spaces with hundreds or thousands of dimensions.                                               | Customer profiles, genomes, recommendation systems.                                        | Embeddings with hundreds or thousands of dimensions.                                         |
| 13 | [**Embeddings: Representing Meaning as Vectors**](sessions/embeddings.md) | Similar objects should have nearby vector representations.                                                           | "King" is closer to "Queen" than to "Pizza."                                               | Word embeddings, image embeddings, Retrieval-Augmented Generation (RAG) and semantic search. |
| 14 | [**Forward Propagation (Inference)**](sessions/forward_propagation.md) | Information flows through a sequence of linear transformations and nonlinearities to produce predictions.            | A manufacturing pipeline that gradually transforms raw materials into a finished product.  | Neural network inference, transformers and large language models.                            |
| 15 | [**Learning from Mistakes: Gradients and Backpropagation**](sessions/gradients_backpropagation.md) | Models improve by measuring prediction error and adjusting parameters in the direction that reduces it.              | Learning to throw darts by correcting each miss.                                           | Gradient descent, backpropagation and neural network training.                               |
| 16 | [**Kaggle Titanic Capstone**](sessions/kaggle_titanic_capstone.md) | Apply every concept from this course to train one real model end-to-end, on real data.                              | Predicting survival from passenger records — a classic intro classification dataset.       | Ties together vectors, transformations, systems of equations, and gradient-based training.   |

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

All content changes flow through a branch + pull request — no one
commits directly to `main`. Branch protection is configured so that
write-access contributors (including the instructor) do **not** need
a separate reviewer to merge their own PR; a PR is required, but
zero additional approvals are needed.

See [repo.md](miscellaneous/setup/admin/repo.md) for the
underlying GitHub branch-protection settings and the one-time setup
steps.

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
   * solution.md starting with a `# Solution: <Exercise Title>`
     heading (the completion report uses this to label and credit
     each exercise separately when a session has more than one),
     then four sections:
     ```text
     * ## Contributors: one GitHub-UserId per line
     * ## Test Cases: What you ran to validate your solution
     * ## Software Installs: Anything beyond the repo's usual toolchain
     * ## Solution Manual: How to run your solution and its test cases
     ```
   * your file(s):
     * requirements.in (or equivalent) for any extra installs
     * all source files
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
