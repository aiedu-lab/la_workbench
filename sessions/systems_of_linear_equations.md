# Systems of Linear Equations

## Concept

A system of linear equations is several constraints on the same
unknowns, asked to hold all at once: balancing finances, electrical
circuits, logistics planning. Written as a matrix equation `Ax = b`,
each row of `A` is one constraint, `x` is the vector of unknowns,
and `b` is the vector of known totals — `np.linalg.solve(A, b)`
finds the one `x` that satisfies every row simultaneously.

Geometrically, each equation is a line (in 2D) or a plane (in
higher dimensions). Solving the system means finding where all of
those lines or planes meet. Two lines normally cross at exactly
one point — a unique solution. But if two equations describe
*parallel* lines, there is no crossing point at all, and if they
describe the *same* line, every point on it is a solution. The
matrix `A` is **singular** exactly when this happens, and
`np.linalg.det(A)` is `0` exactly when `A` is singular — the
determinant is the test for whether a unique solution exists.

This is why systems of equations sit downstream of linear
transformations: solving `Ax = b` is asking "what input, after
applying transformation `A`, lands exactly on `b`?" When `A`
collapses space (determinant zero), some targets `b` are
unreachable, and others are reachable by infinitely many inputs.

Regression, optimization, and parameter estimation in AI are all,
underneath, solving (or approximately solving) systems like this —
finding parameters that satisfy, or best satisfy, many constraints
from data at once.

Watch Gilbert Strang's MIT 18.06 lectures on ["The geometry of
linear equations"](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/)
and ["Elimination with
matrices"](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/)
before the exercise below.

## Exercise

Work through [The Snack Bar
Mystery](../projects/systems_of_linear_equations/) in a Jupyter or
Colab notebook: `Ax = b`, line intersections, and what a singular
matrix means for a system's solutions.
