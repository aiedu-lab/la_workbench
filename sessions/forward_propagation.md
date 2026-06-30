# Forward Propagation (Inference)

## Concept

Forward propagation is everything this course has built, run in
sequence. Information flows through a stack of linear
transformations and nonlinearities to produce a prediction: each
layer multiplies its input by a weight matrix (a linear
transformation, exactly like resizing the rocket or rotating the
flower), adds a bias vector, then applies a nonlinear function
before passing the result to the next layer.

A manufacturing pipeline is the everyday version: raw material
enters one station, gets reshaped, and moves to the next, each
step gradually transforming it into a finished product. A neural
network's forward pass is the same — an input vector enters,
gets transformed by each layer in turn, and exits as an output
(a prediction, a classification, the next token).

The "linear transformation, then transformation, then
transformation" structure is exactly matrix composition from the
Matrix Multiplication session — a deep network really is one long
chain of matrix multiplications, with a nonlinearity inserted
between each link so the whole chain can't collapse into a single
matrix. Neural network inference, transformers, and large language
models all run this same forward pass; the difference between them
is which layers, and how the weight matrices were learned — the
subject of the next session.

## Exercise

<!-- TODO: exercise -->
