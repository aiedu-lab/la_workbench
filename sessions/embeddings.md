# Embeddings: Representing Meaning as Vectors

## Concept

An **embedding** is a vector chosen so that similar objects end up
with nearby vector representations. "King" should land closer to
"Queen" than to "Pizza" — not because anyone hand-coded that rule,
but because the vector for each word was learned so that distance
and direction (the tools from the Distance, Length and Similarity
session) line up with meaning.

This is the payoff of every earlier session: vectors as points and
directions, dot products and cosine similarity, basis and change
of basis, high-dimensional geometry — embeddings are the place
those ideas stop being abstract and start being how real systems
represent text, images, and users. Word embeddings place words in
a space where "similar meaning" means "nearby vector." Image
embeddings do the same for pictures. A user embedding can place
people with similar tastes near each other, which is what powers
recommendations.

Retrieval-Augmented Generation (RAG) and semantic search both work
by embedding a query and a large collection of documents into the
same space, then finding the nearest (most similar) vectors — the
same nearest-neighbor idea from the Distance, Length and Similarity
session, applied to meaning instead of raw numbers. Nothing about
the search step requires understanding language; it requires only
the vector geometry already covered in this course.

## Exercise

<!-- TODO: exercise -->
