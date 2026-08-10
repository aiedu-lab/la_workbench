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

### Chain Rule

Many functions worth differentiating aren't given directly — they're
built by feeding one function's output into another. A **composite
function** `y = f(g(x))` first runs `x` through `g`, then feeds that
result into `f`. The **chain rule** says its derivative is the
product of the two pieces' derivatives, each evaluated at the right
point:

```
dy/dx = f'(g(x)) · g'(x)
```

Worked example: let `y = (2x + 1)^3`. Read this as `f(u) = u^3` with
`u = g(x) = 2x + 1`. Then `f'(u) = 3u^2` and `g'(x) = 2`, so:

```
dy/dx = 3(2x + 1)^2 · 2 = 6(2x + 1)^2
```

The chain rule is what lets a curve built from nested pieces still
be differentiated one layer at a time — the exact same "one layer at
a time" structure that lets a neural network's error signal be
pushed backward through each layer during backpropagation.

**Paper Problem:** For `y = (x^2 + 1)^2`, find `dy/dx` two ways: (1)
expand `(x^2 + 1)^2` into a plain polynomial first, then
differentiate term by term; (2) apply the chain rule directly with
`f(u) = u^2`, `u = g(x) = x^2 + 1`. Confirm both approaches give the
same `dy/dx`.

## Exercise

Work through [Down to the Valley Floor](
  ../projects/single_variable_calculus/
) in a Jupyter or Colab notebook: plotting a curve and its critical
point, confirming `f'(x*) = 0` numerically, and stepping downhill
with a small gradient-descent loop to find the minimum. Classifying
that critical point is practiced separately in [Critical
Points](../projects/critical_points/).
