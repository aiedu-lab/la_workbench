# Embeddings: Representing Meaning as Vectors — Exercise

## Words as Vectors

**Skills:** toy embeddings, cosine similarity, nearest neighbor,
vector arithmetic.

Work through this in a Jupyter or Colab notebook. Run a cell,
predict the result first, then check it — don't just get the
answer, make a picture of it.

Setup cell:

```python
import numpy as np
import matplotlib.pyplot as plt
```

Handy: reuse the `cosine_sim` you wrote in the Distance, Length
and Similarity exercise. After plotting, call
`plt.gca().set_aspect('equal')`.

A tiny, hand-built embedding table places 8 words in 2D:

```python
embeddings = {
    'king':  np.array([4.0, 4.0]),
    'queen': np.array([3.8, 4.2]),
    'man':   np.array([4.0, 1.0]),
    'woman': np.array([3.7, 1.3]),
    'pizza': np.array([-3.0, 2.0]),
    'pasta': np.array([-3.2, 2.3]),
    'dog':   np.array([0.0, -3.0]),
    'cat':   np.array([0.3, -3.2]),
}
```

* Predict, just by eye, which word is closest in *meaning* to
  `'king'` among the other seven.
* Write `nearest_neighbor(query, embeddings, exclude)` that
  computes cosine similarity between `query` and every entry
  except `exclude`, and returns the highest-scoring word. Confirm
  it matches your prediction for `'king'`.
* Plot all 8 word vectors from the origin with labels. Do the
  "royalty" words, "food" words, and "animal" words each cluster
  in their own direction?

**Stretch goal:** Compute `king - man + woman` and find its
nearest neighbor among the remaining words with
`nearest_neighbor`. Does the classic "king - man + woman ≈ queen"
analogy hold in this toy embedding space?

## Help

Copy this once and reuse it to draw the word vectors — no need to
write scatter/annotate boilerplate from scratch:

```python
def plot_word_vectors(embeddings):
    """Scatter each word vector and label it by name."""
    for word, v in embeddings.items():
        plt.scatter(*v, color='C0')
        plt.annotate(word, v)
    plt.gca().set_aspect('equal')
```

Don't just eyeball the closest word — let the assert confirm it:

```python
def cosine_sim(a, b):
    return (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))

def nearest_neighbor(query, embeddings, exclude=None):
    candidates = {w: v for w, v in embeddings.items() if w != exclude}
    return max(candidates, key=lambda w: cosine_sim(query, candidates[w]))

assert nearest_neighbor(embeddings['king'], embeddings, 'king') == 'queen'
```
