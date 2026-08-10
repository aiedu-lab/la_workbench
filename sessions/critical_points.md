# Critical Points and the Second Derivative Test

## Concept

### Optimization Overview

Given a continuous function, "optimizing" it means finding its
global maximum, global minimum, local maxima, local minima, and any
saddle points. That search always happens in two stages. **Stage
1** collects every *candidate* point: places where the function
could plausibly peak or bottom out — critical points (where the
derivative is zero or undefined), boundary points, and, if the
domain is unbounded, the behavior as the input runs off to
`+∞` or `-∞`. **Stage 2** compares the function's
value at every candidate: the largest value found is the global
maximum, the smallest is the global minimum.

```mermaid
flowchart TD
    A[Continuous function f] --> B[Stage 1: find candidates]
    B --> C[Critical points: derivative 0 or undefined]
    B --> D[Boundary points]
    B --> E["Limits at ±∞, if unbounded"]
    C --> F[Stage 2: compare f at every candidate]
    D --> F
    E --> F
    F --> G[Largest value = global maximum]
    F --> H[Smallest value = global minimum]
```

This session zooms into the first stage's most interesting
candidates — critical points — and builds the tool that classifies
each one as a minimum, a maximum, or (once there's more than one
input) a saddle: the **second-derivative test**.

### Single Variable

For a function `f: R -> R`, a critical point occurs where

```
f'(a) = 0
```

(or where `f'(a)` doesn't exist). Geometrically, the tangent line
goes flat right there:

```
      ^
      |
      |      •
      |    /
------•------------------>
```

A critical point is only a *candidate* minimum or maximum — nothing
so far says which, or whether it's neither. To decide, look at how
`f` behaves in a small neighborhood around `a`. The **Taylor
expansion** describes exactly that: nudging `a` by a small step `h`,

```
f(a+h) - f(a) = f'(a)h + (1/2) f''(a) h^2 + ...
```

Read the two terms as two separate physical effects. The
first-order term, `f'(a)h`, says

```
change in f = slope x distance moved
```

— the same shape as `distance = speed x time`. The second-order
term captures something the first-order term misses: the slope
itself doesn't stay put as you move, it drifts at rate `f''(a)`.
Since that drift is approximately linear over a short step, the
*extra* contribution to the change in `f` is the area of a thin
triangle whose base is `h` and whose height is how much the slope
drifted, `f''(a)h`:

```
Slope

|
|      /
|     /
|____/_________

       h
```

```
area = (1/2)(base)(height) = (1/2) h (f''(a) h) = (1/2) f''(a) h^2
```

That's where the otherwise-mysterious `1/2` comes from — it's a
triangle's area formula (equivalently, the average slope over the
interval, since the slope ramps linearly from `f'(a)` to
`f'(a) + f''(a)h`).

**The second-derivative test.** At a critical point, `f'(a) = 0`,
so the Taylor expansion collapses to

```
f(a+h) - f(a) ~= (1/2) f''(a) h^2
```

Since `h^2 > 0` for every nonzero `h`, the sign of this change is
decided entirely by `f''(a)`:

* **`f''(a) > 0`** — every nearby `h` makes `f` larger, so `a` sits
  at the bottom of a bowl: a **local minimum**.

  ```
        •
      /   \
  ```

* **`f''(a) < 0`** — every nearby `h` makes `f` smaller, so `a`
  sits at the top of a dome: a **local maximum**.

  ```
     \     /
       •
  ```

* **`f''(a) = 0`** — the Taylor expansion's leading term vanishes
  too, so it gives no information; higher-order terms decide the
  outcome. For example, `f(x) = x^4` has `f''(0) = 0`, yet `x = 0`
  is still a minimum — the test is **indeterminate** here, not
  wrong.

```mermaid
flowchart TD
    A[Compute f'a] --> B{f'a = 0?}
    B -- No --> C[Not a critical point]
    B -- Yes --> D[Compute f''a]
    D --> E{Sign of f''a?}
    E -- Positive --> F[Local minimum]
    E -- Negative --> G[Local maximum]
    E -- Zero --> H[Indeterminate: check higher-order terms]
```

#### Saddle Points

The indeterminate case above, `f''(a) = 0`, is where a "saddle"
would live in one dimension — except in 1D there's only one
direction to walk, so a point can't curve up on one side and down
on the other the way a true saddle does. What happens instead is an
**inflection point**: the curve flattens, then keeps going the same
way it was already headed.

Take `f(x) = x^3` at `x = 0`. Both `f'(x) = 3x^2` and
`f''(x) = 6x` vanish at `x = 0`, so the second-derivative test is
indeterminate there. But `x = 0` is neither a local minimum nor a
local maximum: for `x < 0`, `f(x) < 0`, and for `x > 0`,
`f(x) > 0` — the curve just flattens momentarily on its way from
falling to rising. That's the 1D shadow of a saddle: the
second-derivative test hits `f''(a) = 0` and needs a higher-order
check, but there's no genuine "up one way, down the other" mixture
to classify, since a single dimension only offers one direction to
move in.

### Multivariable

For a function `f: R^n -> R`, the single derivative `f'` is
replaced by the **gradient**, the vector of every partial
derivative:

$$
\vec{\nabla} f(\mathbf{a}) = \left[ \frac{\partial f}{\partial x_1},
\frac{\partial f}{\partial x_2}, \ldots,
\frac{\partial f}{\partial x_n} \right]
$$

(This is exactly the $\vec{\nabla} f$ from [Partial Derivatives and
Multivariate Calculus](
  partial_derivatives_multivariate_calculus.md
).) A critical point is a point $\mathbf{a}$ where the gradient is
the zero vector:

$$
\vec{\nabla} f(\mathbf{a}) = \mathbf{0}
$$

Taylor's expansion generalizes the same way. For a small
displacement vector $\mathbf{v}$,

$$
f(\mathbf{a}+\mathbf{v}) - f(\mathbf{a}) = \vec{\nabla} f(\mathbf{a})
\cdot \mathbf{v} + \frac{1}{2} \mathbf{v}^T \mathbf{H}(\mathbf{a})
\mathbf{v} + \ldots
$$

where $\mathbf{H}(\mathbf{a})$ is the **Hessian** — the matrix of
every second partial derivative:

$$
\mathbf{H}(\mathbf{a}) = \left[ \frac{\partial^2 f}{\partial x_i
\partial x_j} \right]
$$

**Where the Hessian comes from.** Pick any unit direction
$\mathbf{u}$ and walk along the line
$r(t) = \mathbf{a} + t\mathbf{u}$. Define `g(t) = f(r(t))` — an
ordinary single-variable function tracking `f` along that one line.
Differentiating with the chain rule:

$$
g'(0) = \vec{\nabla} f(\mathbf{a}) \cdot \mathbf{u} \quad
\text{(the directional derivative)}
$$

$$
g''(0) = \mathbf{u}^T \mathbf{H}(\mathbf{a}) \mathbf{u} \quad
\text{(the second directional derivative)}
$$

So $\mathbf{u}^T \mathbf{H} \mathbf{u}$ measures **curvature**: how
the slope along direction $\mathbf{u}$ itself changes. This is the
direct multivariable analog of `f''(a)` — except now there's a
different curvature value for every direction $\mathbf{u}$, and the
Hessian is the single matrix that produces all of them.

The line $r(t) = \mathbf{a} + t\mathbf{u}$ is exactly the
parameterized path from [Parameterization](parameterization.md);
substituting `g(t) = f(r(t))`'s own single-variable Taylor
expansion (`g(t) - g(0) = g'(0)t + \frac{1}{2}g''(0)t^2 + \cdots`,
from the Single Variable section above) with the two derivatives
just found gives the multivariable Taylor expansion **along
direction $\mathbf{u}$**:

$$
f(\mathbf{a}+t\mathbf{u}) - f(\mathbf{a}) = t\,\vec{\nabla}
f(\mathbf{a}) \cdot \mathbf{u} + \frac{1}{2}t^2\,\mathbf{u}^T
\mathbf{H}(\mathbf{a})\mathbf{u} + \cdots
$$

At a critical point, $\vec{\nabla} f(\mathbf{a}) = \mathbf{0}$, so
the linear term vanishes and

$$
f(\mathbf{a}+t\mathbf{u}) - f(\mathbf{a}) \approx \frac{1}{2}t^2\,
\mathbf{u}^T \mathbf{H}(\mathbf{a})\mathbf{u}
$$

— the same $\frac{1}{2}\mathbf{v}^T\mathbf{H}(\mathbf{a})\mathbf{v}$
term introduced above, now derived one parameterized direction at a
time rather than all at once, and $\Delta f$ near a critical point
is dominated entirely by the Hessian's curvature.

**Physical analogy.**

| Physics      | Calculus        |
| ------------ | ---------------- |
| Position     | Function value   |
| Velocity     | Gradient         |
| Acceleration | Hessian          |

At a critical point, velocity (the gradient) is zero, so — exactly
as in `s = s0 + v0*t + (1/2) a t^2` — acceleration (the Hessian)
alone determines what happens next.

**Positive/negative definite matrices.** A symmetric matrix
$\mathbf{H}$ is:

* **Positive definite** if $\mathbf{x}^T \mathbf{H} \mathbf{x} > 0$
  for every nonzero vector $\mathbf{x}$ — every direction curves
  upward, like a bowl:

  ```
        •
      /   \
  ```

* **Negative definite** if $\mathbf{x}^T \mathbf{H} \mathbf{x} < 0$
  for every nonzero $\mathbf{x}$ — every direction curves downward,
  like a dome:

  ```
     \     /
       •
  ```

* **Indefinite** if $\mathbf{x}^T \mathbf{H} \mathbf{x}$ is positive
  for some $\mathbf{x}$ and negative for others — some directions
  curve up, some curve down:

  ```
       /
  ----•----
       \
  ```

  a **saddle**.

* **Semidefinite** if $\mathbf{x}^T \mathbf{H} \mathbf{x} = 0$ for
  some nonzero $\mathbf{x}$ — the test is inconclusive, just like
  `f''(a) = 0` in one variable.

**Why eigenvalues matter.** Hessians are real and symmetric, so the
Spectral Theorem guarantees real eigenvalues and orthogonal
eigenvectors. Writing any vector $\mathbf{x}$ in that eigenvector
basis, $\mathbf{x} = c_1 \mathbf{v}_1 + \ldots + c_n \mathbf{v}_n$,
the quadratic form simplifies to

$$
\mathbf{x}^T \mathbf{H} \mathbf{x} = \lambda_1 c_1^2 + \ldots +
\lambda_n c_n^2
$$

Since every `c_i^2 >= 0`, the sign of
$\mathbf{x}^T \mathbf{H} \mathbf{x}$ depends only on the
eigenvalues `λ_i`:

* all eigenvalues positive `<=>` positive definite `<=>` minimum
* all eigenvalues negative `<=>` negative definite `<=>` maximum
* mixed signs `<=>` indefinite `<=>` saddle point
* any eigenvalue zero `<=>` semidefinite `<=>` indeterminate

**Sylvester's Criterion.** Computing eigenvalues by hand is
tedious; Sylvester's Criterion classifies $\mathbf{H}$ from its
**leading principal minors** instead — the determinants
`D_1, D_2, ..., D_n` of the top-left `1x1`, `2x2`, ..., `nxn` blocks
of $\mathbf{H}$:

* **Positive definite:** every leading principal minor is
  positive — `D_1 > 0, D_2 > 0, ..., D_n > 0`.
* **Negative definite:** the signs alternate, starting negative —
  `D_1 < 0, D_2 > 0, D_3 < 0, ...`. (Each `D_k` equals, in the
  eigenvector basis, the product of the first `k` eigenvalues; if
  every eigenvalue is negative, one negative factor gives a
  negative product, two give a positive product, three give a
  negative product, and so on — hence the alternation.)

**The multivariable second-derivative test.** At a critical point,
$\vec{\nabla} f(\mathbf{a}) = \mathbf{0}$, so
$f(\mathbf{a}+\mathbf{v}) - f(\mathbf{a}) \approx \frac{1}{2}
\mathbf{v}^T \mathbf{H}(\mathbf{a}) \mathbf{v}$, and:

| Hessian           | Result        |
| ------------------ | -------------- |
| Positive definite  | Local minimum |
| Negative definite  | Local maximum |
| Indefinite         | Saddle point  |
| Semidefinite       | Inconclusive  |

```mermaid
flowchart TD
    A["Compute ∇f(a)"] --> B{"∇f(a) = zero vector?"}
    B -- No --> C[Not a critical point]
    B -- Yes --> D["Compute Hessian H(a)"]
    D --> E[Eigenvalues or Sylvester's Criterion]
    E -- All positive --> F[Local minimum]
    E -- All negative --> G[Local maximum]
    E -- Mixed signs --> H[Saddle point]
    E -- Some zero --> I[Indeterminate]
```

#### Saddle Points

An **indefinite** Hessian — some directions curve up, some curve
down — is exactly what defines a saddle point: unlike the 1D case,
there really are multiple independent directions to move in, and
they can disagree.

Take `f(x, y) = x^2 - y^2` at the origin. Its Hessian is constant
everywhere:

$$
\mathbf{H} = \begin{bmatrix} 2 & 0 \\ 0 & -2 \end{bmatrix}
$$

already diagonal, so its eigenvalues are its diagonal entries:
`λ_1 = 2`, `λ_2 = -2` — one positive, one negative, a mixed sign.
Walking along the `x`-axis (`y = 0`), `f(x, 0) = x^2` curves
upward, a bowl; walking along the `y`-axis (`x = 0`),
`f(0, y) = -y^2` curves downward, a dome. The origin is a minimum
along one axis and a maximum along the other simultaneously — the
defining shape of a **saddle point**, matching the Indefinite case
and the eigenvalue rule above (mixed signs `<=>` indefinite `<=>`
saddle point).

### Single Variable as n=1

Everything above reduces exactly to the single-variable case when
`n = 1`. The gradient becomes the ordinary derivative,
$\vec{\nabla} f = f'$, and the Hessian becomes the ordinary second
derivative, $\mathbf{H} = f''$. The quadratic form collapses to a
single term:

$$
\mathbf{v}^T \mathbf{H} \mathbf{v} = v \cdot f'' \cdot v = f'' v^2
$$

so the multivariable Taylor expansion,

$$
f(\mathbf{a}+\mathbf{v}) - f(\mathbf{a}) = \vec{\nabla}
f(\mathbf{a}) \cdot \mathbf{v} + \frac{1}{2} \mathbf{v}^T
\mathbf{H}(\mathbf{a}) \mathbf{v}
$$

becomes exactly the single-variable one,

```
f(a+h) - f(a) = f'(a)h + (1/2) f''(a) h^2
```

and positive/negative definiteness
($\mathbf{v}^T \mathbf{H} \mathbf{v} > 0$ or `< 0`) collapses to
`f'' > 0` or `f'' < 0`. The familiar first-/second-derivative test
from the Single Variable section above isn't a separate idea — it's
the Hessian test in its simplest, one-dimensional form.

### Cheat Sheet

| Concept           | Single Variable      | Multivariable               |
| ------------------ | ---------------------- | ----------------------------- |
| First derivative   | `f'(x)`               | $\vec{\nabla} f$              |
| Critical point     | `f'(x) = 0`            | $\vec{\nabla} f = \mathbf{0}$ |
| Second derivative  | `f''(x)`               | Hessian $\mathbf{H}$          |
| Curvature          | `f''`                  | $\mathbf{v}^T \mathbf{H} \mathbf{v}$ |
| Local minimum      | `f'' > 0`              | $\mathbf{H}$ positive definite |
| Local maximum      | `f'' < 0`              | $\mathbf{H}$ negative definite |
| Saddle             | not applicable in 1D   | $\mathbf{H}$ indefinite       |
| Indeterminate      | `f'' = 0`               | $\mathbf{H}$ semidefinite or singular |

The unifying idea: optimization is fundamentally about local
curvature. In one dimension there's only one direction to move, so
a single number, `f''`, captures it. In many dimensions there are
infinitely many directions, so the Hessian acts as a "curvature
machine" — for any direction $\mathbf{u}$,
$\mathbf{u}^T \mathbf{H} \mathbf{u}$ returns the curvature along
that direction. Its eigenvectors are the principal directions of
curvature, and its eigenvalues measure how strongly the function
curves along each one.

## Reference

Watch these lectures from MIT's 18.02 *Multivariable Calculus*
(Fall 2007) [video gallery](
  https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/video_galleries/video-lectures/
), the same series [Partial Derivatives and Multivariate
Calculus](partial_derivatives_multivariate_calculus.md) draws on —
these two are most directly about classifying critical points:

* **Lecture 9** — Max-Min and Least Squares
* **Lecture 10** — Second Derivative Test

## Exercise

Work through all three exercises in [Critical Points](
  ../projects/critical_points/
) in a Jupyter or Colab notebook: first **Finding the Bowl's
Bottom** — finding and classifying every critical point of a
single-variable cubic by hand and numerically — then **Saddle or
Bowl?** — classifying multivariable critical points with the
Hessian, cross-checking eigenvalues against Sylvester's Criterion —
then **Which Way Does It Curve?**, sweeping directional curvature
`uᵀHu` over a full circle of directions and confirming the extremal
directions line up with the Hessian's eigenvectors.
