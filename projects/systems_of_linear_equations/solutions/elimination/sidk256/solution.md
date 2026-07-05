# Solution: Gaussian Elimination

## Contributors
adisarcar
sidk256

## Test Cases
`gaussian_elimination.py` solves a system of equations with
6 variables and 6 equations with basic gaussian elimination
technique.
Finally, it prints the value of the variables
`x1, x2, x3, x4, x5, x6` as answer.

## Software Installs
* NONE beyond the repo's `.venv` that already has numpy —
  see `requirements.in`.
* IF you want to use the local .venv, run:
```bash
  python3 -m venv .venv &&\
  source .venv/bin/activate &&\
  pip install -r requirements.in
```

## Solution Manual
* Run gaussian elimination:
  `python3 gaussian_elimination.py`.
* Confirm the printed solution satisfies six equations:
  `x1, x2, x3, x4, x5, x6`
