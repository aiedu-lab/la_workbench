# Learning from Mistakes: Gradients and Backpropagation

## Concept

Forward propagation produces a prediction; learning is what
happens next. A model improves by measuring how wrong its
prediction was (the error, or loss) and adjusting its parameters
in the direction that reduces that error. The **gradient** is
exactly that direction: for each parameter, it says which way to
nudge it, and by how much, to make the error a little smaller.

Learning to throw darts works the same way: you don't recompute
your whole throwing technique from scratch after every miss — you
notice which way you missed and correct in that direction next
time. A model does this automatically, for every parameter at
once, using calculus's derivative to measure "which way is
downhill" on the error.

**Backpropagation** is how that correction reaches every layer of
a deep network efficiently. Since forward propagation is a chain
of matrix multiplications and nonlinearities (see Forward
Propagation), the chain rule from calculus lets the error computed
at the output be propagated backward, layer by layer, turning into
a gradient for every weight matrix along the way — without
recomputing the whole network from scratch for each parameter.

This is gradient descent: repeatedly run forward propagation, measure
the error, backpropagate the gradient, and nudge every parameter a
small step downhill. Repeat enough times, on enough examples, and
the parameters settle into values that make good predictions. This
is neural network training, and it is the mechanism behind every
model from a small classifier to a large language model.

## Exercise

Work through [Rolling Downhill](
  ../projects/gradients_backpropagation/
) in a Jupyter or Colab notebook: hand-rolled gradient descent on 
a toy quadratic loss, watching the loss drop step by step toward 
its minimum.
