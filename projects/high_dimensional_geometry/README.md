# High-Dimensional Geometry — Exercise

## Curse of Dimensionality Mini-Lab

**Skills:** high-dimensional vectors, `np.random`, distance
concentration.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `np.random.default_rng`, `np.linalg.norm(..., axis=1)` to
get one distance per row at once.

For each dimension `d` in `[2, 3, 10, 100]`, generate 500 random
points uniformly in `[0, 1]^d`, and compute the distance from the
first point to all the other 499.

* Predict: as `d` grows, do you expect distances to spread out
  more, or to bunch up closer together relative to their average?
* For each `d`, compute `relative_spread = distances.std() /
  distances.mean()`.
* Plot a histogram of the distances for each `d` side by side.
  Watch how the spread of the histogram changes shape as `d`
  grows.

**Stretch goal:** Nearest-neighbor search relies on some points
being clearly closer than others. Using your `d = 100` distances,
how much closer is the *nearest* point than the *farthest*, as a
percentage of the average distance? Compare that percentage to the
`d = 2` case.

## Help

Copy this once and reuse it to compare distance distributions
across dimensions — no need to write subplot boilerplate from
scratch:

```python
def plot_distance_histograms(dists_by_dim):
    """One histogram per {dimension: distances} entry."""
    fig, axes = plt.subplots(1, len(dists_by_dim), figsize=(12, 3))
    for ax, (d, dists) in zip(axes, dists_by_dim.items()):
        ax.hist(dists, bins=20)
        ax.set_title(f"d = {d}")
```

Don't just eyeball the histograms shrinking — let the assert
confirm relative spread drops:

```python
rng = np.random.default_rng(0)
pts_2d = rng.random((500, 2))
pts_100d = rng.random((500, 100))
dists_2d = np.linalg.norm(pts_2d - pts_2d[0], axis=1)[1:]
dists_100d = np.linalg.norm(pts_100d - pts_100d[0], axis=1)[1:]

relative_spread_2d = dists_2d.std() / dists_2d.mean()
relative_spread_100d = dists_100d.std() / dists_100d.mean()
assert relative_spread_100d < relative_spread_2d
```
