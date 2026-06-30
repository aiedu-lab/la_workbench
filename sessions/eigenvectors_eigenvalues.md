# Eigenvectors and Eigenvalues (Conceptual)

## Concept

Most vectors get knocked off their original direction by a
transformation — a rotation turns them, a shear slants them. An
**eigenvector** is a special direction that a transformation
leaves unchanged: applying the matrix only stretches or shrinks
it, never turns it. The amount it stretches or shrinks by is its
**eigenvalue**. In the basis built from eigenvectors, a
transformation that looks tangled in the original coordinates
becomes a simple per-direction scaling — which is exactly why
"change of basis" from two sessions ago matters here.

This is why eigenvectors keep showing up wherever something
repeats a transformation many times. A vibrating bridge oscillates
along the directions that are its structure's eigenvectors —
everything else cancels out, leaving the dominant eigenvalue's
direction as the one that grows large and dangerous. Google's
PageRank repeatedly applies a "follow a random link" matrix to a
ranking vector; the ranking that doesn't change anymore *is* an
eigenvector, with eigenvalue 1.

In data, the directions where points vary the most are the
eigenvectors of the data's covariance matrix, ranked by
eigenvalue — exactly what PCA computes to find the principal
directions in data. Diffusion models repeatedly apply a
transformation to noise; whether that process stays stable or
blows up is governed by the eigenvalues involved. Model stability
during training depends on the same thing: weight matrices whose
eigenvalues stay near 1 keep signals from exploding or vanishing
as they pass through many layers.

Watch 3Blue1Brown's *Essence of Linear Algebra*, Chapter 14 —
["Eigenvectors and
eigenvalues"](https://www.3blue1brown.com/?topic=linear-algebra) —
and Chapter 15 — ["A quick trick for computing
eigenvalues"](https://www.3blue1brown.com/?topic=linear-algebra) —
plus Gilbert Strang's MIT 18.06 lecture on eigenvalues and
eigenvectors at the [18.06 video
gallery](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/).

## Exercise

<!-- TODO: exercise -->
