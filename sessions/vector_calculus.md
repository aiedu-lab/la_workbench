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

### Gradient — $\vec{\nabla} f$

**Purpose:** the gradient tracks the maximum rate and direction of
increase of a scalar field. It's the same $\vec{\nabla} f$
introduced in [Partial Derivatives and Multivariate Calculus](
  partial_derivatives_multivariate_calculus.md
), now framed as one instance of a broader family of field
operators.

**Definition:** the gradient maps a scalar field to a vector field —
one output vector per input point:

$$
\vec{\nabla} f = \frac{\partial f}{\partial x}\hat{i} +
\frac{\partial f}{\partial y}\hat{j} +
\frac{\partial f}{\partial z}\hat{k}
$$

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
field), compute $\vec{\nabla} f = (2x, 2y)$ and evaluate it by hand
at the point `(1, 2)`, giving $\vec{\nabla} f(1, 2) = (2, 4)$.
Notice this vector points straight away from the origin — radially
outward, the steepest-ascent direction — and is perpendicular to the
circle `x^2 + y^2 = 5`, the level curve through `(1, 2)`. That
perpendicularity is not a coincidence: the gradient always points
across level curves, never along them, because moving *along* a
level curve keeps `f` constant.

### Divergence — $\vec{\nabla} \cdot \vec{\mathbf{F}}$

**Purpose:** divergence measures the net flow of a vector field out
of a specific point — whether that point acts as a source (flow
emanates from it) or a sink (flow converges into it) — and the
aggregate strength of that outflow.

**Definition:** unlike the gradient, divergence maps a vector field
to a *scalar* field — one output number per input point:

$$
\vec{\nabla} \cdot \vec{\mathbf{F}} = 
\frac{\partial F_x}{\partial x} + 
\frac{\partial F_y}{\partial y} + 
\frac{\partial F_z}{\partial z}
$$

**Applications:**

* **Fluid dynamics** — enforces mass conservation via the continuity
  equation. For an incompressible fluid like water, the divergence
  of the velocity field is zero everywhere
  ($\vec{\nabla} \cdot \vec{\mathbf{v}} = 0$): whatever flows into a
  region must flow back out.
* **Electrostatics** — forms the basis of Gauss's Law, one of
  Maxwell's equations. The divergence of an electric field equals
  the local charge density: positive charges are sources, negative
  charges are sinks.

**Paper Problem:** compare two vector fields at the origin. For
$\vec{\mathbf{F}}(x, y) = (x, y)$ (flowing straight outward from
every point), $\vec{\nabla} \cdot \vec{\mathbf{F}} = \partial x /
\partial x + \partial y / \partial y = 1 + 1 = 2$ — a positive
constant, confirming every point is a source. For
$\vec{\mathbf{F}}(x, y) = (-y, x)$ (pure rotation around the
origin), $\vec{\nabla} \cdot \vec{\mathbf{F}} = \partial(-y) /
\partial x + \partial x / \partial y = 0 + 0 = 0$ — the field is
divergence-free: it swirls, but nothing is created or destroyed at
any point.

### Curl — $\vec{\nabla} \times \vec{\mathbf{F}}$

**Purpose:** curl measures the rotation, or swirling intensity, of a
vector field around a specific point.

**Definition:** curl maps a vector field to another vector field —
the axis and strength of local rotation at each point — computed as
a symbolic determinant:

$$
\vec{\nabla} \times \vec{\mathbf{F}} =
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} &
\dfrac{\partial}{\partial z} \\
F_x & F_y & F_z
\end{vmatrix}
$$

**Applications:**

* **Electromagnetism** — powers Faraday's Law and Ampère's Law
  (two more of Maxwell's equations). A changing magnetic field
  induces a curling electric field, which is how electric
  generators produce power.
* **Computer graphics** — simulates realistic smoke, fire, and water
  eddies; real-time physics engines use curl noise to generate
  turbulent, swirling fluid effects without heavy computational
  overhead.

**Paper Problem:** compare the same rotational field from the
Divergence problem, $\vec{\mathbf{F}}(x, y, 0) = (-y, x, 0)$,
against the purely radial field
$\vec{\mathbf{F}}(x, y, 0) = (x, y, 0)$. Expanding the determinant
above, the rotational field gives
$\vec{\nabla} \times \vec{\mathbf{F}} = (0, 0, 2)$ — a nonzero
$\hat{k}$ component confirming genuine spin around the `z`-axis —
while the radial field gives
$\vec{\nabla} \times \vec{\mathbf{F}} = (0, 0, 0)$: it flows
straight out in every direction, with no rotation at all. Together
with the Divergence problem, this pair of fields shows divergence
and curl capturing two independent, complementary properties: one
field has zero divergence and nonzero curl, the other has the
reverse.

## Reference

* [Vector calculus video](https://www.youtube.com/watch?v=lKXW7DRyyro)
  — a worked visual introduction to gradient, divergence, and curl.
* Khan Academy's Multivariable Calculus course, ["Divergence and
  curl" unit](
    https://www.khanacademy.org/math/multivariable-calculus
  ) — free, widely-used video lessons and articles on exactly these
  three operators.
* ***Div, Grad, Curl, and All That: An Informal Text on Vector
  Calculus*** by H. M. Schey — a classic, highly-rated book that
  builds physical intuition for these operators from electromagnetic
  field examples, without getting lost in formalism.

## Exercise

Work through all three exercises in [Vector Calculus](
  ../projects/vector_calculus/
) in a Jupyter or Colab notebook: **Steepest Ascent** — numerically
confirming the gradient's direction against the Gradient Paper
Problem; **Source or Sink?** — numerically confirming divergence's
sign against the Divergence Paper Problem; and **Does It Spin?** —
numerically confirming curl against the Curl Paper Problem.
