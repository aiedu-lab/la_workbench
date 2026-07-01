# Scalars, Vectors and Matrices

## Concept

A **scalar** is a single number — a magnitude with no direction,
like a temperature or a price. A **vector** is an ordered list of
numbers, and it carries two meanings at once: a *point* in space
(GPS coordinates, RGB colors, a shopping list) and a *direction
with length* (wind velocity, a force, a step taken). A **matrix**
is a rectangular grid of numbers — a dataset, an image, or, as
later sessions show, a transformation in disguise.

Once you can add and scale vectors, you can combine and reweight
information: adding two vectors composes two movements or two
forces into one; multiplying a vector by a scalar stretches or
shrinks it without changing its direction (or flips it, if the
scalar is negative). These two operations — addition and scalar
multiplication — are the entire foundation linear algebra is built
on.

In AI systems, this vocabulary is everywhere before any "learning"
happens: tokens become vectors, datasets become matrices, and
embeddings represent words, images, and users as vectors that can
be added and scaled just like the pirate's paces below. Feature
weighting, residual connections, and weighted averages are all
vector addition and scalar multiplication wearing different names.

Watch 3Blue1Brown's *Essence of Linear Algebra*, Chapter 1 —
["Vectors, what even are
they?"](https://www.3blue1brown.com/?topic=linear-algebra) — before
the exercise below. It covers exactly this: what a vector is, and
what addition and scaling mean geometrically.

## Exercise

Work through [Pirate Treasure Walk](
  ../projects/scalars_vectors_matrices/
) in a Jupyter or Colab notebook: vector addition, scalar 
multiplication, magnitude, and plotting with `quiver`.
