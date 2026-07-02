# Solution: Build a Flower with Rotations

## Contributors
adisarcar
sidk256

## Test Cases
`rotationFlower.py` builds one rose-curve petal, then applies a
rotation matrix `rot(phi)` at 8 evenly spaced angles (45° apart) and
plots each rotated copy so the petals visually tile into a full
flower. Note: as submitted, the script's `for i in range 8:` line is
missing the parentheses around `8` (should read `range(8)`) and will
raise a `SyntaxError` until fixed — recorded here exactly as
originally submitted.

## Software Installs
None beyond the repo's `.venv` (numpy, matplotlib — see
`requirements.in`).

## Solution Manual
1. `pip install -r requirements.in` (or reuse the repo root `.venv`).
2. Fix the `range 8` → `range(8)` typo noted above.
3. `python3 rotationFlower.py`, enter an angle when prompted, and
   confirm the 8 rotated petals form a symmetric flower.
