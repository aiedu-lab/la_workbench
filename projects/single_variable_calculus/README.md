# Single-Variable Calculus — Exercise

## Down to the Valley Floor

**Skills:** derivative as slope, critical points via `f'(x) = 0`,
the first-/second-derivative test, numerical derivatives via
finite differences, and a simple 1D gradient-descent loop.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `np.linspace` for plotting, a central difference for
numerical derivatives. Plot the curve before touching any
derivative code — seeing the shape makes the critical point
obvious.

### Paper Problem

By hand, for `f(x) = x^2 - 4x + 3`:

* Compute `f'(x)`. Set it to `0` and solve for the critical point
  `x*`.
* Compute `f''(x)`. Is it positive or negative at `x*`? What does
  that tell you about the critical point — minimum or maximum?
* Compute `f(x*)`.

### Coding Exercise

* Define `f(x) = x**2 - 4*x + 3` and plot it over `x` in
  `[-2, 6]`. Mark your hand-computed `x*` on the curve — does it
  land at the bottom of the bowl?
* Estimate `f'(x*)` numerically with a central difference,
  `(f(x*+h) - f(x*-h)) / (2*h)` for a small `h` (e.g. `1e-5`).
  Confirm it's close to `0`.
* Estimate `f''(x*)` numerically the same way, applied to your
  numerical `f'` instead of `f`. Confirm its sign matches your
  paper-problem answer.
* Starting from a different point (e.g. `x0 = 5.0`), run a small
  gradient-descent loop: repeat `x = x - lr * f'(x)` (using your
  numerical derivative) for a few dozen steps with a small learning
  rate `lr` (e.g. `0.1`). Track every `x` visited and plot the path
  on top of the curve. Does it end up at `x*`?

**Stretch goal:** Try a `lr` that's too large (e.g. `1.1`). What
happens to the path — does it still converge? This is the same
instability gradient descent runs into when training a real model
with too high a learning rate.

## Help

Copy this once and reuse it to plot a curve with a marked point —
no need to write plotting boilerplate from scratch:

```python
def plot_curve_with_point(f, xr, x_star, label='critical point'):
    """Plot f over xr and mark the point (x_star, f(x_star))."""
    xs = np.linspace(*xr, 200)
    plt.plot(xs, f(xs), color='C0')
    plt.scatter([x_star], [f(x_star)], color='C1', zorder=3)
    plt.annotate(label, (x_star, f(x_star)))
```

Don't just eyeball convergence — let the asserts confirm it:

```python
def central_diff(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

f = lambda x: x**2 - 4*x + 3
x_star = 2.0

assert abs(central_diff(f, x_star)) < 1e-3  # f'(x_star) ~ 0

fprime = lambda x: central_diff(f, x)
assert central_diff(fprime, x_star) > 0  # f''(x_star) > 0: min

x, lr = 5.0, 0.1
for _ in range(50):
    x = x - lr * central_diff(f, x)
assert abs(x - x_star) < 1e-2  # gradient descent converged
```
