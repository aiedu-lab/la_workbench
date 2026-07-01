# Forward Propagation (Inference) — Exercise

## One Neuron, Step by Step

**Skills:** weight matrix, bias, activation function, forward
pass.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `A @ x` for the matrix-vector product. After plotting, no
special aspect ratio is needed — this is a 1D curve, not a shape.

A single layer maps a 3-feature input to 2 outputs:
`x = [1.0, 2.0, 3.0]`, `W = [[0.2, -0.5, 1.0], [0.1, 0.3, -0.2]]`,
`b = [0.1, -0.2]`, with a ReLU activation
(`relu(z) = max(z, 0)`).

* By hand, compute the pre-activation `z = W @ x + b` for both
  output units. Write down your two numbers before running code.
* Write `forward(x, W, b, activation)` that computes
  `activation(W @ x + b)`, and confirm it matches your hand
  calculation once ReLU is applied.
* Plot the ReLU curve over `[-5, 5]` and mark where each of your
  two `z` values lands on it — which one gets zeroed out?

**Stretch goal:** Swap ReLU for `sigmoid(z) = 1 / (1 + exp(-z))`
and recompute the output. How does the output range change
compared to ReLU?

## Help

Copy this once and reuse it to see the shape of any activation
function — no need to write plotting boilerplate from scratch:

```python
def plot_activation(fn, xrange=(-5, 5)):
    """Plot an activation function over `xrange`."""
    xs = np.linspace(*xrange, 200)
    plt.plot(xs, fn(xs))
    plt.axhline(0, color='gray', linewidth=0.5)
```

Don't just eyeball the output — let the assert confirm your hand
calculation:

```python
def relu(z):
    return np.maximum(z, 0)

def forward(x, W, b, activation):
    return activation(W @ x + b)

x = np.array([1.0, 2.0, 3.0])
W = np.array([[0.2, -0.5, 1.0], [0.1, 0.3, -0.2]])
b = np.array([0.1, -0.2])
manual_expected = np.array([2.3, 0.0])
assert np.allclose(forward(x, W, b, relu), manual_expected)
```
