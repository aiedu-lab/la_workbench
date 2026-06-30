# What is a Model?

## Concept

A model is simply a function that maps inputs to outputs. That is
the entire idea behind machine learning — strip away the buzzwords
and every model, from a linear regression to a large language
model, is doing the same thing: taking some input and producing
an output, according to rules it has learned rather than rules a
programmer wrote by hand.

Real-world examples make the pattern concrete:

* House features (square footage, location, bedrooms) → price.
* Email text → spam or not spam.
* An image → an object label.
* A sentence so far → the next word.

In every case, a traditional program would need an explicit rule
for every situation. A model instead learns the mapping from
examples — and that mapping is exactly what the rest of this
course gives you the tools to describe precisely: as vectors,
matrices, and the transformations between them.

Neural networks are mathematical models that learn these mappings
from data. Once you can see a model as "a function from inputs to
outputs, with adjustable parameters," every later session — from
vectors to forward propagation to backpropagation — is really just
asking: *what shape should that function take, and how do its
parameters get tuned?*

## Exercise

<!-- TODO: exercise -->
