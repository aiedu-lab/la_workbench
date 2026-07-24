# Partial Derivatives and Multivariate Calculus — Exercise

## The Hill and Its Slices

**Skills:** partial derivatives as frozen-variable slopes, the
chain rule for a function of a function, the gradient as a
vector, `np.linalg.norm` and dot products, and finding a minimum
where the gradient is the zero vector.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: a central difference estimates a derivative numerically
without symbolic algebra — `(f(x+h) - f(x-h)) / (2*h)` for a small
`h`. The same idea, applied along just one axis at a time, gives a
partial derivative.

### Paper Problem

Let `f(x, y) = x^2 + x*y`, and suppose `y` is itself a function of
`x`: `y = g(x) = 3*x - 2`. By hand:

* Compute `∂f/∂x` and `∂f/∂y` (treating `x` and `y` as independent).
* Compute `dy/dx` from `g`.
* Use the chain rule, `df/dx = ∂f/∂x + ∂f/∂y * dy/dx`, to get the
  full derivative of `f` along the curve `y = g(x)`.
* Now substitute directly: let `h(x) = f(x, g(x))`, expand it out,
  and differentiate `h(x)` the ordinary single-variable way.
* Confirm both routes give the same answer.

### Coding Exercise

* Define `f(x, y) = x**2 + x*y` and visualize it as a contour plot
  over a grid of `x, y` values — this is the "hill" from the
  session's Concept section, viewed from above.
* Pick a point `(x0, y0)`, e.g. `(1.0, 1.0)`. On the same figure,
  draw a horizontal line at `y = y0` and a vertical line at
  `x = x0` — these mark the two slices you're about to take.
* Plot the slice with `y` frozen at `y0`: `f(x, y0)` as a function
  of `x` alone. The slope of this curve at `x0` is `∂f/∂x`.
* Plot the slice with `x` frozen at `x0`: `f(x0, y)` as a function
  of `y` alone. The slope of this curve at `y0` is `∂f/∂y`.
* Estimate both partials numerically with a central difference and
  collect them into a gradient vector `grad = [df_dx, df_dy]`.
  Use `np.linalg.norm(grad)` to get the steepness of the hill's
  steepest direction at `(x0, y0)`.
* Confirm the chain rule: compute `df/dx` along `y = g(x)` two
  ways — (a) the chain-rule formula using your numerical partials
  and `dy/dx = 3`, and (b) a central difference applied directly
  to `h(x) = f(x, g(x))`. They should match.
* Pick a small step direction `d = [dx, dy]` (e.g. `[0.01, 0.02]`).
  Compare `grad @ d` (the dot product) against the actual change
  in `f` for a small step in that direction, estimated with a
  central difference along the line `(x0, y0) + t*d`. They should
  agree closely — this is `dz = ∇f · dx` from the session.

### Finding Max/Min via Partial Derivatives

A separate, simpler hill, `f(x, y) = x^2 + y^2` (a perfect bowl),
makes critical points easy to see. Its gradient is
`[2*x, 2*y]`, which is the zero vector only at `(0, 0)`.

* Confirm numerically that the gradient at `(0, 0)` is
  approximately `[0, 0]`.
* Sample several nearby points (e.g. random small `(x, y)` offsets)
  and confirm `f(0, 0)` is less than or equal to `f` at every
  sampled point — visual (and numeric) confirmation that `(0, 0)`
  is a minimum, the two-variable analog of the first-/second-
  derivative test from [Single-Variable Calculus](
    ../single_variable_calculus/
  ).

**Stretch goal:** Repeat the max/min check on
`f(x, y) = -(x^2 + y^2)` (an upside-down bowl). The gradient is
still zero at `(0, 0)`, but is it now a minimum or a maximum? How
do the nearby sample points tell you which one?

## Finding the Best-Fit Line

**Skills:** minimizing a two-variable function via partial
derivatives, centered vectors, variance/covariance as dot
products, and projection.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

### Paper Problem

You have `N = 5` points: `x = [1, 2, 3, 4, 5]`,
`y = [2, 3, 5, 4, 6]`. You want the line `y = a*x + b` that
minimizes `f(a, b) = (1/N) * sum_i (y_i - (a*x_i + b))^2`. By
hand:

* Set `∂f/∂a = 0` and `∂f/∂b = 0` and solve the resulting pair of
  equations for `a` and `b` in terms of `sum(x_i)`, `sum(y_i)`,
  `sum(x_i*y_i)`, and `sum(x_i^2)` — this is the general
  derivation behind `a = Cov(x, y) / Var(x)` and
  `b = Ave(y) - a * Ave(x)` from the session's Concept section.
* Compute `Ave(x)`, `Ave(y)`, then the centered values `Cen(x)`
  and `Cen(y)` for all 5 points.
* Compute `Var(x) = (1/N) * Cen(x) . Cen(x)` and
  `Cov(x, y) = (1/N) * Cen(y) . Cen(x)` by hand, then `a` and `b`.
* You should get `a = 0.9` and `b = 1.3`.

### Coding Exercise

* Define `x = np.array([1, 2, 3, 4, 5])` and
  `y = np.array([2, 3, 5, 4, 6])`.
* Compute `a` and `b` using the centered-vector/dot-product
  formulas from the Paper Problem — `Cen(x) = x - x.mean()`,
  `Cen(y) = y - y.mean()`, `a = (Cen(y) @ Cen(x)) / (Cen(x) @
  Cen(x))`, `b = y.mean() - a * x.mean()`.
* Cross-check against `np.polyfit(x, y, 1)`, which returns
  `[a, b]` directly — the two approaches should agree.
* Plot the 5 points as a scatter, then draw the fitted line
  `y = a*x + b` over the same `x` range to see how well it tracks
  the data.

**Stretch goal:** Repeat the fit on `z = 2 * np.exp(0.3 * x)`
(with some noise added) by first taking `w = np.log(z)`, fitting
a line to `(x, w)`, and recovering the exponential's rate `a` and
scale `d = exp(b)` — this is the exponential-fit generalization
from the session's Concept section.

## Help

Copy this once and reuse it to draw a function's contour plot
alongside its two frozen-variable slices:

```python
def plot_function_and_slices(f, xr, yr, x0, y0, n=100):
    """Contour plot of f plus its slices frozen at x0 and y0."""
    xs = np.linspace(*xr, n)
    ys = np.linspace(*yr, n)
    X, Y = np.meshgrid(xs, ys)
    Z = f(X, Y)

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))

    axes[0].contourf(X, Y, Z, levels=20)
    axes[0].axhline(y0, color='C1')
    axes[0].axvline(x0, color='C2')
    axes[0].set_title('f(x, y)')

    axes[1].plot(xs, f(xs, y0), color='C1')
    axes[1].scatter([x0], [f(x0, y0)], color='C1', zorder=3)
    axes[1].set_title(f'f(x, y={y0}) — slope is df/dx')

    axes[2].plot(ys, f(x0, ys), color='C2')
    axes[2].scatter([y0], [f(x0, y0)], color='C2', zorder=3)
    axes[2].set_title(f'f(x={x0}, y) — slope is df/dy')
```

Copy this once and reuse it to draw the scatter of points
alongside the fitted best-fit line:

```python
def plot_best_fit(x, y, a, b):
    """Scatter the points and overlay the fitted line y = a*x + b."""
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='C0', label='data')
    xs = np.linspace(x.min(), x.max(), 100)
    ax.plot(xs, a * xs + b, color='C1', label='best fit')
    ax.legend()
```

Don't just eyeball the chain rule or the critical point — let the
asserts confirm them:

```python
def partial_x(f, x, y, h=1e-5):
    return (f(x + h, y) - f(x - h, y)) / (2 * h)

def partial_y(f, x, y, h=1e-5):
    return (f(x, y + h) - f(x, y - h)) / (2 * h)

f = lambda x, y: x**2 + x * y
g = lambda x: 3 * x - 2
h = lambda x: f(x, g(x))
x0 = 1.0

chain_rule_deriv = partial_x(f, x0, g(x0)) + partial_y(f, x0, g(x0)) * 3
direct_sub_deriv = (h(x0 + 1e-5) - h(x0 - 1e-5)) / (2e-5)
assert np.isclose(chain_rule_deriv, direct_sub_deriv, atol=1e-3)

grad = np.array([partial_x(f, x0, 1.0), partial_y(f, x0, 1.0)])
d = np.array([0.01, 0.02])
t = 1e-4
directional = (f(x0 + t * d[0], 1.0 + t * d[1])
               - f(x0 - t * d[0], 1.0 - t * d[1])) / (2 * t)
assert np.isclose(grad @ d, directional, atol=1e-2)

bowl = lambda x, y: x**2 + y**2
grad_at_origin = np.array([partial_x(bowl, 0.0, 0.0),
                            partial_y(bowl, 0.0, 0.0)])
assert np.linalg.norm(grad_at_origin) < 1e-3  # gradient ~ [0, 0]

samples = np.random.uniform(-1, 1, size=(20, 2))
assert all(bowl(0.0, 0.0) <= bowl(px, py) for px, py in samples)

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 4, 6])
cen_x = x - x.mean()
cen_y = y - y.mean()
a = (cen_y @ cen_x) / (cen_x @ cen_x)
b = y.mean() - a * x.mean()
assert np.allclose([a, b], np.polyfit(x, y, 1))
```
