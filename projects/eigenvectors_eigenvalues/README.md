# Eigenvectors and Eigenvalues (Conceptual) — Exercise

## Directions That Don't Turn

**Skills:** eigenvectors, eigenvalues, `np.linalg.eig`, repeated
transformation.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `np.linalg.eig` returns eigenvalues and eigenvectors. After
plotting, call `plt.gca().set_aspect('equal')` so angles aren't
distorted.

Take `A = [[2, 1], [1, 2]]` and four candidate vectors: `[1, 1]`,
`[1, -1]`, `[1, 0]`, `[0, 1]`.

* Apply `A` to each candidate and plot the vector before and after
  with an arrow each. Which candidates keep pointing the same
  direction (just longer or shorter), and which ones visibly turn?
* Apply `A` again to the already-transformed vectors (i.e. `A @ A
  @ v`). The non-eigenvector directions should visibly rotate
  toward one of the directions that didn't turn.
* Compute `np.linalg.eig(A)` to get the true eigenvectors and
  eigenvalues, and confirm they match the directions you found by
  eye.

**Stretch goal:** `A` is symmetric, so its eigenvectors are
orthogonal. Confirm this: compute the dot product between the two
eigenvectors `np.linalg.eig` returns and check it's ~0.

## Help

Copy this once and reuse it to compare a vector before and after
the transform — no need to write `quiver` boilerplate from
scratch:

```python
def plot_before_after(vecs, A, colors=None):
    """Draw each vector in `vecs` and its image `A @ v`."""
    colors = colors or ['C0'] * len(vecs)
    for i, v in enumerate(vecs):
        plt.quiver(0, 0, *v, color=colors[i], alpha=0.4,
                   angles='xy', scale_units='xy', scale=1)
        plt.quiver(0, 0, *(A @ v), color=colors[i],
                   angles='xy', scale_units='xy', scale=1)
    plt.gca().set_aspect('equal')
```

Don't just eyeball which directions don't turn — let the assert
confirm the eigenvector equation:

```python
A = np.array([[2, 1], [1, 2]])
eigvals, eigvecs = np.linalg.eig(A)
eigval, eigvec = eigvals[0], eigvecs[:, 0]
assert np.allclose(A @ eigvec, eigval * eigvec)
```
