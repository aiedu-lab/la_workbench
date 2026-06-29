# Prompt History

This file maintains a chronological ledger of prompts that led to the 
creation and evolution of the Specification Driven Workbench (SDW) for
Linear Algebra Workbench.

## Purpose

**Prompt:** "Act as an applied math educator. I want to build a hands-on 
Linear Algebra lab for high schoolers and undergrads. The lab should teach 
them on the practitioners perspective of linear algebra concepts and how 
it is used to power ML and AI applications. I want this to be a 
'Specification Driven' project where we define the plan in markdown first."

---

## Context
[x] Status

This repository (la_workbench) is a mirror image of the sister 
repository (ai_workbench). The contents and objective of this 
repo is to educate kids via practical handson simple exercises 
about the concept of Linear Algebra. More on local `README.md`

References:
* repo (la_workbench) location relative to this file: `../../`
* objective of this REPO: `LOCAL_REPO_LOCATION/README.md`
* repo URL: `https://github.com/aiedu-lab/la_workbench`.
* sister repo (ai_workbench) location: `../../../ai_workbench/`
* objective of sister repo (ai_workbench): `SISTER_REPO_LOCATION/README.md`
* sister repo URL: https://github.com/aiedu-lab/ai_workbench

## Repo Hygiene

The local repo should have the same hygiene as the sister 
repo ie. no one can commit to main branch, everyone 
makes changes to a branch, and submits a pull request.

Create a markdown file in `miscellanaous/setup/instructor/repo.md`
that has: 
* step by step instruction on what all settings we tweak at 
GitHub to maintain the hygiene as specified above.
* ensure the contribution hygiene reflects the norms of the
sister repo.

### Structure of Repo

#### Common Utilities
I've  copied: 
* .gitignore, .github, and skills from sister repo 
(.agent, .claude). 
* operating guardrails (CLAUDE.md with AGENTS.md as symbolic 
link to avoid duplication). 

Copy as appropriate any other (non content specific) 
environmental files to the local repo.

Update and contextualize all these files as appropriate 
to reflect the objectives of the local repo rather than 
that of the sister repo. 

#### Review `README.md`

Update `README.md` similar to sister repo `README.md`.

Update Agenda of `README.md`
* Reflect the sister repo's `README.md` style where agenda cross 
links to sessions and projects (exercises). 
* Reflect the sister repo's format where we've an introduction and 
developer workbench setup session in Agenda. 

#### Review Setup

Reflect the sister repo's `miscellanaous/setup/` where we've one
for `instructor/` (already created) and one for `student/`

Create a labsetup.py and preflight_check.py where we set up 
NumPy, PyTorch, Jupiter, and some common tools (that we'll add 
as we discover more and build the agenda) in .venv in 
LOCAL_REPO_ROOT with a requirements.in, requirements.txt, etc. 

#### Update `Sessions`, `Projects`
* Create placeholders sessions in `sessions/` with exercises 
reflected in an appropriate directory in `projects/`.

---

## Companion Relationship with AI Workbench
[x] Status

**Prompt:** "Add to README.md a note that la_workbench, while
independent of ai_workbench, is a companion session: Linear
Algebra fundamentals help students grok ai_workbench's exercises,
turning the often-dry theory of Linear Algebra into something
alive once they see how it powers real-world AI systems.
Symmetrically, update ai_workbench's README.md to note that
linear algebra mechanics are the engine that makes the AI
Workbench exercises come to life."
