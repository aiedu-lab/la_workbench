# Solutions: Scalars to Linear Equations

Answer key for [test-scalars-to-linear-equations.md](
  ../test-scalars-to-linear-equations.md
). Each entry gives the correct option(s) and a reference
explanation (≤100 words) of the concept, approach, and visual
intuition — use it to check your own reasoning, not just your
letter choices.

---

**Q1.** Correct: A, C, D.

A dilation that doubles height and halves width scales area by
`2 * 0.5 = 1`, so its determinant is 1, not 2 — this rules out B
and confirms A. A shear slides space sideways without stretching
or compressing along either axis, so it always preserves area:
determinant 1 (C). A determinant of 0 means the transformation
squashes 2D space onto a line (or a point) — one fewer dimension
than it started with (D).

**Q2.** Correct: A.

Composing the *same* rotation twice is special: rotating 30° then
30° more is indistinguishable from rotating 60° once, because
both directions of composition describe the identical net turn.
That is not evidence of general commutativity — "rotate then
scale" reshapes space differently than "scale then rotate" applied
to the same starting picture, so matrix multiplication order
matters in general (rules out B, C, D).

**Q3.** Correct: A.

Cosine similarity divides out each vector's length, leaving only
the angle between them. A short song and a long song can point in
nearly the same "direction" in feature space even though their
raw distance (magnitude difference) is large — cosine similarity
sees them as aligned, which is exactly the property recommendation
and search systems want: "how alike," not "how big."

**Q4.** Correct: A.

Each linear equation is a line; solving the system means finding
every point that lies on all the lines at once. Two parallel
lines point in the same direction but never touch, so no point
satisfies both — no solution exists. This is a purely geometric
fact about intersection, independent of which line is "longer"
(rules out B) and independent of any guarantee of uniqueness
(rules out C, D).

**Q5.** Correct: A, C.

`det(A) = 0` means `A` squashes space onto a lower-dimensional
subspace, so only vectors `b` inside that subspace are reachable
(A) — generic `b` outside it give no solution, not a guaranteed
one (rules out B). Depending on `b`, a singular system can
describe the *same* line twice (infinite solutions) or two
*parallel* lines (no solution) (C) — singularity is about
existence/uniqueness, not just computational speed (rules out D).

**Q6.** Correct: A, B, C.

A shear slides points sideways by an amount depending on position,
so most vectors change length and direction even though the shape
they trace keeps the same area (A). A proportional dilation
(stretch one way, shrink the other by the same factor) similarly
preserves area while still changing every vector's length (B).
Both are linear: straight lines stay straight and the origin is
fixed (C). Neither uniformly doubles every vector (rules out D).

**Q7.** Correct: A, C.

Row operations combine equations (add a multiple of one row to
another) without changing the set of points that satisfy every
original equation — they just re-express the same constraints in
a form that's easier to read off (A). Because of this, elimination
and `np.linalg.solve` are two routes to the identical intersection
point when a unique solution exists (C). The solution point itself
never physically moves (rules out B), and elimination works on
non-singular systems too (rules out D).

**Q8.** Correct: A, C.

A redundant equation (a combination of the other two) describes a
line that already passes through wherever the other two lines
meet — it constrains nothing new (A). Geometrically, throwing in a
row that's already a combination of existing rows can't expand or
shrink the set of outputs `Ax` can reach — the column space is
unchanged (C). Redundancy doesn't force unsolvability (rules out
B) and is compatible with a unique solution from the other two
equations (rules out D).

**Q9.** Correct: B, C.

`R = -I` (a 180° rotation) simply flips every vector's sign, so
`(-I) @ S = -S = S @ (-I)` for *any* `S` — the special structure of
`-I`, not shears/rotations in general, is what makes this pair
commute (B). Trivially, if `S` is the identity (no shear applied
at all), both composite orders just reduce to `R` (C). Shears and
rotations do not commute in general (rules out A), and matching
determinants alone doesn't force commutativity (rules out D).

**Q10.** Correct: A, C.

Rank 2 means the columns of `A` only span a 2D plane inside 3D
space — the column space — so a generically chosen `b` almost
certainly misses that plane and no `x` reaches it (A); "3 equations
in 3 unknowns" does not by itself guarantee a solution once the
rows are dependent (rules out B). When `b` does lie in the plane,
there's a whole line of `x` values that map to it, since one
direction contributes nothing new (C) — rank has real geometric
content (rules out D).

**Q11.** Correct: B, C.

Row operations only recombine existing constraints; they never
add or remove information about where the original lines/planes
intersect, so any valid elimination order lands on the same
solution `x` (B) — the point being solved for cannot depend on the
order you chose to reveal it (rules out A). The intermediate
triangular matrices can differ in appearance between the two
orders, yet both correctly encode the same intersection (C); there
is no single "correct" order (rules out D).

**Q12.** Correct: A.

A pure rotation preserves lengths and right angles, so its columns
are always unit-length and mutually perpendicular (orthonormal) —
checking this directly tests the "pure rotation" claim (A). A
shear breaks this property (its slid direction is no longer
perpendicular to the fixed one), so a matrix that is rotation
*plus* shear will fail the orthonormal-columns check. Determinant
value alone (B), sign of entries (C), and matrix size (D) don't
distinguish a rotation from rotation-plus-shear.
