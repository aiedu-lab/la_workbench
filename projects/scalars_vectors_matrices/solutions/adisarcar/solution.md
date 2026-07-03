# Solution: Pirate Treasure Walk

## Contributors
adisarcar
sidk256

## Test Cases
`ptreasurewalk.py` sums four walk vectors into `a5` and prints it,
then prints the boolean
`norm(a5) >= norm(a1) + norm(a2) + norm(a3) + norm(a4)` to compare the
direct-path length against the sum of the individual legs. Each leg
and the running total are also drawn with `plt.quiver` so the walk
can be traced visually.

## Software Installs
None beyond the repo's `.venv` (numpy, matplotlib — see
`requirements.in`).

## Solution Manual
1. `pip install -r requirements.in` (or reuse the repo root `.venv`).
2. `python3 ptreasurewalk.py`.
3. Check the printed sum vector and boolean, and confirm the quiver
   plot traces a connected path from leg to leg.
