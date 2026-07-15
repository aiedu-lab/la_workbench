# Test: Scalars to Linear Equations

This is a 1-hour, 12-question multiple-choice test covering the
sessions from [Scalars, Vectors and Matrices](
  ../sessions/scalars_vectors_matrices.md
) through [Systems of Linear Equations](
  ../sessions/systems_of_linear_equations.md
). Working alone or with classmates is fine — discussing the
concepts together is encouraged.

Some questions have more than one correct option. For each
question, mark every option you believe is correct, then write
**no more than 100 words** describing the basic concept, approach,
and visual intuition you used. Correctness is judged on that
reasoning, not on numerical computation — none of these questions
require heavy arithmetic.

Check your answers against [the solution key](
  solutions/soln-scalars-to-linear-equations.md
) once you've finished.

---

**Q1.** _(Basic)_ A dilation matrix doubles height and halves
width; a shear matrix slides space sideways by an amount that
depends on position. Which statement(s) about their determinants
are true?

A. Both leave area unchanged, so both have determinant 1.
B. The dilation's determinant is 2, since height doubled.
C. The shear's determinant is 1, no matter how much it slants.
D. A determinant of 0 would mean the transformation collapses
   space onto a lower dimension.

**Q2.** _(Basic)_ Rotating by 30° twice and rotating by 60° once
produce the same result: `rot(30) @ rot(30) = rot(60)`. What
visual idea explains why matrix multiplication order otherwise
matters (`A @ B` generally is not `B @ A`)?

A. "Rotate then scale" and "scale then rotate" are genuinely
   different transformations, even though repeating the *same*
   rotation composes predictably.
B. Matrix multiplication is always commutative for any A and B.
C. Only rotation matrices can be multiplied together.
D. Order never affects the outcome of a transformation.

**Q3.** _(Basic)_ Cosine similarity is the dot product of two
vectors normalized by their lengths. Why do recommendation and
search systems often prefer it over raw distance?

A. Because a short item and a long item (e.g. a short song and a
   long song) can still point in nearly the same direction, so
   cosine similarity captures "alignment" independent of size.
B. Because raw distance is always a better measure of similarity.
C. Because cosine similarity can only be computed on 2D vectors.
D. Because normalizing by length always increases the dot product.

**Q4.** _(Basic)_ In `Ax = b`, each row of `A` describes one
equation, which in 2D is a line. What does "solving the system"
mean geometrically, and what happens if two of those lines are
parallel?

A. Solving means finding the point(s) where all the lines meet;
   two parallel lines never meet, so there is no solution.
B. Solving means finding the longest line among the equations.
C. Parallel lines always meet at exactly one point.
D. The system has a unique solution regardless of whether the
   lines are parallel.

**Q5.** _(Medium)_ A matrix `A` is singular exactly when
`np.linalg.det(A) == 0`. Select every statement that correctly
connects this to systems of equations:

A. A singular `A` means the transformation collapses space onto a
   lower dimension, so some target vectors `b` become unreachable.
B. For a singular `A`, every possible `b` still has exactly one
   solution `x`.
C. A singular `A` can correspond to two equations describing the
   same line (infinitely many solutions) or parallel lines (no
   solution), depending on `b`.
D. Singularity only ever affects how fast a computer can solve
   the system, never whether a solution exists.

**Q6.** _(Medium)_ A shear matrix never changes area, no matter
how much it slants, and it leaves one direction completely fixed.
Contrast this with a dilation. Select every true statement:

A. A shear can change the length and direction of most vectors
   even though the area of any shape stays the same.
B. A dilation that stretches taller and narrows width proportionally
   can also preserve area while changing every vector's length.
C. Both transformations keep straight lines straight and the
   origin fixed — they are still linear transformations.
D. A shear always doubles the length of every vector it acts on.

**Q7.** _(Medium)_ Elimination solves `Ax = b` by row operations
that reduce `A` toward a simpler (triangular) form, rather than
calling `np.linalg.solve` directly. Which statement(s) best
describe what's happening geometrically as elimination proceeds?

A. Each row operation is combining constraint-lines (or planes)
   without changing where they all meet, gradually making the
   intersection point easier to read off directly.
B. Row operations physically move the solution point to a new,
   different location.
C. Elimination and `np.linalg.solve` can reach the same unique
   solution when one exists, because both are answering "where do
   these lines/planes meet?"
D. Row operations always require the matrix to already be
   singular before they can be applied.

**Q8.** _(Medium)_ Suppose a 3-equation system in 2 unknowns has
one equation that is a combination of the other two (e.g. their
sum). Select every statement consistent with the column-space
intuition from this test's sessions:

A. That equation's line still passes through the same intersection
   point as the other two, so it adds no new constraint.
B. Adding a redundant equation always makes a system unsolvable.
C. The transformation's "reachable" outputs (its column space) are
   unaffected by throwing in a redundant combination of rows.
D. Redundant equations can never coexist with a unique solution.

**Q9.** _(High)_ Let `S` be a shear and `R` a rotation. Under
what condition(s) would the composite matrices `R @ S` and
`S @ R` be equal, even though matrix multiplication generally
does not commute?

A. Never — a shear and a rotation never commute under any
   circumstance.
B. Whenever `R` is the 180° rotation (`R = -I`), since `-I`
   commutes with every matrix.
C. Whenever `S` is the identity transformation — i.e. no shear at
   all is actually applied.
D. Only when both `S` and `R` happen to have determinant exactly
   1.

**Q10.** _(High)_ A 3x3 matrix `A` has rank 2 (one row is a
linear combination of the other two, and `det(A) = 0`). For a
generic vector `b`, is `Ax = b` solvable, and what does this say
about the columns of `A`?

A. Generically unsolvable, because the column space of `A` is
   only a 2D plane inside 3D space, and a generic `b` will not lie
   exactly on that plane.
B. Always solvable for every `b`, since 3 equations in 3 unknowns
   always have a unique solution.
C. If a solution exists for a specific `b` that does lie in the
   column space, it is not unique — infinitely many solutions
   exist along a fixed direction.
D. Rank 2 carries no geometric meaning distinct from rank 3.

**Q11.** _(High)_ Two students both correctly solve `Ax = b` by
elimination, but perform their row operations in a different
order (one eliminates using row 1 first, the other starts from
row 2). What is true about their results?

A. They must get different final solutions `x`, since the
   elimination order changes the answer.
B. They get the same final solution `x`, because elimination
   never changes which point(s) satisfy every original equation —
   only how the constraints are combined en route.
C. Their intermediate triangular matrices may look different, but
   both correctly identify the same underlying intersection
   point(s).
D. Only one of the two elimination orders can be "the" correct
   one.

**Q12.** _(High)_ A shear leaves one direction entirely fixed. A
rotation (other than 0°/360°) leaves no nonzero real vector fixed.
If a 2x2 matrix `M` is claimed to be "a rotation combined with a
shear along the x-axis, in some order," what property would you
check first to test whether `M` could instead be a pure rotation?

A. Whether `M`'s columns are unit-length and perpendicular to each
   other (orthonormal) — a pure rotation always has this property,
   so a failure here rules out pure rotation.
B. Whether `det(M)` equals exactly 2.
C. Whether any entry of `M` is negative.
D. Whether `M` is a 2x2 matrix at all.
