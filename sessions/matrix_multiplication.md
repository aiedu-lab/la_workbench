# Matrix Multiplication

## Concept

Multiple transformations can be composed into one. If matrix `A`
rotates space and matrix `B` scales it, then `A @ B` is a single
matrix that does both — scale, then rotate — in one
multiplication. That is what matrix multiplication *is*: not a
row-times-column arithmetic trick to memorize, but composition of
transformations, the same way calling two functions in sequence
composes into one combined function.

This composition view explains things that look strange if matrix
multiplication is just memorized arithmetic. Order matters —
`A @ B` is generally not `B @ A` — because "rotate then scale" and
"scale then rotate" really are different transformations. Repeated
multiplication by the same matrix composes a transformation with
itself: rotating by 30° twice is the same single transformation as
rotating by 60° once, and `rot(30) @ rot(30)` should equal
`rot(60)` exactly because of this.

A factory assembly line is the everyday version: each station
performs one operation, and the line as a whole is the composition
of every station. Forward propagation through a neural network or
transformer works the same way — each layer is a matrix
multiplication, and the network's full behavior is the composition
of every layer's transformation, applied one after another.

Watch 3Blue1Brown's *Essence of Linear Algebra*, Chapter 4 —
["Matrix multiplication as
composition"](https://www.3blue1brown.com/?topic=linear-algebra) —
before the exercise below.

## Exercise

Work through [Build a Flower with Rotations](
  ../projects/matrix_multiplication/
) in a Jupyter or Colab notebook: rotation matrices, the 
angle-matrix connection, and composing transformations through 
repeated multiplication.
