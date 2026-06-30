# Distance, Length and Similarity

## Concept

A vector's **length** (or *norm*) tells you how big it is —
`np.linalg.norm` from the Pirate Treasure Walk exercise already
computed one. The **distance** between two vectors is just the
length of the vector that separates them: subtract, then measure.
That single idea — subtract, then measure — is how a computer
decides whether two things are "close."

Closeness, though, is not always about distance. Two vectors can
be far apart in length but point in almost the same direction, and
for many questions *direction* is what actually matters. The
**dot product** of two vectors captures exactly this: it grows
when vectors point the same way, shrinks toward zero when they are
perpendicular, and goes negative when they point opposite ways.
Normalize it by the vectors' lengths and you get **cosine
similarity** — a measure of "how aligned," independent of size.

This is why recommendation and search systems lean on dot products
and cosine similarity rather than raw distance: a short song and a
long song can still be very similar in style, the way two vectors
can point the same direction at different lengths. Finding similar
songs, recommending products, and searching documents are all,
underneath, nearest-neighbor or highest-similarity lookups over
vectors.

Embeddings make this concrete: words, images, and users become
vectors precisely so that "similarity" becomes a number you can
compute. Semantic search and recommendation systems work by
embedding everything into the same vector space, then ranking by
distance or cosine similarity.

Watch 3Blue1Brown's *Essence of Linear Algebra*, Chapter 9 —
["Dot products and
duality"](https://www.3blue1brown.com/?topic=linear-algebra) —
before the exercise below. It builds the dot product up
geometrically, from projection to the algebraic formula.

## Exercise

<!-- TODO: exercise -->
