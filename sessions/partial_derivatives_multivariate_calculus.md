# Partial Derivatives and Multivariate Calculus

## Concept

Extend single-variable calculus to a function of two inputs,
`z = f(x, y)` — think of `z` as the elevation of a hill, with `x`
and `y` the east-west and north-south position:

```
          z
          ^
         /\
        /  \
       /    \
------/------\------> x
     /
    /
   y
```

A **partial derivative** freezes one input and asks how steep the
hill is if you only walk in the other direction. Freeze `y` and
walk only east-west:

```
y held constant

          ^
         /|
        / |
-------/--|-------->
      x
```

The slope you measure along that single slice is `∂f/∂x`.
Freezing `x` instead and walking only north-south gives `∂f/∂y`
the same way. A partial derivative always answers: "if I move in
only *this* one direction, how steep is the hill?"

Real walking rarely stays aligned with one axis, though — usually
both `x` and `y` change together. The **total differential** adds
up both contributions:

```
dz = (∂f/∂x) dx + (∂f/∂y) dy
```

This says the total change in elevation, from a small diagonal
step, is the sum of "how much `x` changed, scaled by how steep `x`
is" and "how much `y` changed, scaled by how steep `y` is" — both
partials contribute simultaneously, not one at a time.

Collect the two partials into a single vector, and something
elegant happens:

```
grad f = [ df/dx, df/dy ]     (the gradient, written ∇f)
dx_vec = [ dx, dy ]           (your step direction)

dz = ∇f . dx_vec              (a dot product)
```


The **gradient** `∇f` is a vector that points in the direction of
steepest uphill; its length tells you how steep that steepest
direction is. The total differential — how much elevation changes
for *any* step — is simply the dot product of the gradient with
that step. This is exactly the dot-product idea from [Distance,
Length and Similarity](distance_length_similarity.md), now put to
work measuring how a function changes: partial derivatives collect
into a vector, and linear algebra (the dot product) is what
combines them into one number.

Critical points generalize the same way as in the single-variable
case: a point where the gradient is the zero vector — both
partials zero at once — is a candidate minimum, maximum, or
saddle, the two-variable version of "the hill flattens out."

This groundwork is exactly what later sessions build on: the
gradient reappears, unmodified, as the direction gradient descent
walks downhill during model training (see [Learning from Mistakes:
Gradients and Backpropagation](gradients_backpropagation.md)), and
the total differential is the first-order piece of a Taylor
expansion approximating a function near a point.

### Minimizing Least Squares

Suppose you have `N` data points `(x_i, y_i)` and want the
straight line `y = a*x + b` that fits them best. "Best" means
choosing the slope `a` and intercept `b` that minimize the average
squared gap between the line and the data:

```
f(a, b) = (1/N) * sum_i ( y_i - (a*x_i + b) )^2
```

This is exactly the two-variable minimization this session just
introduced — the two "directions" aren't `x` and `y`, they're the
two unknowns `a` and `b`. The gradient of `f` with respect to
`(a, b)` must be the zero vector at the minimum:

```
∂f/∂a = 0
∂f/∂b = 0
```

Working through those two equations (see the paper problem in
[Finding the Best-Fit Line](
  ../projects/partial_derivatives_multivariate_calculus/
)) gives a closed-form solution:

```
b = Ave(y) - a * Ave(x)
a = Cov(x, y) / Var(x)
```

where `Ave` is the average, `Var(x)` is the variance of `x`, and
`Cov(x, y)` is the covariance between `x` and `y`.

Linear algebra reveals what these statistics really are. Collect
the points into vectors `X = [x_1, ..., x_N]` and
`Y = [y_1, ..., y_N]`, and *center* each one by subtracting its
own average:

```
Cen(X) = X - Ave(X) * vec(1)
Cen(Y) = Y - Ave(Y) * vec(1)
```

Variance and covariance are then just dot products of these
centered vectors:

```
Var(X)    = (1/N) * Cen(X) . Cen(X)
Cov(X, Y) = (1/N) * Cen(Y) . Cen(X)
```

so the slope `a` is a ratio of dot products —
`a = Cov(Cen(X), Cen(Y)) / Var(Cen(X))` — and `a * Cen(X)` is
exactly the **projection** of `Cen(Y)` onto `Cen(X)`, the same
projection idea from [Orthogonality and Projections](
  orthogonality_projections.md
). The correlation between `x` and `y` is simply the cosine of
the angle between `Cen(X)` and `Cen(Y)`:

```
rho = ( Cen(Y) / |Cen(Y)| ) . ( Cen(X) / |Cen(X)| )
```

In plain language: the slope `a` measures how much `x` and `y`
tend to move together, relative to how much `x` alone moves — a
ratio of "moving together" to "moving." The intercept `b` is just
the average "lift" needed on top of `a*x_i` to land on `y_i`.

**Generalizing the problem.** Fitting a straight line isn't the
only place this machinery applies. An exponential fit
`Z = d * exp(a*X)` becomes a straight-line fit after taking a log:
`Y = ln(Z) = a*X + ln(d)`, so `b = ln(d)`. A quadratic fit
`Y = a*X^2 + b*X + c` is *still* linear in its three unknowns
`(a, b, c)` — the same `∂f/∂a = ∂f/∂b = ∂f/∂c = 0` approach
applies, just with one more partial derivative to set to zero.

The unifying insight: statistics starts with averages, variances,
and covariances, but linear algebra reveals these are simply
lengths and dot products. Least-squares regression, underneath, is
projecting the output vector onto the subspace spanned by the
input vectors.

## Reference

Watch these lectures from MIT's 18.02 *Multivariable Calculus*
(Fall 2007) [video gallery](
  https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/video_galleries/video-lectures/
) — they cover, in order, exactly the ideas above:

* **Lecture 8** — Partial derivatives; tangent plane approximation
* **Lecture 9** — Max-min problems
* **Lecture 10** — Second derivative test; boundaries and infinity
* **Lecture 11** — Differentials; chain rule
* **Lecture 12** — Gradient; directional derivative; tangent plane

## Exercise

Work through both exercises in [Partial Derivatives and
Multivariate Calculus](
  ../projects/partial_derivatives_multivariate_calculus/
) in a Jupyter or Colab notebook: first **The Hill and Its
Slices** — visualizing a two-variable function and its
frozen-variable slices, confirming the chain rule against direct
substitution, and finding a minimum where the gradient is the zero
vector — then **Finding the Best-Fit Line**, applying the same
minimization idea to derive the least-squares slope and intercept
from the Concept section above.
