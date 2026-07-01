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

## Help

Copy this once and reuse it for every arrow you need to draw — no
need to write `quiver` boilerplate from scratch:

```python
def plot_vectors(vecs, origin=(0, 0), colors=None, labels=None):
    """Draw each vector in `vecs` as an arrow from `origin`."""
    ox, oy = origin
    colors = colors or ['C0'] * len(vecs)
    for i, v in enumerate(vecs):
        plt.quiver(
            ox, oy, v[0], v[1], color=colors[i],
            angles='xy', scale_units='xy', scale=1,
        )
        if labels:
            plt.annotate(labels[i], (ox + v[0], oy + v[1]))
    plt.gca().set_aspect('equal')
```

Don't just eyeball the answer — compute the final position two
independent ways and assert they agree:

```python
moves = np.array([[3, 0], [0, 4], [-2, 2], [5, -1]])

final_position = np.array([0, 0])
for m in moves:
    final_position = final_position + m

assert np.allclose(final_position, moves.sum(axis=0))
```
