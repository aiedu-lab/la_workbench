# Column Space, Rank and Linear Independence — Exercise

## Which Directions Can I Reach?

**Skills:** column space as "every reachable output", rank,
`np.linalg.matrix_rank`, linear independence.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `np.linalg.matrix_rank`, `np.linalg.lstsq`. After plotting,
call `plt.gca().set_aspect('equal')` so directions aren't distorted.

Two redundant sensors report `A_dep = [[1, 2], [2, 4]]` — sensor 2
always reads exactly twice sensor 1.

* Predict: are `A_dep`'s two columns independent? Confirm with
  `np.linalg.matrix_rank(A_dep)`.
* Test whether `b1 = [3, 6]` is reachable (some `x` solves
  `A_dep x = b1`) by comparing `np.linalg.matrix_rank(A_dep)` to
  `np.linalg.matrix_rank(np.column_stack([A_dep, b1]))` — equal
  ranks mean `b1` is in the column space.
* Repeat for `b2 = [3, 5]`. Which one is unreachable, and why does
  it make sense given the two sensors are redundant?
* Plot the column space (a line through the origin, direction
  `[1, 2]`) and mark `b1` and `b2` — which one lands on the line?

Now a 3-sensor system, `A32 = [[1, 0], [0, 1], [1, 1]]`, where
sensor 3 always reads sensor 1 plus sensor 2.

* Predict whether `b3 = [2, 3, 5]` is reachable (check: does
  `5 == 2 + 3`?). Solve with `np.linalg.lstsq(A32, b3)` and confirm
  the residual is ~0.
* Repeat for `b4 = [2, 3, 1]`. This one should NOT be reachable —
  confirm the residual is clearly nonzero.

**Stretch goal:** `A_dep` has rank 1, so its column space is
exactly the line through `[1, 2]`. Write the general formula for
every reachable `b = [b0, b1]` in terms of a single free variable.

## Help

Copy this once and reuse it to draw the column space of a
rank-deficient 2x2 matrix — no need to write plotting boilerplate
from scratch:

```python
def plot_span_2d(direction, targets=None, labels=None, extent=8):
    """Draw the line spanned by `direction` and mark target points."""
    t = np.linspace(-extent, extent, 2)
    line = np.outer(t, direction)
    plt.plot(line[:, 0], line[:, 1], color='C0')
    if targets is not None:
        for i, pt in enumerate(targets):
            plt.scatter(*pt, color='C1')
            if labels:
                plt.annotate(labels[i], pt)
    plt.gca().set_aspect('equal')
```

Don't just eyeball reachability — let the assert confirm it:

```python
A_dep = np.array([[1, 2], [2, 4]])
b1 = np.array([3, 6])
x_lstsq, *_ = np.linalg.lstsq(A_dep, b1, rcond=None)
assert np.allclose(A_dep @ x_lstsq, b1)  # b1 is reachable

b2 = np.array([3, 5])
assert np.linalg.matrix_rank(A_dep) != np.linalg.matrix_rank(
    np.column_stack([A_dep, b2])
)  # b2 is NOT reachable
```
