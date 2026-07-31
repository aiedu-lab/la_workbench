# Single-Variable Calculus

## Concept

A function `y = f(x)` maps a single input to a single output. Its
**derivative** `f'(x)` measures the slope of the curve at each
point — how steeply, and in which direction, `y` changes as `x`
nudges slightly. Where the curve is climbing, `f'(x) > 0`; where
it's falling, `f'(x) < 0`; and at the very bottom of a valley or
the very top of a hill, the curve momentarily flattens out:
`f'(x) = 0`.

```
        f(x)
         ^
         |  *                     *
         |    *                 *
         |      *             *
         |        *         *
         |          *     *
         |            * *
         +--------------*----------------> x
                      x* (f'(x*) = 0)
```

That flat point, `x*`, is a **critical point** — a candidate for a
local minimum or maximum, but not automatically one or the other.
Classifying it — and why the **second derivative** `f''(x)` is what
settles the question — is the subject of [Critical Points and the
Second Derivative Test](critical_points.md).

There's a second way to read `f'(x)`: as a direction. At any point
`x`, moving in the direction of `f'(x)` walks *uphill* (`f`
increases), and moving in the *opposite* direction — `-f'(x)` —
walks *downhill* (`f` decreases). Repeatedly nudging `x` a small
step in the `-f'(x)` direction, over and over, walks straight down
to the nearest valley floor, arriving at the same `x*` where
`f'(x*) = 0`. That single idea, "always step downhill using the
derivative," is gradient descent in its simplest, one-variable
form — the seed [Learning from Mistakes: Gradients and
Backpropagation](gradients_backpropagation.md) later generalizes to
every parameter of a neural network at once.

## Exercise

Work through [Down to the Valley Floor](
  ../projects/single_variable_calculus/
) in a Jupyter or Colab notebook: plotting a curve and its critical
point, confirming `f'(x*) = 0` numerically, and stepping downhill
with a small gradient-descent loop to find the minimum. Classifying
that critical point is practiced separately in [Critical
Points](../projects/critical_points/).
