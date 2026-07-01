# Column Space, Rank and Linear Independence

## Concept

A matrix's **column space** is the set of every output it can
possibly produce — every vector `b` that `Ax = b` can actually be
solved for. The **rank** is the dimension of that space: how many
genuinely independent directions the matrix's columns span. If two
columns point along the same line (or one is a combination of the
others), they are **linearly dependent** — one of them adds no new
reachable direction, and the rank is smaller than the number of
columns.

This is the multi-sensor problem in disguise: multiple sensors
measuring the same quantity give you several numbers but only one
piece of independent information. A matrix built from such
measurements has columns that are linearly dependent, and its rank
reveals exactly how much genuinely new information is present,
regardless of how many columns were collected.

The same idea explains *which* `b` a system `Ax = b` can reach. If
`A`'s columns don't span the full output space, some targets `b`
are unreachable no matter what `x` is — this is the geometric
picture behind the singular matrices from the previous session,
generalized beyond just "determinant is zero."

In AI systems, rank measures model capacity and feature
redundancy: a low-rank weight matrix can only represent a limited
family of transformations, and redundant features are columns a
model's rank reveals as not actually adding information.
Dimensionality reduction techniques exploit exactly this — finding
a lower-rank approximation that keeps most of the information.

Watch 3Blue1Brown's *Essence of Linear Algebra*, Chapter 7 —
["Inverse matrices, column space and null
space"](https://www.3blue1brown.com/?topic=linear-algebra) — and
Chapter 8 — ["Nonsquare matrices as transformations between
dimensions"](https://www.3blue1brown.com/?topic=linear-algebra) —
plus Gilbert Strang's MIT 18.06 lectures on column space and
independence at the [18.06 video
gallery](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/).

## Exercise

Work through [Which Directions Can I
Reach?](../projects/column_space_rank/) in a Jupyter or Colab
notebook: column space as reachable outputs, rank via
`np.linalg.matrix_rank`, and testing whether a target vector is
reachable from a redundant or independent set of columns.
