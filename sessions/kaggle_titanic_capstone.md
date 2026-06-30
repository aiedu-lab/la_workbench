# Kaggle Titanic Capstone

## Concept

Every earlier session ended in a small toy exercise: a pirate's
paces, a rocket's resize, a flower of rotations, a snack bar's
prices. Each one isolated a single idea — vector addition, a
dilation matrix, composition, a singular system — and let you see
it in a few lines of NumPy. This session is different: it is one
real, messy, end-to-end project that asks you to use everything
those toy exercises taught, together, on real data.

The [Titanic competition](https://www.kaggle.com/competitions/titanic)
asks a simple question — given a passenger's data (class, age, sex,
fare, family aboard), did they survive? — but answering it touches
the whole course's arc: passenger records become a feature matrix
(Scalars, Vectors and Matrices); features get compared and
weighted (Distance, Length and Similarity); a model is a
transformation from the feature matrix to a prediction vector
(Linear Transformations, Matrix Multiplication); fitting that
model means solving for parameters that best satisfy many
constraints at once (Systems of Linear Equations, Orthogonality
and Projections); and the parameters are learned by repeatedly
running forward propagation and correcting with the gradient
(Forward Propagation, Gradients and Backpropagation).

A toy exercise can be solved by directly computing the right
answer. This capstone cannot — there is no formula for "did they
survive," only data and a training pipeline. That is the
difference: every session before this taught you a tool; this one
asks you to build a complete model with those tools, the way every
model discussed in this course, including the largest, was built.

## Exercise

Work through the [Kaggle Titanic
Capstone](../projects/kaggle_titanic_capstone/): load the
passenger data, build a feature matrix, train a model end to end,
and submit predictions.
