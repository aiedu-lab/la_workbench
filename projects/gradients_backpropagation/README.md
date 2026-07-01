# Learning from Mistakes: Gradients and Backpropagation — Exercise

## Rolling Downhill

**Skills:** gradient descent, loss function, derivatives as
"downhill direction."

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `np.meshgrid` to build a grid for a contour plot. After
plotting, call `plt.gca().set_aspect('equal')` so the bowl isn't
distorted.

The loss `loss(w) = (w0 - 3)**2 + (w1 + 2)**2` is a bowl with its
minimum at `w = [3, -2]`. Its gradient is
`grad(w) = [2 * (w0 - 3), 2 * (w1 + 2)]`.

* Starting at `w = [0, 0]` with learning rate `0.1`, predict
  whether 20 steps of `w = w - lr * grad(w)` will land close to
  the minimum `[3, -2]`.
* Run the 20 steps, recording every `w` visited as `path`. Plot
  `loss(w)` at each step — it should decrease every iteration.
* Plot the loss as a contour over a grid of `(w0, w1)` values, with
  the descent path drawn on top.

**Stretch goal:** Repeat with learning rate `1.1` instead of `0.1`.
What happens to the path, and why does a too-large learning rate
break gradient descent?

## Help

Copy this once and reuse it to see the bowl and the path together
— no need to write contour boilerplate from scratch:

```python
def plot_descent(loss_fn, path, extent=6):
    """Contour of `loss_fn` over a grid, with `path` overlaid."""
    grid = np.linspace(-extent, extent, 100)
    w0, w1 = np.meshgrid(grid, grid)
    z = loss_fn(np.stack([w0, w1]))
    plt.contour(w0, w1, z, levels=20)
    path = np.array(path)
    plt.plot(path[:, 0], path[:, 1], 'o-', color='C1')
    plt.gca().set_aspect('equal')
```

Don't just eyeball the descent — let the assert confirm the loss
actually dropped:

```python
def loss_fn(w):
    return (w[0] - 3) ** 2 + (w[1] + 2) ** 2

def grad_fn(w):
    return np.array([2 * (w[0] - 3), 2 * (w[1] + 2)])

w = np.array([0.0, 0.0])
path = [w.copy()]
for _ in range(20):
    w = w - 0.1 * grad_fn(w)
    path.append(w.copy())

assert loss_fn(path[-1]) < loss_fn(path[0])
```
