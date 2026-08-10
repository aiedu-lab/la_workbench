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

### Integration with Substitution

Differentiation asks "given a function, what's its slope?"
**Integration** asks the reverse question: "given a slope function
`f'(x)`, what function `f(x)` produced it?" The result, `f(x) + C`
(the `+ C` because any constant vanishes under differentiation), is
called the **antiderivative**, and the indefinite integral is written
`∫f'(x) dx = f(x) + C`.

Whenever the integrand looks like the output of a chain-rule
differentiation, **`u`-substitution** runs the chain rule backward to
find the antiderivative. Worked example:

```
∫ 2x(x^2 + 1)^3 dx
```

Let `u = x^2 + 1`, so `du = 2x dx` — exactly the `2x dx` factor
already sitting in the integral. Substituting:

```
∫ u^3 du = u^4/4 + C = (x^2 + 1)^4/4 + C
```

**Paper Problem:** Evaluate `∫ 3x^2(x^3 + 4)^2 dx` by substitution
(let `u = x^3 + 4`). Then differentiate your answer and confirm you
recover the original integrand `3x^2(x^3 + 4)^2`.

## Exercise

Work through [Down to the Valley Floor](
  ../projects/single_variable_calculus/
) in a Jupyter or Colab notebook: plotting a curve and its critical
point, confirming `f'(x*) = 0` numerically, and stepping downhill
with a small gradient-descent loop to find the minimum. Classifying
that critical point is practiced separately in [Critical
Points](../projects/critical_points/).
