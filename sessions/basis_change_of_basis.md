# Basis and Change of Basis

## Concept

A **linear combination** is what you get by scaling and adding
vectors — exactly the two operations from the first session,
applied together. The **span** of a set of vectors is every
linear combination you can build from them: every point reachable
by scaling and adding. A **basis** is the smallest such set that
still reaches everywhere in a space — enough vectors to span it,
with none redundant (none linearly dependent on the others).

Every vector's coordinates are only meaningful relative to a
chosen basis. `(3, 4)` means "3 of the first basis vector plus 4
of the second" — change the basis vectors, and the same point
gets entirely different coordinates, even though the point itself
hasn't moved. This is the same object represented in a different
coordinate system, the way GPS coordinates and a local street
map's "3 blocks north, 2 blocks east" describe the same location
in two different bases.

**Change of basis** is the matrix operation that translates
coordinates from one basis into another — useful whenever the
"natural" coordinates for a problem aren't the default ones a
system started in. Choosing a better basis can turn a hard
problem (coordinates tangled together) into an easy one
(coordinates that act independently), which is exactly the
motivation behind the eigenvector basis in a later session.

In AI systems, this is the idea behind feature spaces and latent
representations: an embedding is, in effect, a choice of basis in
which "similar" things land near each other — a basis chosen not
by hand, but learned from data.

Watch 3Blue1Brown's *Essence of Linear Algebra*, Chapter 2 —
["Linear combinations, span, and basis
vectors"](https://www.3blue1brown.com/?topic=linear-algebra) — and
Chapter 13 — ["Change of
basis"](https://www.3blue1brown.com/?topic=linear-algebra) —
before the exercise below.

## Exercise

Work through [Describe It In My Coordinates](
  ../projects/basis_change_of_basis/
) in a Jupyter or Colab notebook: defining a custom basis, 
converting a point's coordinates into it with `np.linalg.solve`, 
and converting back.
