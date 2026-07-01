# Linear Transformations — Exercise

Work through both parts in a Jupyter or Colab notebook. Run a
cell, predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `A @ B` multiplies matrices, `np.linalg.det` for the
determinant. After plotting, call `plt.gca().set_aspect('equal')`
so shapes aren't squished.

## Part 1 — Resize the Rocket

**Skills:** dilation (scaling) matrices, matrix × points,
determinant as area factor.

You're given a small rocket drawn as a set of 2-D points stored as
the columns of a 2 × N matrix.

* Build a dilation matrix that makes the rocket twice as tall but
  half as wide, then apply it to the shape with `@`.
* Before running it, predict by hand where the nose-tip point
  `(0, 6)` lands. Then check.
* Plot the original and the resized rocket on the same axes
  (remember equal aspect ratio).
* Compute `np.linalg.det` of your scaling matrix. How does that
  number relate to how the rocket's area changed?

**Stretch goal:** Find a single matrix that doubles the area but
keeps the same shape (just bigger). What does its determinant
equal?

## Part 2 — Make It Lean (Shear)

**Skills:** shear transformations, which coordinates move,
determinant and area.

Take an upright block letter "F" stored as a set of points.

* Build a horizontal shear matrix `[[1, k], [0, 1]]` and apply it
  to slant the letter into an italic version. Try `k = 0.5` first.
* Plot upright vs. sheared on the same axes. Which coordinate of
  each point changes, and which stays fixed?
* Create a "shadow" effect: draw the original in solid black and a
  sheared, faint-gray copy behind it.
* Predict whether shearing changes the shape's area, then test
  your guess with `np.linalg.det` of the shear matrix.

**Stretch goal:** Combine a shear and a rotation by multiplying
the two matrices. Does the order matter? Compare `S @ R` with
`R @ S`.

## Help

Copy this once and reuse it for both parts — no need to write
scatter/line boilerplate from scratch:

```python
def plot_points(points, ax=None, color='C0', label=None):
    """Plot a 2 x N shape as a closed outline."""
    ax = ax or plt.gca()
    closed = np.hstack([points, points[:, :1]])
    ax.plot(closed[0], closed[1], color=color, label=label)
    ax.set_aspect('equal')
```

Don't just eyeball the area change — let the determinant confirm
your prediction:

```python
# Part 1: half as wide, twice as tall — area factor is det(A)
A = np.array([[0.5, 0], [0, 2]])
assert np.isclose(np.linalg.det(A), 1.0)  # width x height cancels

# Part 2: any shear [[1, k], [0, 1]] preserves area exactly
shear = np.array([[1, 0.5], [0, 1]])
assert np.isclose(np.linalg.det(shear), 1.0)
```
