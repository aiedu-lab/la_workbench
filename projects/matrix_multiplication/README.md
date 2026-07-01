# Matrix Multiplication — Exercise

## Build a Flower with Rotations

**Skills:** rotation matrices, the angle-matrix connection, loops,
composition.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `A @ B` multiplies matrices. After plotting, call
`plt.gca().set_aspect('equal')` so shapes aren't squished.

Start with one small, lopsided "petal" shape near the origin.

* Write a function `rot(deg)` that returns the 2×2 rotation matrix
  for a given angle in degrees.
* Test it first: rotate the point `(1, 0)` by 90° and confirm you
  get `(0, 1)`.
* Use a loop to rotate the petal by 0°, 45°, 90°, ... up to 360°,
  plotting each copy. You should get a symmetric flower.
* Experiment with the angle step. What step angle gives exactly 8
  petals? Exactly 12?

**Stretch goal:** Rotating by 30° twice should equal rotating by
60° once. Verify this with matrix multiplication: is
`rot(30) @ rot(30)` the same as `rot(60)`?

## Help

Copy this once and reuse it to draw the petal at every angle — no
need to write scatter/line boilerplate from scratch:

```python
def plot_shape(points, ax=None, color='C0'):
    """Plot a 2 x N shape as a closed outline."""
    ax = ax or plt.gca()
    closed = np.hstack([points, points[:, :1]])
    ax.plot(closed[0], closed[1], color=color)
    ax.set_aspect('equal')
```

Don't just eyeball the composition claim — let the assert confirm
it:

```python
def rot(deg):
    t = np.radians(deg)
    return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

assert np.allclose(rot(30) @ rot(30), rot(60))
```
