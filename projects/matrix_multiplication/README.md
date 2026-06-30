# Matrix Multiplication — Exercise

## Build a Flower with Rotations

**Skills:** rotation matrices, the angle-matrix connection, loops,
composition.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `A @ B` multiplies matrices. After plotting, call
`plt.gca().set_aspect('equal')` so shapes aren't squished.

Start with one small, lopsided "petal" shape near the origin.

* Write a function `rot(deg)` that returns the 2×2 rotation matrix
  for a given angle in degrees.
* Test it first: rotate the point `(1, 0)` by 90° and confirm you
  get `(0, 1)`.
* Use a loop to rotate the petal by 0°, 45°, 90°, ... up to 360°,
  plotting each copy. You should get a symmetric flower.
* Experiment with the angle step. What step angle gives exactly 8
  petals? Exactly 12?

**Stretch goal:** Rotating by 30° twice should equal rotating by
60° once. Verify this with matrix multiplication: is
`rot(30) @ rot(30)` the same as `rot(60)`?
