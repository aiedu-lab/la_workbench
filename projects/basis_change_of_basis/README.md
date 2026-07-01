# Basis and Change of Basis — Exercise

## Describe It In My Coordinates

**Skills:** basis vectors, change of basis, `np.linalg.inv`,
`np.linalg.solve`.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `np.linalg.inv`, `np.linalg.solve`. After plotting, call
`plt.gca().set_aspect('equal')` so the grid isn't distorted.

Define a custom, non-standard basis with two vectors:
`b1 = [2, 1]` and `b2 = [-1, 1]`. Stack them as the columns of a
matrix `basis`.

* A point sits at `p = [3, 4]` in standard coordinates. Predict
  roughly how many `b1`s and `b2`s it would take to reach `p`, just
  by eye. Then solve `basis @ c = p` for the exact coordinates `c`
  with `np.linalg.solve`.
* Convert back: reconstruct `p` from `c` with `basis @ c` and
  confirm you get the original standard coordinates.
* Plot the custom basis grid (lines parallel to `b1` and `b2`,
  spaced at integer multiples) over the standard grid, and mark
  `p`. Which grid line intersection does `p` sit on?

**Stretch goal:** Pick a second point `q = [-1, 2]` and find its
coordinates in the same custom basis. Do `p`'s and `q`'s custom
coordinates add the same way their standard coordinates do?

## Help

Copy this once and reuse it to draw the custom basis grid — no
need to write plotting boilerplate from scratch:

```python
def plot_basis_grid(basis, extent=5):
    """Draw grid lines parallel to each column of `basis`."""
    b1, b2 = basis[:, 0], basis[:, 1]
    t = np.linspace(-extent, extent, 2)
    for k in range(-extent, extent + 1):
        line1 = np.outer(t, b1) + k * b2
        line2 = np.outer(t, b2) + k * b1
        plt.plot(line1[:, 0], line1[:, 1], color='C0', alpha=0.3)
        plt.plot(line2[:, 0], line2[:, 1], color='C1', alpha=0.3)
    plt.gca().set_aspect('equal')
```

Don't just eyeball the coordinates — let the assert confirm the
round trip:

```python
basis = np.array([[2, -1], [1, 1]])
point_standard = np.array([3, 4])
coords_in_basis = np.linalg.solve(basis, point_standard)
assert np.allclose(basis @ coords_in_basis, point_standard)
```
