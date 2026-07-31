# Critical Points — Exercise

## Finding the Bowl's Bottom

**Skills:** critical points via `f'(x) = 0`, the second-derivative
test, `np.roots`, numerical derivatives via finite differences.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `np.roots` finds every root of a polynomial from its
coefficients, highest power first — no algebra by hand needed once
you have `f'(x)`'s coefficients. A central difference,
`(f(x+h) - f(x-h)) / (2*h)`, estimates a derivative numerically.

### Paper Problem

By hand, for `f(x) = x^3 - 3*x`:

* Compute `f'(x)`. Set it to `0` and solve for both critical
  points.
* Compute `f''(x)`. Evaluate its sign at each critical point to
  classify it as a minimum or a maximum.
* Is either critical point indeterminate (`f''(x) = 0`)? Check, and
  say why or why not.

### Coding Exercise

* Write `f'(x) = 3*x^2 - 3`'s coefficients as `[3, 0, -3]` and pass
  them to `np.roots` to find both critical points. Compare against
  your hand-solved values.
* For each critical point, estimate `f''(x)` numerically — apply a
  central difference to a central-difference estimate of `f'(x)` —
  and confirm its sign matches your paper-problem classification.
* Plot `f` over `x` in `[-2.5, 2.5]`, mark each critical point, and
  label it "min" or "max".

**Stretch goal:** Repeat the process for `g(x) = x^4`. `np.roots`
on `g'(x) = 4*x^3`'s coefficients gives a single critical point at
`x = 0` — but `g''(0) = 0`, so the second-derivative test is
indeterminate there. Plot `g` anyway: is `x = 0` actually a minimum,
a maximum, or neither? What does this tell you about trusting the
test blindly?

## Saddle or Bowl?

**Skills:** gradient, Hessian, positive/negative-definite matrices,
`np.linalg.eigvalsh`, Sylvester's Criterion, 3D/contour
visualization.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `np.linalg.eigvalsh` returns the eigenvalues of a symmetric
matrix, sorted, as real numbers. For a `2x2` Hessian `H`, Sylvester's
Criterion only needs `D_1 = H[0,0]` and `D_2 = det(H)`.

### Paper Problem

Two functions share the same critical point but are shaped
differently: the saddle `f(x, y) = x^2 - y^2` and the bowl
`g(x, y) = x^2 + 2*y^2`. For each:

* Compute the gradient `∇f` (or `∇g`). Confirm `(0, 0)` is a
  critical point — the gradient is the zero vector there.
* Compute the Hessian `H` by hand (it's constant for both
  functions, since neither has any cubic or higher terms).
* Classify `H` with Sylvester's Criterion: compute `D_1 = H[0,0]`
  and `D_2 = det(H)`, then read off positive definite / negative
  definite / indefinite from their signs.

### Coding Exercise

* Build each Hessian as a NumPy array: `H_saddle` for `f`, `H_bowl`
  for `g`.
* Classify each two ways — `np.linalg.eigvalsh(H)`'s signs, and
  Sylvester's Criterion (`D_1`, `D_2`) from the Paper Problem — and
  confirm both approaches agree.
* Visualize both functions (a 3D surface via
  `ax.plot_surface(...)`, or a contour plot) over a small grid
  around the origin, marking `(0, 0)` on each. Does the picture
  match "saddle" and "bowl"?

**Stretch goal:** Classify `h(x, y) = x^2` (no `y` term at all).
What do the eigenvalues and Sylvester's Criterion say about `H` —
positive definite, negative definite, indefinite, or something
else? Plot it and explain what you see along the `y` direction.

## Help

Copy this once and reuse it to plot a curve with several marked,
labeled critical points:

```python
def plot_curve_with_critical_points(f, xr, points, labels):
    """Plot f over xr and mark each (point, f(point)) with a label."""
    xs = np.linspace(*xr, 200)
    plt.plot(xs, f(xs), color='C0')
    for i, (x_star, label) in enumerate(zip(points, labels)):
        plt.scatter([x_star], [f(x_star)], color=f'C{i + 1}', zorder=3)
        plt.annotate(label, (x_star, f(x_star)))
```

Copy this once and reuse it to plot a two-variable function's
surface with a marked critical point:

```python
def plot_surface_with_point(f, xr, yr, point, label, n=50):
    """Plot f's surface over xr/yr and mark (point, f(*point))."""
    xs = np.linspace(*xr, n)
    ys = np.linspace(*yr, n)
    X, Y = np.meshgrid(xs, ys)
    Z = f(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, alpha=0.6, cmap='viridis')
    ax.scatter(*point, f(*point), color='C1', s=50)
    ax.set_title(label)
```

Don't just eyeball the classifications — let the asserts confirm
them:

```python
def central_diff(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

f = lambda x: x**3 - 3*x
roots = np.sort(np.roots([3, 0, -3]).real)
assert np.allclose(roots, [-1.0, 1.0])

fprime = lambda x: central_diff(f, x)
assert central_diff(fprime, roots[0]) < 0  # x = -1: local max
assert central_diff(fprime, roots[1]) > 0  # x = 1: local min

def sylvester_classify(H):
    d1, d2 = H[0, 0], np.linalg.det(H)
    if d1 > 0 and d2 > 0:
        return 'positive definite'
    if d1 < 0 and d2 > 0:
        return 'negative definite'
    if d2 < 0:
        return 'indefinite'
    return 'semidefinite'

def eig_classify(H):
    eigs = np.linalg.eigvalsh(H)
    if np.all(eigs > 0):
        return 'positive definite'
    if np.all(eigs < 0):
        return 'negative definite'
    if np.any(eigs > 0) and np.any(eigs < 0):
        return 'indefinite'
    return 'semidefinite'

H_saddle = np.array([[2.0, 0.0], [0.0, -2.0]])
H_bowl = np.array([[2.0, 0.0], [0.0, 4.0]])

assert sylvester_classify(H_saddle) == eig_classify(H_saddle) == (
    'indefinite'
)
assert sylvester_classify(H_bowl) == eig_classify(H_bowl) == (
    'positive definite'
)
```
