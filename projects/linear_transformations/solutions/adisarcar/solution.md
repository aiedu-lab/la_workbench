# Solution: Resize the Rocket / Make It Lean

## Contributors
adisarcar
sidk256

## Test Cases
* `rocketDilation.py` (Part 1) applies the dilation matrix
  `[[1/2, 0], [0, 2]]` to a hand-drawn rocket outline and plots the
  original (red) against the transformed shape (blue) so the
  squeeze-x/stretch-y effect is visible side by side.
* `makeitlean.py` (Part 2) applies a shear matrix `[[1, k], [0, 1]]`
  with `k = 0.5` to an upright letter "F" and plots the original
  (green) against the sheared shape (red) to show the lean.

## Software Installs
None beyond the repo's `.venv` (numpy, matplotlib — see
`requirements.in`).

## Solution Manual
1. `pip install -r requirements.in` (or reuse the repo root `.venv`).
2. `python3 rocketDilation.py` — compare the red/blue rocket outlines.
3. `python3 makeitlean.py` — compare the green/red "F" outlines.
