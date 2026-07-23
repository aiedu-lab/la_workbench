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

## Contribution
[x] Status

### Background

This workbench is meant to help student learn, create 
a body of work that is available for their own reference 
and for the reference of others, say applications to 
internships, camp programs, etc.

#### Record Contribution

Suggest mechanisms via which a student or group of 
students can submit their solution - approach and code 
that becomes a record of their contribution.

##### Possible Example Approach

The below approach is to serve as an example as you 
may come up with a better approach:

1. create a subdirectory inside the exercise directory 
  in `projects/<exercise>` - the name of the subdirectory
  can be the list of github-userid of the student. 
  Example `alpha` if the solution is contributed 
  by `alpha`. If a group collaborate on the project then
  any one of them can submit the solution, as the 
  contributors are anyway spelled out in a markdown file 
  inside that directory in any case - reference next
  line item for details.

2. submit a PR `project/<exercise>/<github-userid>` that has 
  the exercise solution with the following files:
* solution.md: there are separate sections for
  * contributors: alphabetically ordered list of 
    `<github-userid>: Full User Name` students in the group that 
    created the solution. 
  * test cases: ran by the student to validate the solution
  * software installs: in local .venv if required
  * solution manual: instructions on how to run the solutions
    and test cases to validate the solution.
2.2. code files:
* requirements.in (for any installs)
* python files
* ... any files e.g. sample data

2.3. On validation of the solution: 
* the maintainer/admin approves the pull request and the 
  student's contribution is recorded as an approved 
  checked in subdirectory with solutions in github.
* this approval triggers running a script in
  `miscellaneous/report/report.py` which updates a 
  `miscellaneous/report/report.md` file that is 
  a table of all the sessions in column and the
  list of students in alphabetical order that have 
  completed the exercise. note that the updated 
  report.md should be available in main branch as 
  a record. Ideally this step is automated and 
  triggered automatically when a PR is approved
  by a maintainer.

#### How to submit solution for each exercise?

Create a section in `README.md` at root of the repo. The section
is appropriately named to tell students on how to submit solutions
for each exercise. If approved by the teacher, how students 
validate their solution was recorded.

#### First recording

Reference [sol][../../.tmp/linear_algebra_workbench_solutions]

Two students submitted their solutions before we had set up a 
process on `how to submit solution for each exercise`. 
Their names and github-userids are:

| #   | Full Name         | GitHub-UserId |
| --- | ----------------- | ------------- |
|   1 | Aditya Sarcar     | adisarcar     |
|   2 | Siddharth Kayath  | sidk256       |

1. They have submitted solutions that is available in `sol`.

2. Figure out which exercise it solves. For each of them
   create a subdirectory by the `<Github-UserID>` of any one of 
   these students and then create the appropriate additional 
   files in that directory along with the solution python 
   file.

3. Once all the solutions are created submit a pull request
   for it to be approved and recorded in the repo.

Push all the new content in this repo branch to origin and
submit pull request. Suggest what and how to trigger the 
creation of the report table once PR is approved?

#### Reflect in sister repo - AI Workbench

Reference sister repo `../../../ai_workbench/`

Reflect the changes in `how to submit solution ...`, 
reporting script, report markdown file, and instructions
in `README.md` to how students can submit solution and
validate it was approved and available for records.

Update the `prompt_history.md` of that to record the 
change for historical reasons.

Push all the new content in this repo branch to origin.

### Addendum: Refined Requirements (2026-07-02)

* `solution.md` Contributors section: bare GitHub-UserId per line;
  `report.py` resolves Full Name from the GitHub-UserId via the public
  GitHub Users API rather than requiring it typed manually.
* `report.py` must be idempotent — re-running with no new/changed
  submissions leaves every generated file byte-identical.
* Add a per-student report `miscellaneous/report/student/
  <github-userid>-report.md`: Full Name, GitHub-UserId, Date Last
  Updated, then a table of every exercise topic, a short concept
  description, and a completion checkmark.
* Applies to both `la_workbench` and `ai_workbench` (see Step 4.6).

## Cleanup Contribution
[x] Status

Reference
* [readme](../../README.md)
* [report-workflow](../../.github/workflows/report.yml)
* [exercise](../../projects/<exercise>/)
* [report](../report/)
* [report-data](../report/report.md)
* [student](../report/student)
* [AI-Workbench](../../../ai_workbench/)

1. Move the solutions folder in each `exercise` under a subdirectory
`solutions/` to ensure the `exercise` directory is clean. For 
example, move `projects/linear_transformations/adisarcar` should 
be `projects/linear_transformations/solutions/adisarcar`.

3. Update the `report.py` to add another line `Full Name: <full name>` 
   of the student in the per student report inside the `student` 
   directory ASSUMING the student's full name can be extracted 
   from GitHub using the GitHub-UserId.

4. Rename `report` to `reporting`, Rename `report.py` inside `report`
   to `generate_reports.py`, Rename `report-data` to `summary_report.md`

4. Rename `student` to `for_each_student`.

5. Ensure consistency of all content that are impacted by the move.
Few examples are: 
* `report.py` inside `reporting`.
* `readme`
* `report-workflow`

6. Reflect all these changes you made in this repo in the sister repo
   `AI-Workbench` and add    these changes to the `prompt_history.md` 
   file (for historical records) that is sitting inside `AI-Workbench` 
   sister repo.

## Gaussian Elimination
[x] Status

References:
* [all-sessions](
  ../../sessions/
)
* [systems-session](
  ../../sessions/systems_of_linear_equations.md
)
* [systems-exercise](
  ../../projects/systems_of_linear_equations/
)
* [readme](
  ../../README.md
) 
* [setup](
  ../setup/student/labsetup.py
)
* [elimination-solution](
  ../../projects/systems_of_linear_equations/solutions/elimination/sidk256/solution.md
)
* [workbench](
  ../../sessions/dev_workbench.md
)

### Installation
Prior to running any python exercise, the student should activate a virtual 
environment. This could either be the root repo's .venv or a local .venv.
Furthermore, if any additional installations are required, we suggest 
do it inside a virtual environment using `requirements.in`. For reference 
have a look at `elimination-solution`.

* Review all the solutions already added in projects/<project-name> 
directories and ensure the documentation is clear.

* Add to a central plan, say `setup`, the above suggestions to 
reinforce the environment and install setup.

### Gaussian Elimination
We now have two exercises in `systems-exercise` - one uses linear algebra
functions in numpy and one that solves the systems of linear equations
using elimentary elimination - gaussian elimination.

The solution to the original exercise `the snack bar mystery` directly 
used linear algebra function `np.linalg` - it has been moved inside 
`linalg` subdirectory inside the solutions directory of `systems-exercise`.

The new solution to another exercise using elimination has been moved 
inside `elimination` subdirectory inside the solutions directory of 
`systems-exercise`.

* Update the `systems-session`, section `Exercise` to reflect 
both the exercises.

* Update the `README.md` of `elimination-solution` to articulate the
exercise.

* The same session `systems-session` could have multiple exercises
as was in the case. Ensure that the reporting tables are not messed 
up for these cases and we get to reflect multiple exercises as 
well for the report of `all-students` as well as the report
`for-each-student`.

* Given that we now have two exercises for `systems-exercise` and the
original exercise has been moved inside `linalb` subdirectory, ensure
that all references to paths and files are correct and validated 
after this move.

## Cleanup Solutioning
[x] Status

### Maintainer
Relative to repo root:
* Move the `miscellaneous/setup/instructor/repo.md` inside a new directory 
from REPO root `miscellaneous/setup/admin/`
* Crate a new file inside this new directory `miscellaneous/setup/admin/`
named `member.md` with a section that uses `gh` CLI command to change
the list of members one as a contributor, one as a maintainer, one to 
move from maintainer to contributor, and one from contributor to 
maintainer. 
* Reference GitHub documentation that explains the privilege review and 
amend commands. Add a note that `gh` for the user should be authorized 
to run this command with appropriate (admin?) privileges including
what `gh` command to run to find out your privileges and what should
the privilege be (admin?) to run above commands.  
* Create another new file inside a new directory relative to REPO root
`miscellaneous/setup/maintainer/pull_request.md` with `gh` commands to
approve, reject, amend, ... the pull request changes.

### Rephrase
Reference
* [setup-repo](../setup/instructor/repo.md)
* [readme](../../README.md)
* [solution-submit](../../README.md#-submitting-exercise-solutions) step 3
* [solution-template](../reporting/solution_template.md)
* [generate-report](../reporting/generate_reports.py)
* [ai-workbench](../../../ai_workbench/)

Current description of `solution-submit` is prone to errors as downstream
GitHub actions to generating report depends on few sections clearly
laid out or else errors result.

`solution-submit` step 3 phrasing after the first line 
`3. Create projects/<project-name>/solutions/<github-userid>/ —`
is very verobse and prone to error. 

Instead of 
```text
   <project-name> is the matching project subfolder for the session
   (e.g. projects/embedding/), and <github-userid> is any one member's
   GitHub user id if you worked in a group. Inside it, add:
   * solution.md starting with a `# Solution: <Exercise Title>`
     heading (the completion report uses this to label and credit
     each exercise separately when a session has more than one),
     then four sections:
     ```text
     * ## Contributors: one GitHub-UserId per line
     * ## Test Cases: What you ran to validate your solution
     * ## Software Installs: Anything beyond the repo's usual toolchain
     * ## Solution Manual: How to run your solution and its test cases
     ```
   * your file(s):
     * requirements.in (or equivalent) for any extra installs
     * all source files
```
rephrase so that students can just copy the 
`solution-template` file and edit each section ensuring
that the `Solution`, `Contributors`, and any other fields used by
the GitHub workflow and `generate-report` process correctly without
any errors.

### Validate

#### Git Commit Hook
Suggest a way so that incorrectly formatted soluton.md that 
craps out the GitHub workflow and `genereate-report` is rejected
during git commit.

#### Test
Rerun the GitHub workflow a valid solution.md file and an 
incorrectly format solution.md to ensure that the process of
reporing is resilient. 

### Reflect
Reflect all these changes in sister repo `ai-workbench`. Update the
prompt_history.md in the sister repo for records. git commit
the changes. The push to origin can be manually driven.

## Pull Request
[x] Status

Reference
* [contributor](../setup/contributor)
* [setup-repo](../setup/contributor/contributor.md)
* [maintainer](../setup/maintainer)
* [admin](../setup/admin)
* [readme](../../README.md)
* [ai-workbench](../../../ai_workbench/)


### Contributor
Students and instructors are roles based on educations.
Contributors, maintainers, or admins are GitHub roles.

Generally:
* students are contributors.
* instructors could be contributors, maintainers, or even admin

1. Create new directory `contributor`. Create a new file inside that 
directory as `contributor.md`. Add sections on
* Submit PR: `gh` CLI command to submit pull request and commands 
* Validate: `gh` CLI command to validate the role and auth of the 
user as a contributor.

2. Rename the file pull_request.md inside `maintainer` as maintainer.md 
as the file will have all information that a maintainer should know 
including but not limited to pull request handing. 
Add a section that helps user validate with `gh` CLI command to 
cross-check the role and auth of the user is sufficient to be a 
maintainer.

3. Consolidate the files repo.md and member.md into one file
admin.md inside `admin` directory. It will have all information
that an admin should know including section for repo and section
for members. Add a section on how a user may validate with `gh` 
CLI command to find and cross-check the role and auth of the user 
is sufficient to be an admin.

4. Update README.md appropriate section, such as 
`Contribution Guidelines` for contributors, with a reference to
the contributor.md. Similarly, add sections for 
`Admin Guidelines` and `Maintainer Guidelines`. 

As discussed above, these sections are distinct from the Student 
and Instructor setup and other commands that should be kept as is. 
Add a note clearly separating the Student/Instructor education 
roles from Contributor/Maintainer/Admin GitHub roles.

### Validate
Given the file moves, renames, and consolidation above (repo.md +
member.md → admin.md; pull_request.md → maintainer.md; new
contributor.md), ensure that all references to these files or
directories — in README.md, in the moved/renamed files' own
cross-links, and anywhere else in the repo — are correct and
updated after this restructure.

### Reflect
Reflect all these changes in sister repo `ai-workbench`. Update the
prompt_history.md in the sister repo for records. git commit
the changes. The push to origin can be manually driven.

## Test One
[x] Status

### Testing Philosophy
For each test below create a one hour multiple choice problem 
set of 12 questions each that students can attempt alone
or in collaboration. 

This is an academic test and meant to validate that students
have the theory and problem solving background to accompany 
the hands of practical aspect of workbench.

33% of those questions are basic difficulty, 33% of them are
medium difficulty, and 33% of them are high difficulty. 
None of them will test a lot of numerical jugglery. 

The emphasis is that if students understand the concepts, 
intuition, and visual imagery, they should be able to solve
the problem. 

Collaboration among students are allowed and even encouraged
so that they can discuss to clarify the concept and visual 
intuition to come up with the solution. 

The expectation is that students check the right answer or 
answers If there are  multiple options correct with a very 
short description (no more than a paragraph of 100 words at most)
of the basic concept, approach, and visual intuition the 
student(s) used to craft the solution.

### Test Linear Algebra **Systems of Linear Equations**

Reference:
* [AGENDA](../../README.md#agenda)
* [sessions](../../sessions/)
* [scalars vectors and matrices](../../sessions/scalars_vectors_matrices.md)
* [systems of linear equations](../../sessions/systems_of_linear_equations.md)
* [test scalars to linear equations](
  ../../tests/test-scalars-to-linear-equations.md
  )
* [solution scalars to linear equations](
  ../../tests/solutions/soln-scalars-to-linear-equations.md
  )

1. Generate the 12 questions as `test scalars to linear equations` based 
on all the content and concepts that is covered between and including the 
sessions `scalars vectors and matrices` and  `systems of linear equations` 
in the `AGENDA`.

2. Generate the solution to the tests as `solution scalars to linear equations`.

3. Add the test as a separate test session immediately after the 
session of `systems of linear equations` in `AGENDA` hyperlinking to 
`test scalars to linear equations`. Add the solution hyperlink to the 
same session for reference.

### Test AP Calculus BC
Reference
* AP Calculus BC Course Content
  * Units 1–8: AB Calculus Topics
    * Unit 1: Limits and Continuity
    * Unit 2: Differentiation: Definition and Fundamental Properties
    * Unit 3: Differentiation: Composite, Implicit, and Inverse Functions
    * Unit 4: Contextual Applications of Differentiation
    * Unit 5: Analytical Applications of Differentiation
    * Unit 6: Integration and Accumulation of Change
    * Unit 7: Differential Equations (including Logistic Growth and Euler's Method)
    * Unit 8: Applications of Integration (including Volumes of Revolution and Arc Length)
  * Units 9–10: BC Exclusive Topics
    * Unit 9: Parametric Equations, Polar Coordinates, and Vector-Valued Functions 
    (e.g., derivatives and integrals on curves, polar area)
    * Unit 10: Infinite Sequences and Series (e.g., convergence tests, 
    Taylor and Maclaurin polynomials, and power series)
* [AP Calculus BC Course](
  https://apcentral.collegeboard.org/media/pdf/ap-calculus-ab-and-bc-course-and-exam-description.pdf
)
* [test limits and continuity to analytical apps of diff](
  ../../tests/test-limits-continuity-to-analytical-apps-of-diff.md
  )
* [solution limits and continuity to analytical apps of diff](
  ../../tests/solutions/soln-limits-continuity-to-analytical-apps-of-diff.md
  )

1. Generate the 12 questions as 
`test limits and continuity to analytical apps of diff` based 
on all the content and concepts that is covered between and including 
`Unit 1` and `Unit 5` given above in the reference and as expressed 
in the course content at `AP Calculus BC Course`.

2. Generate the solution to the tests as 
`solution limits and continuity to analytical apps of diff`.

3. Add the test as a separate test session immediately after the 
session `test scalars to linear equations`. Add the solution hyperlink
to the same session for reference.

## Partial Derivatives and Multivariate Calculus
[x] Status

Reference: 
* [partial](/.tmp/partial_derivatives_and_multivariate_calculus.md)
* [sessions](/sessions/)
* [projects](/projects/)
* [AGENDA](/README.md#agenda)
* [column-space](/sessions/column_space_rank.md)

### Objective
Create a introductory session introducing the concept of partial 
differentiation and multi-variate calculus. This introduces the
concept of gradient. 
**Later** we will set up Gradient will then be used to elaborate 
Taylor Expansion to approximate a function in a neighborhood.
**Later** we will tie together in how gradient is used for
basic machine learning to minimize error function.

### Tasks
* Create a session 'Partial Derivatives and Multivariable Calculus'
  Reference `partial` student session to create the sesion, 
  instead of ascii images use mermaid diagrams, for the session.
  You can reference another session in `sessions` to motivate
  the structure of the lesson.

* Add the session in `sessions` and cross reference the session in 
`AGENDA` - before the `column-space` session. 

* Add a simple paper problem and associated coding exercise 
(using np.linalg) on taking the example of a multi-variable 
function f(x,y) that computes the derivative using partial 
derivatives. 

Assume that the second variable is a function of the first 
variable i.e. y = g(x) and show how 
the results are same when computing the full derivative of f wrt x.

* As with other exercises, ensure that we have the corresponding 
`projects` directory that has the folder for the exercise and
as consistent with other projects we should have a README in that
folder with clear description of the codign exercise and sample
code to visualize any effects.

### Addendum: Revised Scope (2026-07-23)

**Round 1:**
* Keep the `.tmp` reference file's ASCII-art diagrams as-is in the
  new session — Mermaid is only suited to simple box/flow diagrams,
  not these directional/3D sketches.
* The Partial Derivatives exercise must include Python code that
  visualizes the chosen `f(x, y)`, plus two slice plots — one with
  `y` frozen (varying `x`), one with `x` frozen (varying `y`) — to
  build visual intuition for what a partial derivative is.
* Add a small section to the Partial Derivatives exercise showing
  how to find a function's max/min via its partial derivatives
  (gradient equal to the zero vector).
* Add a new session, **before** Partial Derivatives, covering
  single-variable calculus: a paper-and-code exercise that
  visualizes a curve, finds its max/min via the first derivative
  equal to zero plus a second-derivative check, and mirrors the
  same gradient-descent-style coding exercise (in 1D) used later
  for the multivariable minimum — building intuition in one
  variable before generalizing to several.

**Round 2:**
* Add MIT OCW 18.02 *Multivariable Calculus* (Fall 2007) [video
  lectures](
    https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/video_galleries/video-lectures/
  ) as a new `## Reference` section on sessions where the lecture
  content actually matches — e.g. Lectures 8-12 for the Partial
  Derivatives session (partial derivatives/tangent plane, max-min
  problems, the second-derivative test, differentials/chain rule,
  and the gradient/directional derivative).
