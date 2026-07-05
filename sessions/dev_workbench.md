# Development Workbench Setup

## Sign Up for Google Colab

Before anything else, create a free account at
[colab.research.google.com](
  https://colab.research.google.com/
).

Why Colab:

* **Zero configuration** — write and run Python in your browser,
  no local install required.
* **Free GPU access** — useful once exercises move from toy NumPy
  arrays to PyTorch tensors.
* **Easy sharing** — a notebook link is enough to hand in or
  review an exercise.
* A free account also gives access to popular LLMs and the Gemini
  API, handy for the AI-connection side of this course.

## VSCode & Claude Code Setup

This repo's dev-tool setup mirrors the companion
[ai_workbench](https://github.com/aiedu-lab/ai_workbench) repo —
follow its guides directly rather than duplicating them here:

* [VSCode](https://github.com/aiedu-lab/ai_workbench/blob/main/miscellaneous/tools/dev_workbench/vscode.md)
* [GitHub & Git](https://github.com/aiedu-lab/ai_workbench/blob/main/miscellaneous/tools/dev_workbench/github_and_git.md)
* [Claude Account](https://github.com/aiedu-lab/ai_workbench/blob/main/miscellaneous/tools/claude/cloud.md)
* [Claude Code CLI](https://github.com/aiedu-lab/ai_workbench/blob/main/miscellaneous/tools/claude/cli.md)

Install each in order, then confirm VSCode opens this repo, `git`
is authenticated, and `claude` runs from this repo's root.

### Colab Extension

Install the **Colab** extension for VSCode (or the Jupyter
extension with the Colab connector) so notebooks started in Colab
can be opened and edited from VSCode, and vice versa, without
re-uploading files.

## Run Lab Setup Script

With VSCode and Claude Code ready, set up the Python environment
this course's exercises run in:

```bash
python3 miscellaneous/setup/student/labsetup.py
```

This creates a `.venv` at the repo root, installs NumPy, PyTorch,
Jupyter, and matplotlib from `requirements.txt`, and registers a
`la-workbench` Jupyter kernel. It is safe to re-run at any time.

Validate the environment:

```bash
python3 miscellaneous/setup/student/preflight_check.py
```

Every line should read `PASS`:

```
=== Preflight Check ===

PASS  .venv exists
PASS  requirements.txt up to date
PASS  numpy importable
PASS  torch importable
PASS  matplotlib importable
PASS  jupyter importable
PASS  ipykernel importable
PASS  Jupyter kernel 'la-workbench' registered

All items must show PASS before the lab begins.
```

If any check shows `FAIL`, re-run `labsetup.py` and try again
before moving on to the next session.

## Running Exercise Solutions

Before running any exercise or solution script, activate the
repo-root `.venv` set up above:

```bash
source .venv/bin/activate
```

If a solution's own `requirements.in` needs installs beyond the
repo-root environment, create a `local .venv` inside that
solution's own directory instead — see
`projects/systems_of_linear_equations/solutions/elimination/sidk256/solution.md`
for a worked example:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.in
```
