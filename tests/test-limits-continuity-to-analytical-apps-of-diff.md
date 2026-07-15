# Test: Limits, Continuity to Analytical Applications of Diff.

This is a 1-hour, 12-question multiple-choice test covering AP
Calculus BC Units 1-5 (Limits and Continuity through Analytical
Applications of Differentiation), per the [AP Calculus BC Course
and Exam Description](
  https://apcentral.collegeboard.org/media/pdf/ap-calculus-ab-and-bc-course-and-exam-description.pdf
). Working alone or with classmates is fine — discussing the
concepts together is encouraged.

Some questions have more than one correct option. For each
question, mark every option you believe is correct, then write
**no more than 100 words** describing the basic concept, approach,
and visual intuition you used. Correctness is judged on that
reasoning, not on numerical computation — none of these questions
require heavy arithmetic.

Check your answers against [the solution key](
  solutions/soln-limits-continuity-to-analytical-apps-of-diff.md
) once you've finished.

---

**Q1.** _(Basic)_ A function `f` has a "hole" at `x = a`: it is
undefined there, but the graph approaches the same height `L` from
both sides as `x` gets arbitrarily close to `a`. Which statement(s)
are true?

A. `lim(x -> a) f(x) = L`, even though `f(a)` itself is undefined.
B. The limit cannot exist unless `f(a)` is defined.
C. `f` is discontinuous at `a`, since continuity also requires
   `f(a)` to be defined and equal to the limit.
D. The graph must have a vertical asymptote at `x = a`.

**Q2.** _(Basic)_ The derivative `f'(a)` is best understood as:

A. The slope of the line tangent to the graph of `f` at `x = a`.
B. The instantaneous rate of change of `f` at the single point
   `x = a`, the limit of the secant slope as the second point
   slides toward `a`.
C. The average rate of change of `f` over the whole domain.
D. Always equal to `f(a)` itself.

**Q3.** _(Basic)_ Continuity at `x = a` requires all of the
following to hold *simultaneously*. Which statement correctly
lists them?

A. `f(a)` is defined, `lim(x -> a) f(x)` exists, and the two are
   equal.
B. Only that `lim(x -> a) f(x)` exists — `f(a)` need not be
   defined.
C. Only that `f(a)` is defined — the limit is irrelevant.
D. `f` must be differentiable at `a`.

**Q4.** _(Basic)_ On a position-vs-time graph, the secant line
between two points gives the average velocity over that interval,
while the tangent line at a single point gives the instantaneous
velocity there. Which statement(s) correctly describe the
relationship between the two as the interval shrinks?

A. As the second point slides toward the first, the secant line's
   slope approaches the tangent line's slope.
B. The secant slope and tangent slope are always identical,
   regardless of interval width.
C. Average rate of change is a limit of instantaneous rates, never
   the other way around.
D. Shrinking the interval to a single point makes the secant slope
   undefined at every function.

**Q5.** _(Medium)_ For a composite function `h(x) = f(g(x))`, the
chain rule gives `h'(x) = f'(g(x)) * g'(x)`. Which statement(s)
correctly describe the visual/rate intuition behind this?

A. `g` converts a change in `x` into a change in its own output at
   rate `g'(x)`, and `f` then converts *that* change into a change
   in `h` at rate `f'(g(x))` — the two rates multiply through the
   composition.
B. The chain rule only applies when `f` and `g` are both linear
   functions.
C. `h'(x)` can be computed by simply adding `f'(x)` and `g'(x)`.
D. If `g'(x) = 0` at some point, the overall composed rate of
   change `h'(x)` is also `0` at that point, regardless of `f'`.

**Q6.** _(Medium)_ A curve is defined implicitly by an equation
like `x^2 + y^2 = 25`, where `y` is not solved for explicitly.
Which statement(s) correctly describe implicit differentiation?

A. You differentiate both sides of the equation with respect to
   `x`, treating `y` as an (unknown) function of `x` and applying
   the chain rule to any `y`-term, producing a `dy/dx` term to
   solve for.
B. Implicit differentiation only works when the equation can first
   be solved explicitly for `y`.
C. The resulting `dy/dx` gives the slope of the tangent line to the
   curve at a specific point `(x, y)` on it.
D. Every point on the curve shares the exact same tangent slope.

**Q7.** _(Medium)_ A ladder leans against a wall; its base slides
away from the wall while the top slides down. This is a related
rates problem. Which statement(s) about the approach are true?

A. A single equation (e.g. from the Pythagorean theorem) relates
   the two changing distances at every instant, so differentiating
   that equation with respect to time links their two rates of
   change together.
B. The rate at which the base moves and the rate at which the top
   moves must always be numerically equal.
C. You need to know the actual positions (not just an equation
   relating them) at the instant in question to relate the rates,
   since the relationship between the rates itself depends on the
   current position.
D. Related rates problems require finding an explicit formula for
   position as a function of time before differentiating.

**Q8.** _(Medium)_ The Mean Value Theorem (MVT) says that for a
smooth curve between two points, at least one point in between has
a tangent line parallel to the secant line connecting the
endpoints. Which statement(s) correctly capture the visual
intuition?

A. Somewhere between the endpoints, the instantaneous rate of
   change must match the average rate of change over the whole
   interval.
B. MVT guarantees the tangent-parallel point is exactly halfway
   between the two endpoints.
C. If you drove a route and your average speed was 60 mph, MVT
   says your speedometer must have read exactly 60 mph at some
   moment during the trip.
D. MVT only applies to straight-line functions.

**Q9.** _(High)_ The sign of `f''(x)` (the second derivative)
describes concavity, and an inflection point is where concavity
changes. Select every statement consistent with this:

A. Where `f''(x) > 0`, the graph curves upward like a cup, and
   where `f''(x) < 0`, it curves downward like a cap.
B. A point where `f'(x) = 0` is automatically an inflection point.
C. At an inflection point, `f''(x)` changes sign (e.g. from
   positive to negative), even if `f''` at that exact point is `0`
   or undefined.
D. Concavity describes how the slope `f'(x)` itself is changing,
   not the value of `f(x)`.

**Q10.** _(High)_ To find where a smooth function `f` attains its
maximum or minimum on a closed interval, you check critical points
(`f'(x) = 0` or `f'` undefined) and the interval's endpoints.
Select every true statement:

A. A critical point is not automatically a maximum or minimum —
   its nature must be confirmed, e.g. by checking how the sign of
   `f'` changes on either side of it.
B. The global maximum or minimum on a closed interval must occur
   at a critical point or an endpoint — nowhere else needs to be
   checked.
C. Every critical point of a smooth function is a local extremum.
D. If `f'(x) = 0` at a point but `f''(x)` also equals `0` there,
   the first-derivative sign test can still classify the point
   even when the second-derivative test is inconclusive.

**Q11.** _(High)_ A limit like `lim(x -> a) f(x)/g(x)` produces
the indeterminate form `0/0`, meaning both the numerator and
denominator individually approach `0`. Select every statement
consistent with why derivatives (L'Hôpital's Rule) can resolve
this:

A. Near `x = a`, both `f(x)` and `g(x)` behave approximately like
   their tangent lines at `a`, so the ratio of the functions
   approaches the ratio of their instantaneous rates of change,
   `f'(a)/g'(a)`.
B. `0/0` always equals `1`, so no further work is needed.
C. Replacing `f` and `g` with their derivatives is only valid
   because the original ratio's limit was already an indeterminate
   form — it does not apply to a ratio that already has a clear,
   defined limit.
D. If `f'(a)/g'(a)` is still `0/0`, the rule can be reapplied using
   second derivatives, as long as the indeterminate form persists.

**Q12.** _(High)_ A curve defined implicitly, and its inverse
relation (swap the roles of `x` and `y`), are reflections of each
other across the line `y = x`. Select every statement consistent
with how this connects implicit differentiation to inverse
function derivatives:

A. At corresponding reflected points, the tangent slope of the
   inverse is the reciprocal of the original curve's tangent
   slope there, since reflecting across `y = x` swaps the roles of
   "rise" and "run."
B. Differentiating an inverse function's defining equation
   implicitly (treating the inverse as a function of the original
   variable) is one way to derive that reciprocal-slope
   relationship directly.
C. A curve and its reflection across `y = x` always have identical
   tangent slopes at corresponding points.
D. Wherever the original curve has a horizontal tangent (slope
   `0`), the reflected inverse relation has a vertical tangent at
   the corresponding point.
