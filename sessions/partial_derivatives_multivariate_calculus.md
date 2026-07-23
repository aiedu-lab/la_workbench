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
case: a point where `∇f = [0, 0]` — both partials zero at once —
is a candidate minimum, maximum, or saddle, the two-variable
version of "the hill flattens out."

This groundwork is exactly what later sessions build on: the
gradient reappears, unmodified, as the direction gradient descent
walks downhill during model training (see [Learning from Mistakes:
Gradients and Backpropagation](gradients_backpropagation.md)), and
the total differential is the first-order piece of a Taylor
expansion approximating a function near a point.

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

Work through [The Hill and Its Slices](
  ../projects/partial_derivatives_multivariate_calculus/
) in a Jupyter or Colab notebook: visualizing a two-variable
function and its frozen-variable slices, confirming the chain rule
against direct substitution, and finding a minimum where the
gradient is the zero vector.
