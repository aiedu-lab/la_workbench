# Systems of Linear Equations — Exercise

## The Snack Bar Mystery

**Skills:** systems of linear equations, `Ax = b`, intersection of
lines, singular matrices.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `np.linalg.solve`, `np.linalg.det`. After plotting, call
`plt.gca().set_aspect('equal')` so shapes aren't squished.

At the school snack bar, 2 samosas + 3 juices cost ₹37, and 3
samosas + 2 juices cost ₹38.

* Write this as a matrix equation `A x = b`, then solve for the
  price of one samosa and one juice with `np.linalg.solve`.
* Each equation is a straight line. Plot both lines and mark where
  they cross — confirm the crossing matches your solution.
* Change the prices so the two lines become parallel (make one
  equation a multiple of the other). What does `np.linalg.det(A)`
  give now, and what happens when you try to solve?

**Stretch goal:** A creature collection has chickens (2 legs),
goats (4 legs), and spiders (8 legs): 12 heads, 42 legs in total,
and 2 more chickens than all the other creatures combined. Set up
the 3×3 system and solve it.

## Gaussian Elimination

**Skills:** elementary row operations, forward elimination,
back-substitution, solving `Ax = b` without a black-box solver.

Work through this right after The Snack Bar Mystery above — same
system, solved by hand this time.

Setup cell:

```python
import numpy as np
```

Handy: subtract a multiple of one row from another to zero out an
entry; `np.linalg.solve` is your ground truth to check against.

Reuse the snack bar system: 2 samosas + 3 juices cost ₹37, and 3
samosas + 2 juices cost ₹38.

* Write the augmented matrix `[A | b]` by hand as a NumPy array.
* Eliminate the first variable from row 2: subtract a multiple of
  row 1 from row 2 so its first entry becomes `0`.
* Back-substitute from the resulting upper-triangular system to
  find the price of one juice, then one samosa.
* Compare your hand-solved prices against `np.linalg.solve(A, b)`
  — they should match exactly.

**Stretch goal:** Scale your elimination up to a bigger system —
`solutions/elimination/sidk256/` in this exercise's `solutions/`
folder row-reduces a full 6-variable, 6-equation system the same
way; try extending your steps to that size.

## Help

Copy this once and reuse it to draw both equations as lines — no
need to write plotting boilerplate from scratch:

```python
def plot_lines(A, b, xlim=(-5, 5)):
    """Plot each row of `A x = b` as a straight line."""
    xs = np.linspace(*xlim, 2)
    for row, rhs in zip(A, b):
        ys = (rhs - row[0] * xs) / row[1]
        plt.plot(xs, ys)
    plt.gca().set_aspect('equal')
```

Don't just eyeball where the lines cross — let the assert confirm
your solution satisfies both equations:

```python
A = np.array([[2, 3], [3, 2]])
b = np.array([37, 38])
x = np.linalg.solve(A, b)
assert np.allclose(A @ x, b)
```

Whatever hand-rolled elimination steps you took, the final answer
must agree with the black-box solver:

```python
x_manual = np.array([8.0, 7.0])  # <- replace with your own result
assert np.allclose(x_manual, np.linalg.solve(A, b))
```
