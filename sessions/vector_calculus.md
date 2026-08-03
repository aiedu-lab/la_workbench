# Vector Calculus

## Concept

### Motivation

A scalar field assigns one number to every point in space (an
elevation, a temperature, a pixel's brightness); a vector field
assigns a whole vector to every point (a force, a flow, a velocity).
Vector calculus is the toolkit for asking how such fields change
from point to point, and it shows up everywhere: in **physics**,
mapping an electric or gravitational potential to the field it
produces; in **signal and image processing**, detecting an edge by
measuring how sharply brightness changes across neighboring pixels;
and in **machine learning and AI**, walking downhill on a loss
surface via gradient descent. The three tools below — gradient,
divergence, and curl — are the three fundamental ways a field can
change.

### Gradient

**Purpose:** the gradient tracks the maximum rate and direction of
increase of a scalar field. It's the same `∇f` introduced in
[Partial Derivatives and Multivariate Calculus](
  partial_derivatives_multivariate_calculus.md
), now framed as one instance of a broader family of field
operators.

**Definition:** the gradient maps a scalar field to a vector field —
one output vector per input point:

```
∇f = (∂f/∂x) î + (∂f/∂y) ĵ + (∂f/∂z) k̂
```

**Applications:**

* **Physics** — mapping electric potential to electric field,
  gravitational potential to gravitational field.
* **Machine learning** — gradient descent updates model weights by
  moving in the *opposite* direction of the loss function's
  gradient, to minimize the error between prediction and ground
  truth.
* **Computer vision** — powers edge detection in image processing;
  software computes brightness gradients across pixels to locate
  sharp intensity transitions (edges).

**Paper Problem:** for `f(x, y) = x^2 + y^2` (a bowl-shaped scalar
field), compute `∇f = (2x, 2y)` and evaluate it by hand at the point
`(1, 2)`, giving `∇f(1, 2) = (2, 4)`. Notice this vector points
straight away from the origin — radially outward, the steepest-ascent
direction — and is perpendicular to the circle `x^2 + y^2 = 5`, the
level curve through `(1, 2)`. That perpendicularity is not a
coincidence: the gradient always points across level curves, never
along them, because moving *along* a level curve keeps `f` constant.
