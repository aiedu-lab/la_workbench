# Orthogonality and Projections — Exercise

## Shadow on the Wall

**Skills:** projection formula, projection matrix, orthogonality,
residual vectors.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `a @ b` for the dot product, `np.outer` for building a
projection matrix. After plotting, call
`plt.gca().set_aspect('equal')` so angles aren't distorted.

A vector `v = [3, 4]` casts a "shadow" onto the line through
`a = [2, 1]`.

* Predict, roughly, where the shadow lands on the line — closer to
  the origin or past the tip of `a`?
* Compute the projection with the formula
  `proj = (v @ a / (a @ a)) * a`.
* Compute the residual `v - proj` — the part of `v` that's left
  over. Confirm it's orthogonal to `a` by checking the dot product
  is (nearly) zero.
* Plot the line through `a`, the vector `v`, its shadow `proj`, and
  a dashed segment connecting the tip of `v` to `proj` (the
  residual).

**Stretch goal:** Build the projection matrix
`P = np.outer(a, a) / (a @ a)` directly and confirm `P @ v` gives
the same `proj`. Then confirm `P @ P` equals `P` — projecting twice
lands you in the same place as projecting once.

## Help

Copy this once and reuse it to draw the shadow picture — no need
to write plotting boilerplate from scratch:

```python
def plot_projection(v, a, proj, extent=6):
    """Draw the line through `a`, vector `v`, its shadow `proj`,
    and the residual connecting them."""
    t = np.linspace(-extent, extent, 2)
    line = np.outer(t, a)
    plt.plot(line[:, 0], line[:, 1], color='C0', alpha=0.4)
    plt.quiver(0, 0, *v, color='C1', angles='xy', scale_units='xy',
               scale=1)
    plt.quiver(0, 0, *proj, color='C2', angles='xy',
               scale_units='xy', scale=1)
    plt.plot([v[0], proj[0]], [v[1], proj[1]], 'k--')
    plt.gca().set_aspect('equal')
```

Don't just eyeball the right angle — let the assert confirm it:

```python
v = np.array([3, 4])
a = np.array([2, 1])
proj = (v @ a / (a @ a)) * a
residual = v - proj
assert np.isclose(residual @ a, 0)
```
