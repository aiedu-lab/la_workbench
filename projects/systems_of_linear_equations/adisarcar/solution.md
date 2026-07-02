# Solution: The Snack Bar Mystery

## Contributors
adisarcar
sidk256

## Test Cases
`thesnackbarmystery.py` solves the 2x2 system with
`np.linalg.solve(A, B)` and prints the `(x, y)` answer, then plots
both snack-bar equations as lines. The printed solution is checked by
eye against the plotted intersection point (marked with a blue
circle) — they land on the same spot.

## Software Installs
None beyond the repo's `.venv` (numpy, matplotlib — see
`requirements.in`).

## Solution Manual
1. `pip install -r requirements.in` (or reuse the repo root `.venv`).
2. `python3 thesnackbarmystery.py`.
3. Confirm the printed `(x, y)` solution matches where the two
   plotted lines cross.
