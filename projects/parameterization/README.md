# Parameterization — Exercise

## Walking Through a Surface

**Skills:** parameterizing a line `r(t) = p + t·u`, reducing a
two-variable function to a single-variable slice `g(t) = f(r(t))`,
numerical derivatives via finite differences.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: a central difference, `(g(t+h) - g(t-h)) / (2*h)`, estimates
`g'(t)` numerically — useful for checking a hand-derived slope
without touching symbolic algebra.

### Paper Problem

For `f(x, y) = x^2 + 4*y^2`, starting point `p = (1, 0)`, and
direction `u = (0, 1)`, write `r(t) = p + t·u` and find
`g(t) = f(r(t))`. Compute `g'(0)` by hand and describe in words what
it tells you about `f` at `(1, 0)`, walking in the `u` direction.

### Coding Exercise

* Define `f = lambda x, y: x**2 + 4*y**2` and `p = np.array([1.0,
  0.0])`.
* Pick three directions: `u1 = np.array([1.0, 0.0])`,
  `u2 = np.array([0.0, 1.0])`, and
  `u3 = np.array([1.0, 1.0]) / np.sqrt(2)`.
* For each direction `u`, define `g = lambda t: f(*(p + t * u))` and
  plot `g(t)` over `t` in `[-1, 1]` — three separate 1-D curves,
  each one the surface `f` collapsed along a different path through
  `p`.
* For the `u2 = (0, 1)` direction, estimate `g'(0)` numerically with
  a central difference and compare against your hand-derived answer
  from the Paper Problem.
* Plot all three `g(t)` curves on the same axes, one color per
  direction, with a legend — notice they all pass through `g(0) =
  f(p)`, but look different beyond `t = 0` since each one walks
  through the surface a different way.

**Stretch goal:** Add a fourth direction of your choosing and repeat
the numerical-derivative check at `t = 0`. Does `g'(0)` change with
the direction you walk?

## Help

Copy this once and reuse it to plot the 1-D slice traced out by
walking a 2-variable function along a direction:

```python
def plot_slice(f, p, u, trange=(-1, 1), n=100, ax=None, label=None):
    """Plot g(t) = f(p + t*u) over trange, the 1-D slice of f along
    the line through p in direction u."""
    if ax is None:
        _, ax = plt.subplots()
    ts = np.linspace(*trange, n)
    p, u = np.asarray(p), np.asarray(u)
    gs = [f(*(p + t * u)) for t in ts]
    ax.plot(ts, gs, label=label)
    return ax
```

Don't just eyeball that every slice starts at the same height — let
the asserts confirm it:

```python
f = lambda x, y: x**2 + 4 * y**2
p = np.array([1.0, 0.0])
directions = [
    np.array([1.0, 0.0]),
    np.array([0.0, 1.0]),
    np.array([1.0, 1.0]) / np.sqrt(2),
]

for u in directions:
    g = lambda t, u=u: f(*(p + t * u))
    assert np.isclose(g(0.0), f(*p))  # every slice passes through f(p) at t=0

g = lambda t: f(*(p + t * np.array([0.0, 1.0])))
g_prime_0 = (g(1e-5) - g(-1e-5)) / 2e-5
assert np.isclose(g_prime_0, 0.0, atol=1e-3)  # matches the Paper Problem
```
