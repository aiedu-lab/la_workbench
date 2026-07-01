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


## Content Phase 2
[x] Status

### References
* [3Blue1Brown](
  https://www.3blue1brown.com/?topic=linear-algebra
)
* [GilbertStrang](
  https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/
)
* [Titanic](
  https://www.kaggle.com/competitions/titanic
)
* [BasicExercises](
  ../../.tmp/linear_algebra_python_exercises.txt
)
* [Colab](
  https://colab.research.google.com/
)
* [StudentSetup](
  ../setup/student/
)
* [DevWorkbench](
  ../../sessions/dev_workbench.md
)
* [GitAIWorkbench](
  https://github.com/aiedu-lab/ai_workbench
)
* [AIWorkbench](
  ../../../ai_workbench/
)

### Developer Workbench

#### VSCode & Claude
Reference the setup instructions of VSCode and Claude in 
the `sessions/dev_workbench.md` and the associated 
references of the sister repo `AIWorkbench`. 

You can reference the URL of those sessions per 
`GitAIWorkbench` to maintain DRY principle. However, 
students should have set up Claude, VSCode, and 
Claude extensions to ensure they are setup for 
the exercises. 

Additionally add a small subsection to setup 
the vscode extension to Colab.

#### Setup Scripts
Add a section to direct students run the scripts in 
`StudentSetup`, specifically `labsetup.py` and `preflight_check.py`

### Sessions/Projects

Factor in the links of the different lectures of 
`3Blue1Brown` and `GilbertStrang` into the corresponding session 
per the Agenda of README.md. These lectures are much better than any sessions 
an instructor can hold. 

Hence most of the sessions (if not all sessions) can simply have two sections:

* Concept
  Link to the appropriate lecture(s) of `3Blue1Brown` & `GilbertStrang`.
  If we need to combine sessions in Agenda or Session description to follow 
  more closely with the lectures, please do so.

* Exercise
  Link to the project/exercise corresponding to the lecture. Reference 
  the `BasicExercises` and split it out as appropriate so that 
  at the end of the specific session(s) that covers the concepts 
  needed to cover the exercise.
  If there is any session/exercise that does *not* have a corresponding
  exercise, please create one.

### Kaggle Titantic

Add the `Titanic` exercise at the end of an appropriate session 
or create a separate session for that project at an appropriate slot in 
the agendda. 

## Cleanup
[x] Status

### Validate Skill

Reference:
* `.claude/commands/replan.md`
* `.claude/commands/execute.md`

I refactored `replan.md` to `replan.md` that only generate a plan phase 
and `execute.md` that only executes the latest plan phase. Please 
validate the skills.

### Add `Toy` Exercises

Reference
* [what is a model](../../sessions/what_is_a_model.md)
* [why linear algebra](../../sessions/why_linear_algebra.md)
* [sessions](../../sessions/)
* [projects](../../projects/)
* [linear transformations](../../projects/linear_transformations/README.md)

1. The sessions `what is a model` and `why linear algebra` are 
just overview sessions. The session `kaggle titanic capstone` 
is a capstone project. Except these sssions, ensure that any  
other session is accompanied by an exercise. Whether a
session has an exercise is easily identifiable by observing whether
a session has a non-empty `## Exercise` section.

2. The corresponding exercise should be in the projects folder with a 
subfolder with the topic name. There should be a README.md in that 
subfolder that defines the exercise - reference `linear transformation`
project as an exercise. The session `## Exercise` section 
should cross reference that project subfolder.

3. The structure of the exercise is to solve a problem framed as 
a linear algebra exercise that could be run in colab or jupyter 
with a validation and visualization component to build intuition 
of the concept. 

To reduce cognitive load, add a help section to README that 
suggests the visualization commands in python that helps visualize
a vector, matrix, transformation, etc. as appropriate.

4. Any new exercises generated must be `toy` (basic) in nature 
as the objective is NOT to sweat but to build the intuition. 
Moreover, we already have a `kaggle titanic capstone` overarching 
capstone project that can help students bring all concepts together.
Hence, a new exercise can be basic.

5. The exercise creation is not needed for sessions 
that already have a corresponding project, such as 
`linear transformation`. However, those sessions with
exercises specified should have a validation and visualization 
component to build intuition. 

6. At the end, clean up any project subfolder that does not have 
any exercise content to clean up any old subfolders left behind. 
