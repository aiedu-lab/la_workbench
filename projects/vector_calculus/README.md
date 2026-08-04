# Vector Calculus — Exercise

## Steepest Ascent

**Skills:** central-difference partial derivatives, `np.meshgrid`,
quiver plots over a contour/heatmap.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: a central difference estimates a partial derivative from two
nearby samples — `∂f/∂x ~= (f(x+h, y) - f(x-h, y)) / (2*h)` — and
works the same way for `∂f/∂y` by nudging `y` instead.

* Define `f(x, y) = x**2 + y**2` as a Python function, and build a
  grid of points with `np.meshgrid` over `x, y` in `[-3, 3]`.
* At every grid point, numerically estimate $∂f/∂x$ and $∂f/∂y$ with
  the central-difference formula above (a small `h`, e.g. `1e-3`,
  works well).
* Plot a contour or heatmap of `f` over the grid
  (`plt.contourf` or `plt.pcolormesh`), then overlay the numerical
  gradient vectors with `plt.quiver`.
* Read off your numerical gradient at `(1, 2)` and compare it to the
  hand-computed value from the session's Gradient Paper Problem,
  `∇f(1, 2) = (2, 4)`. Confirm the arrows all point radially
  outward, away from the bowl's bottom.

**Stretch goal:** repeat for the saddle `f(x, y) = x**2 - y**2`.
Unlike the bowl, the gradient arrows now point *outward* along `x`
but *inward* along `y` — sketch by hand where you'd expect the
arrows to vanish entirely, then check your numerical plot agrees.

## Source or Sink?

**Skills:** central-difference divergence, quiver plots colored by a
scalar field.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: divergence sums the central-difference estimates of
$∂F_x/∂x$ and $∂F_y/∂y$ at each point — reuse the central-difference
formula from Steepest Ascent, applied to each component of 
$\vec{\mathbf{F}}$ separately.

* Define two vector fields as Python functions returning
  $[F_x\hat{i}, F_y\hat{j}]$: the radial field 
  $\vec{\mathbf{F}}(x, y) = [x\hat{i}, y\hat{j}]$ and the 
  rotational field 
  $\vec{\mathbf{F}}(x, y) = [-y\hat{i}, x\hat{j}]$.
* Build a grid with `np.meshgrid`, then numerically estimate the
  divergence `∇.F` at every grid point for both fields.
* Visualize each field with `plt.quiver`, colored by its local
  divergence value (pass `divergence.ravel()` as the quiver's color
  argument, or underlay a `plt.pcolormesh` of the divergence).
* Confirm the radial field's divergence is uniformly close to `2`
  and the rotational field's divergence is uniformly close to `0`,
  matching the session's Divergence Paper Problem.

**Stretch goal:** try 
$\vec{\mathbf{F}}(x, y) = [x^2\hat{i}, y\hat{j}]$. 
Its divergence is no longer constant across the grid — where 
is it largest, and does that match where the field's arrows 
spread apart fastest?

## Does It Spin?

**Skills:** central-difference 2D scalar curl, `plt.streamplot`.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: in two dimensions, curl collapses to a single scalar,
$∂F_y/∂x - ∂F_x/∂y$ — the `z`-component of the full 3D curl from the
session, since a 2D field has no `z`-dependence.

* Reuse the radial field 
  $\vec{\mathbf{F}}(x, y) = [x\hat{i}, y\hat{j}]$ and the rotational field 
  $\vec{\mathbf{F}}(x, y) = [-y\hat{i}, x\hat{j}]$ from Source or Sink?.
* Numerically estimate the 2D scalar curl at every grid point for
  both fields, using central differences on $F_x$ and $F_y$.
* Visualize each field with `plt.streamplot(X, Y, U, V)` — the
  streamlines should visibly circle for one field and flow straight
  for the other.
* Confirm the rotational field's curl is uniformly close to `2` and
  the radial field's curl is uniformly close to `0`, matching the
  session's Curl Paper Problem.

**Stretch goal:** try the shear field 
$\vec{\mathbf{F}}(x, y) = [y\hat{i}, 0\hat{j}]$. Its
streamlines look like they're sliding sideways, not circling — yet
compute its curl. What does the nonzero result tell you about "spin"
that the picture alone doesn't?

## Help

Copy this once and reuse it to draw a vector field, optionally
colored by an underlying scalar (divergence or curl) value:

```python
def plot_vector_field(X, Y, U, V, scalar=None):
    """Quiver-plot a vector field; optionally color arrows by scalar."""
    if scalar is not None:
        plt.quiver(X, Y, U, V, scalar, cmap='coolwarm')
        plt.colorbar()
    else:
        plt.quiver(X, Y, U, V)
    plt.gca().set_aspect('equal')
```

Don't just trust your numerical estimates — check them against the
hand-derived closed forms from the session's paper problems:

```python
def central_diff(f, x, y, h=1e-5, wrt='x'):
    if wrt == 'x':
        return (f(x + h, y) - f(x - h, y)) / (2 * h)
    return (f(x, y + h) - f(x, y - h)) / (2 * h)

f = lambda x, y: x**2 + y**2
grad = np.array([
    central_diff(f, 1.0, 2.0, wrt='x'),
    central_diff(f, 1.0, 2.0, wrt='y'),
])
assert np.allclose(grad, [2.0, 4.0], atol=1e-3)

F_radial = lambda x, y: (x, y)
F_rotational = lambda x, y: (-y, x)


def divergence(F, x, y, h=1e-5):
    dFx_dx = (F(x + h, y)[0] - F(x - h, y)[0]) / (2 * h)
    dFy_dy = (F(x, y + h)[1] - F(x, y - h)[1]) / (2 * h)
    return dFx_dx + dFy_dy


def curl_2d(F, x, y, h=1e-5):
    dFy_dx = (F(x + h, y)[1] - F(x - h, y)[1]) / (2 * h)
    dFx_dy = (F(x, y + h)[0] - F(x, y - h)[0]) / (2 * h)
    return dFy_dx - dFx_dy


assert np.isclose(divergence(F_radial, 0.5, -0.5), 2.0, atol=1e-3)
assert np.isclose(divergence(F_rotational, 0.5, -0.5), 0.0, atol=1e-3)
assert np.isclose(curl_2d(F_rotational, 0.5, -0.5), 2.0, atol=1e-3)
assert np.isclose(curl_2d(F_radial, 0.5, -0.5), 0.0, atol=1e-3)
```
