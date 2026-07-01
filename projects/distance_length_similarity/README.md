# Distance, Length and Similarity — Exercise

## Song Similarity Mini

**Skills:** dot product, vector norm, cosine similarity, nearest
neighbor.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: `np.linalg.norm` for length, `a @ b` for the dot product.
After plotting, call `plt.gca().set_aspect('equal')` so angles
aren't distorted.

Four songs are represented as `(tempo, energy)` vectors, each
scored 0–10:

* Chill Wave: `[2, 3]`
* Power Anthem: `[9, 8]`
* Late Night Lo-fi: `[3, 2]`
* Arena Rock: `[8, 9]`

A new song, Study Beats, scores `[2.5, 2.5]`.

* Store the four songs and the query as NumPy vectors.
* Write `cosine_sim(a, b)` using the dot product and
  `np.linalg.norm` — do not use a library shortcut.
* Before computing, predict by eye which song is most "aligned"
  in direction with Study Beats. Then compute cosine similarity
  against all four and confirm with `np.argmax`.
* Plot all five vectors from the origin. Which two point in
  nearly the same direction, even though their lengths differ?

**Stretch goal:** Scale Power Anthem by 0.4 (a quieter mix of the
same song) and recompute its cosine similarity to Arena Rock.
Cosine similarity should barely move even though Euclidean
distance changes a lot — why?

## Help

Copy this once and reuse it to draw every song vector — no need
to write `quiver` boilerplate from scratch:

```python
def plot_vectors(vecs, colors=None, labels=None):
    """Draw each vector in `vecs` as an arrow from the origin."""
    colors = colors or ['C0'] * len(vecs)
    for i, v in enumerate(vecs):
        plt.quiver(
            0, 0, v[0], v[1], color=colors[i],
            angles='xy', scale_units='xy', scale=1,
        )
        if labels:
            plt.annotate(labels[i], (v[0], v[1]))
    plt.gca().set_aspect('equal')
```

Don't just trust your `cosine_sim` implementation — check it
against the formula directly:

```python
a = np.array([9, 8])   # Power Anthem
b = np.array([2.5, 2.5])  # Study Beats
formula = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
assert np.isclose(cosine_sim(a, b), formula)
```
