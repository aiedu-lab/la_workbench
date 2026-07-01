# High-Dimensional Geometry

## Concept

Every session so far has used 2D pictures — arrows on a flat page,
shapes you can sketch. AI routinely works in spaces with hundreds
or thousands of dimensions, where "picture it" stops being
literally possible but the linear algebra you already know keeps
working exactly the same way: vectors still add, scale, and have
a length and an angle between them, no matter how many numbers
they hold.

A customer profile (age, location, purchase history, dozens of
other features), a genome (thousands of markers), or a
recommendation system's catalog (one dimension per possible item a
user might rate) are all naturally high-dimensional vectors. Each
extra dimension is just one more number in the list — nothing
conceptually new, but the geometry starts behaving in ways that
feel unintuitive: in high dimensions, most of a sphere's volume
sits near its surface, and randomly chosen vectors tend to be
nearly orthogonal to each other far more often than low-dimensional
intuition expects.

This matters directly for the next session: embeddings with
hundreds or thousands of dimensions are how AI systems represent
words, images, and users richly enough to capture fine-grained
similarity — far more categories of "alike" than a handful of
dimensions could ever encode. The vocabulary from earlier sessions
(distance, dot product, projection, rank) is exactly what you need
to reason about these spaces; only the dimension count has grown.

## Exercise

Work through [Curse of Dimensionality Mini-Lab](
  ../projects/high_dimensional_geometry/
) in a Jupyter or Colab notebook: generating random points across 
increasing dimensions and observing how pairwise distances 
concentrate.
