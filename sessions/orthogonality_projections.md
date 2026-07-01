# Orthogonality and Projections

## Concept

Two vectors are **orthogonal** when they point in completely
unrelated directions — their dot product is zero, meaning neither
contains any of the other's direction. A **projection** takes a
vector and finds its closest shadow onto a line or subspace: the
component of the vector that *does* point along that direction,
with everything orthogonal to it dropped.

Projections are how you separate signal from noise. Noise-
cancelling headphones work by isolating the component of a sound
wave that matches a known noise pattern and subtracting it,
leaving only what's orthogonal to that pattern. A literal shadow
is a projection too: it keeps a shape's extent along the ground
and discards its extent along the light's direction.

When a system `Ax = b` has no exact solution (more equations than
truly independent unknowns can satisfy), the best you can do is
find the `x` that lands as close to `b` as possible — the
projection of `b` onto the column space of `A`. This is **least
squares**: not solving the system exactly, but minimizing the
error between what `Ax` produces and what `b` actually is.

This is the same idea behind PCA (which projects data onto the
directions that preserve the most variance), regression (which
finds the best-fitting line or plane by least squares), and
attention in transformers (which weights and combines vectors by
how aligned, i.e. how little orthogonal, they are to a query).

Watch Gilbert Strang's MIT 18.06 lectures on ["Projections onto
subspaces"](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/)
and ["Projection matrices and least
squares"](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/)
before the exercise below.

## Exercise

Work through [Shadow on the
Wall](../projects/orthogonality_projections/) in a Jupyter or
Colab notebook: the projection formula, decomposing a vector into
projection plus residual, and confirming orthogonality.
