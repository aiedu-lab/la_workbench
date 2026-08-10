---
description: LaTeX vector/matrix notation that renders correctly
  on GitHub's file viewer
---

# LaTeX Math Notation (GitHub-Safe)

**Why this exists**: GitHub's file-viewer math rendering uses real
MathJax, but two things break silently there that work fine in a
full local MathJax previewer (browser extension, VS Code preview):
`\mathbf{...}` degrades to plain (unbold) instead of erroring, and
`\\` (the matrix/array row separator) only renders correctly when it
is the very last token on its physical source line — anything
trailing it on the same line (an optional `[Npt]` spacing arg, more
cells, `\qquad`, etc.) breaks the block. Discovered debugging
`sessions/partial_derivatives_multivariate_calculus.md`.

## The Rules

1. **Vectors** (e.g. `x`, `b`, `X`, `a`, `v`, `u`, `0`, `1`, `F`):
   wrap as `\mathbf{\vec{symbol}}` — bold outer, arrow inner. A full
   MathJax renderer shows bold+arrow; GitHub shows at minimum the
   arrow even though the outer `\mathbf` degrades to unbold.
2. **Matrices** (e.g. `A`, `B`, `H`, `J`): use `\mathbfit{symbol}`
   instead of `\mathbf{symbol}`.
3. **Always render vectors as column vectors**, never row vectors.
   Use `\begin{bmatrix} ... \\ ... \end{bmatrix}`, not a
   `\left[ a, b \right]` comma-separated row-list, for any
   standalone `$$...$$` vector definition. (Inline prose shorthand
   like `(2x, 2y)` or `[F_x\hat{i}, F_y\hat{j}]` used mid-sentence as
   a tuple, not presented as a formal vector object, is exempt —
   converting those to a stacked column would be typographically
   absurd inline in a sentence.)
4. **In any `bmatrix`/`pmatrix`/`vmatrix`/`array`/`cases` block, put
   each row on its own physical source line, ending exactly at
   `\\`** — nothing else may follow `\\` before the newline. Do not
   use the optional `\\[Npt]` spacing argument; it is not
   last-token-on-line and breaks on GitHub.

## Examples

✅ **Good**:

```latex
$$
\vec{\nabla} f = \begin{bmatrix}
\dfrac{\partial f}{\partial x} \\
\dfrac{\partial f}{\partial y}
\end{bmatrix}
$$

$$
\mathbfit{J} = \begin{bmatrix}
1 & 1 \\
v & u
\end{bmatrix}, \qquad \det \mathbfit{J} = u - v
$$

$d\mathbf{\vec{x}}$ is the step vector; $\mathbfit{A}$ is a matrix.
```

❌ **Bad**:

```latex
$$
\mathbf{J} = \begin{bmatrix} 1 & 1 \\ v & u \end{bmatrix}
$$
\\ mid-line (more cells follow it on the same source line) — breaks
on GitHub even though it's valid LaTeX and renders fine locally.

$$
\mathbf{J} = \begin{bmatrix}
a & b \\[6pt]
c & d
\end{bmatrix}
$$
\\[6pt] optional spacing arg — breaks on GitHub.

$$
\vec{\nabla} f = \left[ \frac{\partial f}{\partial x},
\frac{\partial f}{\partial y} \right]
$$
row vector via comma-list — use a column bmatrix instead.

$\mathbf{J}$ for a matrix — use \mathbfit{J} instead.
```

## Enforcement

Run on any `.md` file with math before committing:

```bash
# Bare \mathbf{X} that should be \mathbf{\vec{X}} (vector) or
# \mathbfit{X} (matrix) — should return nothing.
grep -n 'mathbf{[A-Za-z0-9_]*}' sessions/*.md projects/*/README.md \
  | grep -v 'mathbf{\\vec'

# \\ not at the end of its physical line inside a matrix/array
# block — inspect any hits by hand; the \\ must be the last
# non-whitespace token before the newline.
grep -n '\\\\\\\\[^ ]' sessions/*.md projects/*/README.md
```

`miscellaneous/software_defined_workbench/plan.md` and
`prompt_history.md` are historical ledgers, not rendered lesson
content — exempt from this rule per CLAUDE.md's rule 7 (never edit
`plan.md` content, only step statuses).
