# Solutions: Limits, Continuity to Analytical Apps. of Diff.

Answer key for [test-limits-continuity-to-analytical-apps-of-diff.md](
  ../test-limits-continuity-to-analytical-apps-of-diff.md
). Each entry gives the correct option(s) and a reference
explanation (≤100 words) of the concept, approach, and visual
intuition — use it to check your own reasoning, not just your
letter choices.

---

**Q1.** Correct: A, D.

`g` turns a small change in `x` into a change in its own output,
scaled by `g'(x)`; `f` then turns *that* output change into a
change in `h`, scaled by `f'(g(x))` — the two scaling factors
multiply through the composition (A). If `g'(x) = 0` at a point,
there is no output change from `g` for `f` to further scale, so
`h'(x)` is `0` regardless of `f'`'s value (D). The chain rule
applies to any differentiable `f`, `g` (rules out B), and composing
rates is multiplication, not addition (rules out C).

**Q2.** Correct: A, C.

Differentiating both sides treats `y` as an unknown function of
`x`; any `y`-term picks up a `dy/dx` factor via the chain rule,
giving an equation you solve for `dy/dx` (A) — this works whether
or not the equation can be solved explicitly for `y` (rules out
B). The resulting `dy/dx`, evaluated at a specific `(x, y)` on the
curve, is exactly that point's tangent slope (C); different points
on the same curve generally have different slopes (rules out D).

**Q3.** Correct: A, C.

The Pythagorean relationship between the two distances holds at
every instant, so differentiating it with respect to time
produces one equation linking the two rates (A). But that
equation's coefficients depend on the current distances themselves
— so you must plug in the actual position at the instant in
question to solve for the unknown rate (C); the two rates are not
generally equal (rules out B), and you never need an explicit
position-vs-time formula, only the relating equation (rules out
D).

**Q4.** Correct: A, C.

MVT guarantees some interior point where the instantaneous rate of
change equals the average rate of change over the whole interval
(A) — average speed and *some* instantaneous speedometer reading
must coincide somewhere along the trip (C). It says nothing about
*where* that point falls (rules out B, which wrongly assumes the
midpoint), and it applies to any smooth, not just straight-line,
function (rules out D).

**Q5.** Correct: A, C, D.

Positive `f''` bends the graph upward like a cup; negative `f''`
bends it downward like a cap (A). Concavity is a statement about
how the *slope* `f'(x)` itself is changing as `x` increases, not
about the height `f(x)` (D). An inflection point is where that
bending direction flips — `f''` changes sign — even if `f''`
itself happens to be `0` or undefined right at the flip (C).
`f'(x) = 0` alone says nothing about concavity, so it does not
guarantee an inflection point (rules out B).

**Q6.** Correct: A, B, D.

A critical point is only a *candidate*; you must check how `f'`'s
sign changes on either side to confirm it's actually a max or min
(A) — some critical points (e.g. a flat inflection point) are
neither (rules out C). On a closed interval, the true global
extremes can only hide at a critical point or an endpoint — no
other location needs checking (B). When both `f'` and `f''` vanish
together, the second-derivative test goes silent, but the
first-derivative sign-change test still works (D).

**Q7.** Correct: A, C, D.

Near `x = a`, both functions look like their own tangent lines, so
their ratio behaves like the ratio of those tangent slopes,
`f'(a)/g'(a)` (A) — this substitution is only justified because
the *original* ratio was already `0/0`; a well-defined limit needs
no such rescue (C). If the new ratio is *still* `0/0`, the same
reasoning applies again one derivative deeper, as long as the
indeterminate form persists (D). `0/0` is not simply `1` (rules
out B) — it's a signal to look at rates, not a number itself.

**Q8.** Correct: A, B, D.

Reflecting across `y = x` swaps each point's `(x, y)` coordinates,
which swaps "rise" and "run" — so the inverse's tangent slope at
the mirrored point is the reciprocal of the original's slope there
(A). Differentiating the inverse relation's own implicit equation
is exactly one way to derive that reciprocal relationship (B).
Reciprocal is not the same as identical, except when the slope
happens to be `1` (rules out C); a horizontal original tangent
(slope `0`) reflects to a vertical one, since `1/0` is undefined
(D).

**Q9.** Correct: A.

`f'(x) > 0` means the graph is climbing; `f''(x) < 0` means that
climb rate is itself shrinking — like a car speeding up while its
speedometer's *rate* of increase tapers off, e.g. approaching a
speed limit from below (A). That is *decreasing and concave down*
territory only if `f'` were negative (rules out B), and the
combination is entirely possible — e.g. `sqrt(x)` — so it is not
impossible (rules out C). Concave down bends like a frown, not a
cup, regardless of whether the function is increasing (rules out
D).

**Q10.** Correct: A, D.

Substituting the fixed-perimeter constraint turns area into a
single-variable function `A(x)`; a maximum can occur where
`dA/dx = 0` and the derivative's sign flips from positive to
negative there (A). But `dA/dx = 0` only flags a *candidate* —
confirming it's a true maximum (not a minimum or saddle-like point)
still requires that sign-change or second-derivative check, exactly
as with any critical point (D). The smallest `x` or a degenerate,
collapsed rectangle in fact *minimizes* area toward zero, not
maximizes it (rules out B, C).

**Q11.** Correct: A, C.

Positive velocity means still moving forward; negative acceleration
means that forward speed is shrinking — the car is forward-moving
but decelerating (A), not moving backward (rules out B). If the
deceleration continues, velocity keeps shrinking toward `0`; once
it crosses `0` while acceleration stays negative, the car begins
moving in reverse (C). Velocity and acceleration describe different
things (position's rate vs. velocity's rate) and routinely have
opposite signs, as here (rules out D).

**Q12.** Correct: A, C.

Because `y` isn't given explicitly, `dy/dx = 0` from implicit
differentiation is itself an equation in `x` and `y`; you solve it
together with the curve's original equation to pin down the actual
point(s) (A) — there's no explicit `f'(x)` to simply set to zero.
A horizontal tangent is only a *candidate* extremum: classifying it
as a max, min, or neither still requires further analysis, such as
watching how `dy/dx` behaves nearby (C). Horizontal tangents are
neither guaranteed maxima (rules out B) nor impossible on implicit
curves (rules out D).
