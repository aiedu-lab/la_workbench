# Kaggle Titanic Capstone — Exercise

Every other project in this course is a small toy exercise meant
to isolate one idea. This one is not a toy: it is the
[Kaggle Titanic competition](https://www.kaggle.com/competitions/titanic),
a real, public dataset, worked end to end — load real data, build
a feature matrix, train a complete model, and produce predictions
you could actually submit.

Work through this in a Jupyter or Colab notebook.

Setup cell:

```python
import numpy as np
import pandas as pd
import torch
```

## Steps

* Create a free Kaggle account and download the Titanic dataset
  (`train.csv`, `test.csv`) from the competition page above.
* Load `train.csv` and turn each passenger row into a feature
  vector: passenger class, sex, age, fare, and family size are a
  reasonable starting set. This is the feature matrix from
  Scalars, Vectors and Matrices, built from real, messy data —
  expect missing values to handle before anything else works.
* Decide how to represent each feature as a number (sex isn't
  already numeric; age has gaps to fill). This is a basis choice
  for your data, the same idea as Basis and Change of Basis,
  applied to a real dataset instead of a toy coordinate change.
* Build a small model — logistic regression or a one- or
  two-layer network in PyTorch is enough — that maps a passenger's
  feature vector to a survival prediction. This is the same
  matrix-times-vector-plus-nonlinearity structure from Forward
  Propagation, just with real, learned weights instead of weights
  you chose by hand.
* Train it: repeatedly run forward propagation on the training
  passengers, measure the error against their known survival, and
  use backpropagation and gradient descent to adjust the weights.
  This is Gradients and Backpropagation, run for real, over many
  passes through the data.
* Evaluate accuracy on a held-out slice of the training data, then
  run the trained model on `test.csv` to produce predictions in
  the format the competition expects.

## Reflection

* Which features mattered most to your model's predictions? Does
  that match your intuition about who survived?
* What did you have to decide that none of the earlier toy
  exercises required (missing data, feature encoding, train/test
  split)? Those decisions are most of what makes a real model
  different from a toy one.

**Stretch goal:** Submit your predictions to the competition and
see your leaderboard score. Then try one change — a different
feature set, a deeper network, more training passes — and see
whether it actually improves the score.
