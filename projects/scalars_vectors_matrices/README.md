# Scalars, Vectors and Matrices — Exercise

## Pirate Treasure Walk

**Skills:** vector addition, scalar multiplication, magnitude,
plotting with `quiver`.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `np.linalg.norm` for magnitude. After plotting, call
`plt.gca().set_aspect('equal')` so shapes aren't squished.

A pirate starts at the origin and makes four moves, each a vector
measured in paces: `[3, 0]`, `[0, 4]`, `[-2, 2]`, and `[5, -1]`.

* Store each move as a NumPy array and use vector addition to find
  the treasure's final coordinates.
* Find the straight-line distance from start to treasure with
  `np.linalg.norm`. Is it shorter than the total distance actually
  walked?
* The pirate repeats the same path but takes steps twice as long.
  Use scalar multiplication to get the new moves and the new
  endpoint.
* Plot the journey as connected arrows using `plt.quiver(...)` with
  `angles='xy'`, `scale_units='xy'`, `scale=1`. Mark the start and
  the treasure with dots.

**Stretch goal:** What single vector takes the pirate straight from
start to treasure in one move? How does it relate to the four
moves?
