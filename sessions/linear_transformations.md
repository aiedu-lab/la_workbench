# Linear Transformations

## Concept

A matrix is best viewed as a transformation rather than a table of
numbers. Multiply a matrix by a vector and you don't just get new
numbers — you get a rule for moving every point in space: rotating
maps, resizing images, changing camera perspectives. The matrix
*is* the rule; multiplying by it is *applying* the rule.

Two transformations make the idea concrete. A **dilation** matrix
scales space — stretching it taller, shorter, wider, or narrower
along the axes. A **shear** matrix slides space sideways by an
amount that depends on position, turning upright shapes into
slanted ones while leaving one direction fixed. Both are linear
transformations: straight lines stay straight, the origin stays
fixed, and grid lines stay evenly spaced.

The **determinant** of a transformation's matrix tells you how it
scales area (in 2D) or volume (in 3D). A dilation that doubles
height and halves width leaves area unchanged — and its
determinant is 1. A shear, surprisingly, never changes area at
all, no matter how much it slants — also determinant 1. When the
determinant is 0, the transformation collapses space onto a lower
dimension, which is exactly what makes a system of equations
unsolvable, as the next session shows.

Every neural network layer transforms one vector into another the
same way: a weight matrix times an input vector reshapes the input
space before a nonlinearity is applied. Understanding transformations
geometrically here is what makes forward propagation, later in this
course, feel like a sequence of pictures rather than a sequence of
symbols.

Watch 3Blue1Brown's *Essence of Linear Algebra*, Chapter 3 —
["Linear transformations and
matrices"](https://www.3blue1brown.com/?topic=linear-algebra) —
before the exercises below.

## Exercise

Work through both exercises in [Linear Transformations](
  ../projects/linear_transformations/
): **Resize the Rocket** (dilation matrices, matrix-vector 
multiplication, the determinant as an area factor) and 
**Make It Lean** (
  shear matrices, which coordinates move, and area preservation
).
