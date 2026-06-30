# Introduction

## Concept

Linear Algebra is the language modern AI is written in. Before any
model can learn, its inputs — text, images, audio, tabular rows —
must become numbers, and the structures that hold and transform
those numbers (vectors, matrices) are exactly what this course
builds intuition for.

The course arc follows one continuous thread:

1. **Why a model at all, and why vectors?** ([What is a
   Model?](what_is_a_model.md), [Why Linear
   Algebra?](why_linear_algebra.md)) — frame the problem before
   the math.
2. **The vocabulary.**
   ([Scalars, Vectors and Matrices](scalars_vectors_matrices.md),
   [Distance, Length and Similarity](distance_length_similarity.md))
   — what these objects are and how to compare them.
3. **The machinery.** ([Linear
   Transformations](linear_transformations.md), [Matrix
   Multiplication](matrix_multiplication.md), [Systems of Linear
   Equations](systems_of_linear_equations.md)) — how matrices act on
   vectors and how to solve for unknowns.
4. **The structure underneath.** ([Column Space, Rank and Linear
   Independence](column_space_rank.md), [Basis and Change of
   Basis](basis_change_of_basis.md), [Orthogonality and
   Projections](orthogonality_projections.md), [Eigenvectors and
   Eigenvalues](eigenvectors_eigenvalues.md)) — what a
   transformation preserves, discards, and leaves unchanged.
5. **Where AI lives.** ([High-Dimensional
   Geometry](high_dimensional_geometry.md), [Embeddings](
   embeddings.md), [Forward Propagation](forward_propagation.md),
   [Gradients and Backpropagation](gradients_backpropagation.md)) —
   the same vocabulary and machinery, scaled up and made to learn.
6. **The capstone.** ([Kaggle Titanic
   Capstone](kaggle_titanic_capstone.md)) — train one real model,
   end to end, using everything above.

Each session keeps the same shape: a real-world problem, the linear
algebra idea that solves it, a visualization, and its connection to
modern AI. Most sessions also link a 3Blue1Brown or Gilbert Strang
lecture — watch those before lab day, then use the session to
connect the lecture to a short hands-on exercise.

## Output

Before the next session, complete [Development Workbench
Setup](dev_workbench.md): sign up for Google Colab, install VSCode
and Claude Code, and run the lab setup scripts so NumPy, PyTorch,
and Jupyter are ready for every exercise that follows.
