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

## Minimize Least Squares
[x] Status

Reference:
* [partial](/sessions/partial_derivatives_multivariate_calculus.md)
* [projects](/projects/)
* [AGENDA](/README.md#agenda)

### Define the problem
Add a section in `partial` on 'Minimizing Least Square' i.e.
set of N input and output points (x_i, y_i) and we are to choose
two variables slope (a) and intercept (b) such that we 
minimize the average of the "dispersion":
f(a,b) = 1/N*(y - (a*x_i + b))^2.


* Point out that this is an multi-variable minimization problem,
  where the two variables are a and b.
* Find (a, b) the minimum value of f solution of `fa = ∂f/∂a` and `fb = ∂f/∂b` are zero 
* Create a paper exercise with N points of x_i, y_i and show that
  the (a,b) where f(a,b) is minimized is:
  * b = Ave(y_i) - a*Ave(x_i) and a = Cov(x_i, y_i)/Var(x_i), where: 
    Ave = average = 1/N*sum(), 
    Cov = Ave(x_i*y_i - Ave(x_i)Ave(y_i))
    Var = Ave(x_i - Ave(x_i))^2 
  * Map this analytical formula in linear algebra terms using:
    X = vec(x) = [x_1, x_2, ...]^T, Y = vec(y) = [y_1, y_2, ...]^T,
    vec(1) = [1, 1, ...]^T,  
    Ave(X) = 1/N*vec(1)^T.X, Ave(Y) = 1/N*vec(1)^T.Y, 
    Cen(X) = X - Ave(X)*vec(1), Cen(Y) = Y - Ave(Y)*vec(1), where
    Cen(X) or Cen(Y) is the "centered vector" i.e. translated around mean 
    Var(X) = 1/N*Cen(X)^TCen(X)
    Cov(X,Y) = 1/N*Cen(Y)^TCen(X), with solution:
    a = slope = Cov(Cen(X), Cen(Y))/Var(Cen(X)) and a*Cen(X) is 
    [Cen(Y).(Cen(X)/|Cen(X)|)]*(Cen(X)/|X|) i.e. projection of
    Cen(Y) on Cen(X), AND
    Correlation = cosine of angle between Cen(Y) and Cen(X) is 
    \rho = (Cen(Y)/|Cen(Y)|)^T*(Cen(X)/|Cen(X)|)
  * Add an exercise in the correspoding folder within projects to compute
    the best fit least square line among a list of N points. Add the 
    visualization of the best fit line with the sample code to 
    visualize added to README as has been our norm.
* Explain in simple non-jargon terms that students can understand as
  to what the solution for slope and intercept intuitively means: 
  a (slope) = ratio of how much x_i and y_i move together versus
  how much x move and 
  b (intercept) is simply the 'lift' we need to give
  on average on the a*x_i to get to y_i.

### Generalize the problem
'Minimizing Least Square' is not just a linear equation fit
problem i.e. find a and b such that Y = aX + b least square 
error is minimized.
* Exponential problems can be mapped to the same after some 
  axis normalization i.e. find a and d such that 
  Z = d*exp(aX) least square error is minimized is mapped 
  to linear regression, where Y = ln(Z) = aX + b, and b = ln(d).
* Quadratic problems can be mapped to linear regressions
  i.e. find a, b, and c such that
  Y = a*X^2 + b(X) + c least square error is minimized is
  mapped to linear regression by evaluating the partial 
  derivatives of Y wrt a, b, and c respectively. 

### Conclusion
Conclude with the unifying insight:
* Statistics starts with averages, variances, and covariances.
* Linear algebra reveals that these are simply projections, 
  lengths, and dot products, thus treating least-squares 
  regression as projecting the output vector onto the subspace 
  spanned by the input vectors

## Critical Points
[x] Status

Reference:
* [toc](/.tmp/critical_point_toc.md)
* [critical points overview](/.tmp/critical_points_overview.md)
* [single variable](/sessions/single_variable_calculus.md)
* [multi variable](/sessions/partial_derivatives_multivariate_calculus.md)
* [critical points](/sessions/critical_points)
* [critical points exercises](/projects/critical_points/)
* [systems of linear equations exercise](/projects/systems_of_linear_equations/)
* [agenda](/README.md#agenda)
* [videos](
  https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/video_galleries/video-lectures/
)
* [problems](
  https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/pages/assignments/
)

### Objectives

Developing undergraduate 101 level hands on workbench course on 
linear algebra. Here we are adding content to discover, evaluate,
and analyze critical points. How to optimize and reduce error to 
learn a function from data in machine learning.

* Add a session titles 
"Critical Points and the Second Derivative Test" in
`critical points`.
* Add a exercise "Critical Points Exercises" in 
`critical points exercise`.  
* Redo `single variable` and `multi variable` sessions

### Tasks

1. Add a session `critical points`. Insert that session after 
`multi variable` in `agenda`.

2. Structure that session `critical points` covering the 
table of contents in `toc`. You can borrow the contents 
from `critical points overview` or reference highly 
ranked public internet content as in lectures 8 to 12 in 
`videos`.

4. Add subsections on paper exercises for each new concept. You 
can draw the problem sets from `problems`.

5. Add hands on project exercise(s) in `critical point exercise` 
with hyperlink from the exercise subsection of 
`critical points`. The structure of the hand on 
programming project can be drawn from 
`systems of linear equations exercise`. 

5. There is duplication of sections covered in 
`critical points` from the session and the associated exercise 
in `single variable` and `multi variable`. 
Remove those content - sections and corresponding exercises-  
from `single variable` and `multi variable` AND instead, 
wherever appropriate add forward references to the
sections on `critical points`.

6. Use mermaid diagrams to illustrate decision flow of how to 
identity and ascertain critical points for single and multi
variable use cases.

7. Remembering this is an introductory course, keep the language
simple and illustrate whenever possible with visuals and 
examples.

## Vector Calculus
[x] Status

Reference:
* [vector calculus video](https://www.youtube.com/watch?v=lKXW7DRyyro)
* [critical points](/sessions/critical_points.md)
* [vector calculus](/sessions/vector_calculus.md)
* [vector calculus exercise](/projects/vector_calculus/)
* [agenda](/README.md#agenda)

### Objectives
* Add a session on 'Vector Calculus'
* Add a paper and hands on project on vector calculus
* Use proper mathematical formula notations, such as nabla, delta, etc.

### Tasks
* Add a session `vector calculus` and place it in `agenda` right after 
`critical points`.

* Add a motivation section to `vector calculus` with associated practical 
examples of domain problems it covers, such as physics, signal 
processing, machine learning and artificial intelligence, etc.

* Cover the below topics in concept and paper exercise against each 
subsection. 

* Add associated coding project in `vector calculus exercise`
folder against each subsection below.

* Structure the concept based on the below example content:

#### Gradient $\vec{\nabla}$

* Purpose: The gradient tracks the maximum rate and direction of 
increase of a scalar field.

* Definition: function that maps a scalar multivariable function and
then maps it to vector field
$$
\vec{\nabla} f = 
\frac{\partial f}{\partial x}\hat{i} + 
\frac{\partial f}{\partial y}\hat{j} +
\frac{\partial f}{\partial z}\hat{k}
$$

* Applications:
- Physics: Mapping electric potential to electric field, 
  gravitational potential to gravitational field
- Machine Learning: Gradient descent - updates model weights 
  by moving in the opposite direction of the loss function gradient 
  to minimize errors from prediction to ground truth.
- Computer vision: Powers edge detection in image processing. 
  Software calculates brightness gradients across pixels to locate 
  sharp intensity transitions (edges).

#### Divergence $\vec{\nabla} \cdot \vec{\mathbf{F}}$

* Purpose: Divergence measures the net flow of a vector field out 
of a specific point, indicating whether the point acts as a source 
or a sink and the aggregate measure of the outflow.

* Definition: function that maps a vector field to a scalar outflow 
value
$$
\vec{\nabla} \cdot \mathbf{F} =
\frac{\partial f}{\partial x} F_x + 
\frac{\partial f}{\partial y} F_y +
\frac{\partial f}{\partial z} F_z
$$

* Applications:
- Fluid Dynamics: Enforces fluid mass conservation via the continuity 
equation. For incompressible fluids like water, the divergence of the 
velocity field is zero (\(\nabla \cdot \mathbf{v} = 0\)).
- Electrostatics: Forms the basis of Gauss's Law (the first of Maxwell's 
equations). The divergence of an electric field equals the local charge 
density, meaning positive charges are sources and negative charges are 
sinks.


#### Curl $\vec{\nabla} \cross \vec{\mathbf{F}}$

* Purpose: Curl measures the rotation or swirling intensity of a vector 
field around a specific point.

* Definition: function that maps a vector field to a vector filed
$$
\nabla \times \mathbf{F} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & 
\frac{\partial}{\partial y} & 
\frac{\partial}{\partial z} \\
F_x & F_y & F_z
\end{vmatrix}
$$ 

* Applications:
- Electromagnetism: Powers Faraday's Law and Ampere's Law 
(Maxwell's equations). A changing magnetic field induces a curling 
electric field, which is how electric generators create power.
- Computer Graphics: Simulates realistic smoke, fire, and water eddies. 
Real-time physics engines use curl noise to generate turbulent, swirling 
fluid effects without heavy computational overhead.


### Reference
Add a reference section to the `vector calculus` 
session right at the end with reference to 
`vector calculus video` and a couple of highest 
rated explanatory video, blog, article, or book 
on this topic.

## Vector Calculus Notation Fix
[x] Status

**Prompt:** "The gradient (nabla) is a vector, divergence is a dot
product of nabla (vector) and F (vector), and curl is a cross
product of nabla (vector) and F (vector). The rendering isn't
showing the vector symbol, and the vector symbols (nabla, F, etc.)
aren't shown in bold. Fix this everywhere the mathematical symbols/
vectors are shown, and record it in prompt_history."

### Scope clarification
Asked whether the fix should cover only `vector_calculus.md`, only
the sessions already using nabla/vectors formally (`critical_points.md`,
`partial_derivatives_multivariate_calculus.md`), or every session
with any vector/matrix reference. The user chose the broadest
option: **every session with any vector/matrix reference.**

### Resolution
`sessions/vector_calculus.md` used plain Unicode/code-fence notation
(`∇f`, `∇.F`, `î ĵ k̂`) for Gradient/Divergence/Curl, losing the
`$\vec{\nabla}$`/`$\vec{\mathbf{F}}$` LaTeX styling this section's
original prompt specified. Fixed by switching to GitHub-native
LaTeX math (`$...$`/`$$...$$`), the only way to actually render
arrow (`\vec{}`) and bold (`\mathbf{}`) vector styling.

An audit of every `sessions/*.md` file for bare vector/matrix
symbols found only 6 files needing this fix — `vector_calculus.md`,
`critical_points.md` (gradient, Hessian, displacement/direction
vectors), `partial_derivatives_multivariate_calculus.md` (gradient,
centered vectors), `matrix_multiplication.md`, `systems_of_linear_
equations.md`, and `column_space_rank.md`/`orthogonality_
projections.md` (matrix `A`, vectors `x`/`b`). Every other session
already describes vectors/matrices entirely in prose with no bare
symbols, so needed no changes. `projects/*/README.md` files were
left untouched everywhere — their `F`, `A`, `b` mentions are Python
identifiers tied 1:1 to the accompanying code cells.

Convention applied: `\vec{\nabla}` for the nabla operator (arrow
only); `\vec{\mathbf{F}}` for vector fields (arrow + bold, per the
original vector-calculus prompt); plain `\mathbf{}` bold for other
vectors/matrices (`x`, `b`, `v`, `u`, `a`, `A`, `H` the Hessian);
scalars and literal Python code left unchanged.

## Parameterization
[x] Status

References:
* [Single Variable Session](/sessions/single_variable_calculus.md)
* [Single Variable Project](/projects/single_variable_calculus/)
* [Partial Session](/sessions/partial_derivatives_multivariate_calculus.md)
* [Partial Project](/projects/partial_derivatives_multivariate_calculus/)
* [Partial Chain Ideas](/.tmp/partial_derivatives_chain_rule.md)
* [Parameterization Ideas](/.tmp/parametrization_degrees_of_freedom_lesson.md)
* [Hessian Ideas](/.tmp/hessian.md)
* [Parameterization](/sessions/parameterization.md)
* [Parameterization Project](/projects/parameterization/)
* [Critical Points Session](/sessions/critical_points.md)
* [Critical Points Project](/projects/critical_points/)
* [AGENDA](/README.md#agenda)

### Objectives

* Add a section on 'Chain Rule' for single and multi variable calculus
* Create a session on `Parameterization Session`
* Create a hands on project under `Parameterization Project Folder`

### Tasks

#### Chain Rule and Integration

* Update `Single Variable Session`: 
  * Add a section on concept of chain rule with example and 
    illustrative use case. Add a paper exercise on chain rule 
    for illustration.
  * Add a section on concept of single variable integration 
    and integration with substitution with change of variable.  
    Add example and illustrative use case. Add a paper exercise on 
    integration for illustration. 
  * Reference `Critical Points Session` for example content structure 
    and style.
* Update `Single Variable Project`: 
  * Add a hands on lab project on chain rule with example code 
    needed to plot and visualize.
  * Add a hands on lab project on integration with substitution and 
    change of variable with example code needed to plot and visualize.
  * Reference `Critical Points Project` for example content structure 
    and style. 
* Update `Partial Session`:
  * Add a section on concept of chain rule with example and illustrative 
    use case. Add a paper eercise on chain rule for illustration.
  * Add a section on Jacobian and variable change and substitution for 
    multi-variable integration. Reference `Partial Chain Ideas` for 
    session content example for this topic including what linear algebra
    constructs used to concretely and succinctly represent. 
  * Reference `Critical Points Session` for example content structure 
    and style.
* Reference `Partial Project` and `Partial Chain`:
  * Add a hands on lab project on chain rule with example code 
    needed to plot and visualize.
  * Add a hand on lab project on multi-variable integration with 
    substitution. Reference `Partial Chain Ideas` for 
    session content example for this topic including what linear algebra
    constructs used to concretely and succinctly represent.
  * Reference `Critical Points Project` for example content structure 
    and style. 

#### Create Parameterization Content

* Reference `Parameterization Ideas`
* Create a session `Parameterization` - for content and style 
  reference `Critical Points Session`.
* The session topics should cover `Degrees of freedom` 
  and various types of parameterization. Examples are 
  function parameterization of single and multi variable 
  arguments as well as paratemerization of ANY object type, 
  including functions. Add illustrative examples of all 
  object types. 
* Note how the `Parameterization Ideas` 
  clarifies how the partial derivative of function f(x,y)=xy
  yields the same derivate of g(x) = x^3, when we 
  constrain y=x^2 in f(x,y) i.e. the former is just a  
  parameterized and constrained one degree of freedome equation 
  version of the generic equation f(x,y)=xy with two degre. 
* Add few illustrative paper exercises in `Parameterization` 
  covering single variable, multi variables, functions, etc.
* Add few hands on lab project exercises in arguments - for 
  content and style reference `Critical Points Project`.
* Do NOT add any session content or project related to Hessian 
  matrix - derivation and details - to the `Parameterization`
  session or `Parameterization Project`. For example, session 
  `Connection to Hessian` in `Parameterization Ideas` - 
  concept, content, exercices - should NOT be represented in 
  `Parameterization` or `Parameterization Project`.
* Add a link to the `Parameterization` session in `AGENDA` 
  right before the `Critical Points Session`.

  
#### Update **Critical Points**

* Identity the content in `Critical Points Session` that
  goes over `saddle points`. 
    * Enclode that content into appropriately titled subsections in
      both the respective single variable and multi variable sections.  
    * Confirm that the conditions are specified for single variable
      i.e. second derivative is zero. Add an example equation.
      Add a corresponding project plt.plot of the example.
    * Confirm that the conditions are specified for multi variable
      i.e. Hessian positive definite nor negative definite. Add
      an example equation. Add a corresponding curvature plot 
      example in the corresponding project plt.plot of the example.

* Reference sections of `Parameterization Ideas` and `Hessian`
  as reference material on Hessian including definition, derivation 
  using parameterization, example paper project, example hands 
  on lab project. Specifically, reference the content - concept, 
  paper exercice, project exercise, etc. - in the section  
  `Connection to Hessian` in `Parameterization Ideas`.
  section of `Parameterization Ideas` - concept, content, exercices -  
* Review, restate as appropriate, and represent those session content 
  related to Hessian - as referenced above material to the 
  `Multivariable` subsection of `Critical Points Session`. 
* Similarly, add the hands on project related content wrt Hessian to 
  the `Critical Points Project`.

#### Cleanse

Review the created and updated content for brevity and clarity, namely:
* Confirm links and cross links exists
  * New session links added to `AGENDA`
  * New project links added to the corresponding 
    session sections.
  * Project descriptions added to corresponding
    README.md of the project folder.
* Remove stale links and corss links.
* De-duplicate content duplicated in multiple 
  places - instead add links in one of them.

## PR Tooling DRY + check_pr/merge_pr Reflected from ai_workbench
[x] Status

The companion repo `ai_workbench` (`../../../ai_workbench/`) had
already ported a consistent, DRY set of PR-management tooling from
`../ITDev` (bazel-based) into its own non-bazel, plain-`python3`
form: `check_pr.py`, `merge_pr.py`, a shared `_pr_utils.py`, and a
new `pr_merge_plugin` skill, alongside a refactor of its existing
`submit_pr.py`/`approve_pr.py`/`pr_submit_plugin.py` to use the
shared module. This repo (`la_workbench`) only had the older state
(`submit_pr.py`, `approve_pr.py`, `pr_submit_plugin.py`, each with
its own near-duplicate auth/permission and PR-status logic) — this
session propagates `ai_workbench`'s already-completed version here,
adapted for this repo's own bare-`python3` invocation convention and
its stricter 79-column line-length rule (see
`.agent/rules/always-line-length.md`, vs. `ai_workbench`/`ITDev`'s
80). Reference `ai_workbench`'s own `prompt_history.md` entries
"check_pr/merge_pr Migration Reflected from ITDev" and "PR Tooling
DRY + pr_merge_plugin Reflected from ITDev" for the full story
including the admin-bypass
discovery: `merge_pr.py` retries `gh pr merge` with `--admin` when a
review is required but the caller is `ADMIN` and branch protection
may exempt them — live-verified on `ai_workbench`'s own PRs #70/#71,
where `gh` refused to use a configured admin bypass unless `--admin`
was passed explicitly. `CHANGES_REQUESTED` always hard-blocks
regardless of permission, since that is an explicit human objection
rather than "no review yet."

* Added `_pr_utils.py` (shared `find_repo_root`,
  `check_auth_and_permission` — now returns the resolved permission
  string, `check_clean_branch`, `fetch_pr_status`, `_check_outcome`),
  `check_pr.py` (read-only mergeability report), and `merge_pr.py`
  (merges only after confirming checks/review, with the admin-bypass
  retry above).
* Refactored `submit_pr.py` and `approve_pr.py` to use
  `_pr_utils.check_clean_branch`/`check_auth_and_permission` and
  `_pr_utils.fetch_pr_status` respectively, dropping their own
  inline copies of that logic.
* Refactored `pr_submit_plugin.py`'s branch/tree hook to call
  `_pr_utils.check_clean_branch`, fixing the same latent bug
  `ai_workbench`/`ITDev` both had: `hook_check_branch_state` hardcoded
  `"main"` instead of respecting `--base`; it now takes a `base`
  parameter.
* Added `pr_merge_plugin.py` and its skill
  (`.claude/skills/pr_merge_plugin/`): a "wait for checks, then
  merge, then confirm" 3-step chain that deliberately never inspects
  `reviewDecision` itself, since `merge_pr.py` is the sole authority
  on whether an unsatisfied review blocks the merge or is
  admin-bypassable.
* Added `pr_tools_test.py` (35 hermetic tests) and
  `pr_merge_plugin_test.py` (12 hermetic tests) — `subprocess.run`
  and `fetch_pr_status` fully mocked, no real `git`/`gh` call ever
  made. No `pr_submit_plugin_test.py` existed here to update.

Validated via `py_compile` and `--help` on all five CLI entry points,
both hermetic test files reporting `OK`, and a line-length pass
(79 cols) on every new/changed file. No real GitHub pull request was
opened, approved, or merged during this session; committed and
pushed to this repo's own current branch, not `main`.

## Bazel Bootstrap + PR Tooling Reflected from aim
[x] Status

The user decided `la_workbench` should be treated exactly like the
sister repo `../aim` was: `aim` also started with no real service
code, but was deliberately bootstrapped with a full bazel scaffold
anyway (its own bootstrap commit says "treated identically to
ITDev (full parity), since aim will have real code soon"), and has
since been brought fully up to date with ITDev's DRY PR-tooling
work (check_pr/merge_pr, shared `_pr_utils.py`, `pr_merge_plugin`
skill, hermetic bazel-wired tests). This session propagates that
same "no real code yet, but full bazel scaffold + PR tooling
anyway" pattern here, superseding the bazel-free
plain-`python3` implementation this repo's own prior session entry
("PR Tooling DRY + check_pr/merge_pr Reflected from ai_workbench",
above) had added.

* Added the bazel scaffold: `.bazelversion` (9.2.0), `MODULE.bazel`
  / `WORKSPACE` (module name `la_workbench`), `.bazelignore`
  (excludes `.venv/` -- PyTorch's vendored `torchgen` package ships
  a real `BUILD.bazel` file deep inside `.venv/lib64/.../torchgen/
  packaged/autograd/`, which otherwise breaks `bazel build //...`
  with an invalid-label error; `aim` never hit this since it has no
  `.venv`). `.gitignore` gained `bazel-*`/`external/` (`.venv/` was
  already ignored).
* Added a stub `.github/workflows/pr-validation.yaml` (a placeholder
  `echo` step) so `//:pr_check` (wraps `act`) has something
  real-but-trivial to validate against -- this repo had no existing
  PR-validation workflow to conflict with.
* Ported `tools/scripts/build_utils/_container_checks.py` and
  `pr_check.py` verbatim from `aim` (`find_workspace_root` via
  `BUILD_WORKSPACE_DIRECTORY`, bazel-run-only).
* Replaced the entire bazel-free `tools/scripts/repo_utils/`
  PR-tooling set (`_pr_utils.py`'s own `find_repo_root()` bare path
  walk, same-directory `from _pr_utils import ...`) with `aim`'s
  bazel-based, package-qualified equivalents: `_pr_utils.py`,
  `check_pr.py`, `submit_pr.py`, `approve_pr.py`, `merge_pr.py`,
  `pr_submit_plugin.py` (2-command `bazel build //...` / `bazel
  test //...` stub -- no container-test commands, matching `aim`
  exactly since neither repo has `oci_image` targets yet),
  `pr_merge_plugin.py`, and their hermetic test files
  (`pr_merge_plugin_test.py`, `pr_tools_test.py`). Added
  `pr_submit_plugin_test.py`, which this repo never had.
* Added root `BUILD.bazel` (`pr_check`/`submit_pr`/`check_pr`/
  `approve_pr`/`merge_pr` `py_binary` targets) and `tools/BUILD.bazel`
  (`container_checks`/`pr_utils`/`pr_submit_plugin_lib`/
  `pr_merge_plugin_lib` `py_library` targets, three `py_test`
  targets, `exports_files`), mirroring `aim`'s target wiring exactly.
* Updated both `.claude/skills/pr_submit_plugin/skill.md` and
  `pr_merge_plugin/skill.md` from their bazel-free wording ("this
  repo has no bazel setup... .venv is unrelated") to `aim`'s
  bazel-based invocation style (`bazel run //:submit_pr -- ...`,
  `bazel run //:merge_pr -- ...`). The `.claude/skills/*/scripts/*.py`
  symlinks were already correct and untouched.

Validated: `bazel build //...` succeeds cleanly (first-ever bazel
build in this repo, after adding `.bazelignore`). All 8 explicit
targets (`check_pr`/`submit_pr`/`approve_pr`/`merge_pr`/`pr_check`/
`pr_submit_plugin_lib`/`pr_merge_plugin_lib`/`pr_utils`) build
cleanly. `bazel test //tools:pr_submit_plugin_test
//tools:pr_merge_plugin_test //tools:pr_tools_test` -- all 3 PASS.
`bazel run //:check_pr|//:submit_pr|//:approve_pr|//:merge_pr --
--help` all print usage cleanly. `bazel run //:pr_check` hit an
environment-level Docker/WSL gap (vsock/credential-store failure
under WSL2) -- not a bug in the ported code; `act` itself is
installed and correctly targeted the stub workflow.

This session was interrupted mid-flight (a Windows Docker Desktop
restart killed the parent process); resuming picked up cleanly at
the already-committed bazel scaffold (commit above), with only this
prompt_history.md entry itself left uncommitted. Re-validated
everything above from scratch after resuming -- `bazel build //...`,
the 8 explicit targets, all 3 test suites (PASS), and all 4
`--help` invocations -- with identical clean results. Re-tried
`bazel run //:pr_check` specifically because the Docker restart was
expected to have fixed the credential-socket gap: it did not --
`docker-credential-desktop.exe get` still fails with the same
`UtilAcceptVsock:271: accept4 failed 110` error, confirming this is
a persistent WSL2-vsock/Docker-Desktop integration gap rather than
something a Docker restart alone resolves. System-level Docker
config was left untouched, as fixing it is outside this repo's
scope. No line exceeds this repo's 79-column rule
(`.agent/rules/always-line-length.md`, same as `aim`'s). No real
GitHub pull request was opened, approved, or merged during this
session; committed and pushed to this repo's own current branch,
not `main`.

---

## Container-test stubs, consistency docs, slash-command wrappers
[x] Status

**Date:** 2026-08-30

**Prompt:** Same session as ITDev's own entry (see its
`specification_driven_development/prompt_history.md` for the full,
unparaphrased prompt text) -- container-test stub targets,
cross-repo consistency documentation, README PR-plugin sections,
three new `/pr_submit_plugin`/`/pr_approve_plugin`/`/pr_merge_plugin`
slash commands, and a branch-protection validation pass -- all done
directly in this repo by the same session (not delegated).

**What changed in this repo:**
- Added `tools/scripts/build_utils/container_tests_stub.py` and stub
  `//:container_tests`/`//:dockerfile_container_tests` `py_binary`
  targets (this repo has no real oci_image/Dockerfile targets yet),
  each printing a placeholder message and exiting 0, so
  `pr_submit_plugin.py`'s build+test chain now runs the same
  4-command sequence as ITDev instead of a 2-command stub.
  `pr_submit_plugin.py`/`pr_submit_plugin_test.py`/
  `pr_submit_plugin/skill.md` are now byte-identical to ITDev's
  copies (verified via `diff -q`); `pr_merge_plugin.py`/`skill.md`
  were left untouched.
- Added a generic "Sync note" to the module docstring of every
  PR-related script (`_pr_utils.py`, `submit_pr.py`, `check_pr.py`,
  `approve_pr.py`, `merge_pr.py`, `pr_submit_plugin.py`,
  `pr_merge_plugin.py`, `pr_check.py`), a "Cross-Repo Consistency"
  section to both skill.md files, and a matching comment above the
  PR-tools `BUILD.bazel` section, explaining this tooling is
  intentionally duplicated (not symlinked) across all 5 sister repos
  and must be kept in sync, with a `diff` spot-check example.
- Added/updated a "PR Workflow Plugins" README section covering
  `check_pr`/`submit_pr`/`approve_pr`/`merge_pr` with example usage.
- Fixed a pre-existing path bug in both skill.md files' "Run it via"
  example: it was missing the `.claude/` prefix
  (`skills/pr_submit_plugin/scripts/...` instead of
  `.claude/skills/pr_submit_plugin/scripts/...`), which would not
  have resolved from the repo root; repointed both to the verified
  `tools/scripts/repo_utils/<script>.py` path instead.
- Added three new slash commands, byte-identical across all 5 repos:
  `.claude/commands/pr_submit_plugin.md` (drafts a title/body from
  the branch's actual `git log`/`git diff` content, confirms with
  the user, then invokes `pr_submit_plugin.py` unchanged),
  `.claude/commands/pr_approve_plugin.md` (thin arg-parsing wrapper
  around `bazel run //:approve_pr`; relevant only to MAINTAIN/ADMIN,
  and fails on self-approval per `approve_pr.py`'s own guard), and
  `.claude/commands/pr_merge_plugin.md` (thin wrapper around
  `pr_merge_plugin.py`; relevant only when checks passed and either
  no review is required, the PR is `APPROVED`, or the caller is
  ADMIN with an exempting branch-protection admin bypass). Added
  matching "Or via `/pr_*_plugin`" cross-references to each
  underlying script's own docstring.
- Branch-protection validation (`gh api`) requested to confirm
  PR-only merges to `main`, `required_approving_review_count` 0 for
  private / 1 for public, and admin bypass everywhere -- findings
  logged centrally in ITDev's own prompt_history.md entry (this
  repo's specific result: see that entry for the private-vs-public,
  Free-plan-vs-Pro breakdown covering all 5 repos).
- Re-ran `bazel build //...` / `bazel test //...` (green) and
  `bazel run //:container_tests` / `//:dockerfile_container_tests`
  (both print the stub message and exit 0) in this repo.

---

---

## act --reuse: durable fix for the container-cleanup timeout
[x] Status

**Date:** 2026-08-30

**Prompt:** Follow-on to the entry above. Full details, including
the diagnostic trail (act upgrade, credential-helper removal, and
why the reboot fixed some symptoms but not this one), are in ITDev's
own `specification_driven_development/prompt_history.md` entry of
the same title -- not re-explained here. Summary: after a full
reboot didn't clear a recurring `act` post-job container-cleanup
timeout, the fix was `act`'s own `--reuse` flag, applied identically
to this repo per: "Yes: please reuse. Don't just use in ITDev but in
the spirit of consistency across all repos, let us duplicate this
across all sister repos," plus "Document at appropriate places the
periodic use of `docker container prune` to ensure we reclaim."

**What changed in this repo:**
- Added `--reuse` to the `act` invocation in
  `tools/scripts/build_utils/pr_check.py`, with the same inline
  comment ITDev's copy carries explaining why (a vsock-forwarded
  `docker.sock` on Docker Desktop's WSL2 backend can exceed `act`'s
  internal context deadline during post-success container removal,
  even though the job itself passed).
- Documented the accompanying `docker container prune` maintenance
  note in this repo's README, in its "PR Workflow Plugins" section.
- `bazel build //...` verified green after the change.

---

---

## Local .pr_check_skip marker for sister repos
[x] Status

**Date:** 2026-08-30

**Prompt:** "Add the .pr_check_skip marker-file approach to all
sister-repos except ITDev. Then I will manually do the PR submit and
follow on commands to approve the merger."

**What changed in this repo:**
- Added a local, git-ignored `.pr_check_skip` marker-file check to
  the top of `pr_check.py`'s `main()`: if the file exists at the
  repo root, print a message and exit 0 immediately, without ever
  invoking `act`/Docker. Toggle with `touch .pr_check_skip` /
  `rm .pr_check_skip`.
- Deliberately NOT applied to ITDev's `pr_check.py` -- its CI gate
  must never be skippable, since it validates real service code.
  This is an intentional, narrow, explicitly-commented divergence
  from ITDev's copy of `pr_check.py` (both copies otherwise stay
  byte-identical to each other, per the usual sync-note discipline).
- Added `.pr_check_skip` to `.gitignore`.
- Documented the toggle in this repo's README, next to the existing
  `docker container prune` note.
- Verified: `touch .pr_check_skip && bazel run //:pr_check` prints
  the skip message and exits 0 with no Docker call; removing the
  marker restores normal behavior. `bazel build //...` green.

---

---

## Rename PR slash commands, add /check_pr and /check_prs
[x] Status

**Date:** 2026-08-30

**Prompt:** Same session as ITDev's own entry of the same title --
full prompt text and the scope-clarification exchange are recorded
there, not repeated here. Summary: rename
`/pr_submit_plugin`/`/pr_approve_plugin`/`/pr_merge_plugin` to
`/pr_submit`/`/pr_approve`/`/pr_merge`, add new `/check_pr <PR#>`
and `/check_prs` commands, applied identically to all 5 repos
(confirmed to include ITDev, not just the 4 sister repos).

**What changed in this repo:**
- Renamed `.claude/commands/pr_submit_plugin.md` → `pr_submit.md`,
  `pr_approve_plugin.md` → `pr_approve.md`, `pr_merge_plugin.md` →
  `pr_merge.md` (content updated: new invocation line, new
  self-referential sync-note path). The underlying skill/script
  names are unchanged -- only the slash-command layer was renamed.
- Added `.claude/commands/check_pr.md` (`/check_pr <PR#>`, a trivial
  wrapper around `bazel run //:check_pr`) and `check_prs.md`
  (`/check_prs`, lists every open PR with a per-PR check/review
  status summary -- no underlying script needed).
- Updated every cross-reference to the old command names: the four
  `.py` scripts' docstrings, both skill.md files, `BUILD.bazel`'s
  sync-note comment, and README's "Preferred entry points"
  paragraph.
- `bazel build //...` / `bazel test //...` verified green after the
  rename.

---

---

## Use bare python3, not .venv/bin/python3, in PR commands
[x] Status

**Date:** 2026-08-30

**Prompt:** Same session as ITDev's own entry of the same title --
full prompt text and the discovered bug are recorded there, not
repeated here. Summary: `pr_submit_plugin.py`'s docstring had picked
up `.venv/bin/python3` in this repo (which has no `.venv`) when it
was copied byte-identical from ITDev during the earlier
"container-test stubs" work; switched every PR-command reference to
bare `python3`, everywhere, and added a `python3`-availability guard
to `/pr_submit` and `/pr_merge`'s invocation snippets.

**What changed in this repo:**
- Switched every occurrence of `.venv/bin/python3` to bare `python3`
  in `.claude/commands/pr_submit.md`, `pr_merge.md`, both skill.md
  files, and `pr_submit_plugin.py`'s docstring (`pr_merge_plugin.py`
  here already used bare `python3` correctly, so it needed no
  change).
- Added a `command -v python3` availability guard directly in the
  invocation snippet shown by `/pr_submit` and `/pr_merge` -- prints
  a warning to stderr and exits 1 before attempting the real
  invocation if `python3` isn't on PATH.
- Verified: `bazel test //tools:pr_submit_plugin_test
  //tools:pr_merge_plugin_test //tools:pr_tools_test` green;
  smoke-tested `python3 tools/scripts/repo_utils/
  pr_submit_plugin.py --help` directly (this repo has no `.venv`) to
  confirm the bare invocation resolves and runs.

---

---

## Extend .pr_check_skip to ITDev too
[x] Status

**Date:** 2026-08-31

**Prompt:** Same session as ITDev's own entry of the same title --
full prompt text is recorded there, not repeated here. Summary: the
earlier decision to exclude ITDev from `.pr_check_skip` was
reversed once it became clear the marker only ever skips the local
`act` pre-push simulation, never the real GitHub Actions CI (which
still runs `pr-validation.yaml` on every actual push/PR regardless)
-- so the original "ITDev's gate must never be skippable" concern
didn't actually apply.

**What changed in this repo:**
- Updated the explanatory comment in `pr_check.py` (it previously
  claimed ITDev was permanently excluded from this mechanism) to
  instead clarify what's actually true: this only ever skips the
  local `act` simulation, never real CI.
- Updated this repo's README note to drop the now-false "ITDev has
  no such skip" claim -- all 5 repos support the marker the same
  way now.
- `bazel test //tools:pr_submit_plugin_test
  //tools:pr_merge_plugin_test //tools:pr_tools_test` green after
  the change.

---

---

## Rename /check_pr, /check_prs to /pr_check, /pr_checks
[x] Status

**Date:** 2026-08-31

**Prompt:** Same session as ITDev's own entry of the same title --
full prompt text and the naming-collision finding are recorded
there, not repeated here. Summary: `/check_pr`/`/check_prs` renamed
to `/pr_check`/`/pr_checks` to match `/pr_submit`/`/pr_approve`/
`/pr_merge`'s word order; `check_pr.py`/`//:check_pr` themselves
left unchanged, since renaming them would collide with the
unrelated, pre-existing `//:pr_check` (act/CI validator) target.

**What changed in this repo:**
- Renamed `.claude/commands/check_pr.md` → `pr_check.md`,
  `check_prs.md` → `pr_checks.md`, with an explicit disambiguation
  note added: `/pr_check` wraps `//:check_pr`, not the unrelated
  `//:pr_check` act/CI validator.
- `tools/scripts/repo_utils/check_pr.py` and `//:check_pr` left
  untouched -- already consistent with `approve_pr.py`/
  `merge_pr.py`/`submit_pr.py`'s "verb_pr" ordering, and renaming
  it would have collided with `//:pr_check`.
- Updated `BUILD.bazel`'s slash-command comment and README's
  "Preferred entry points" paragraph to match.
- `bazel build //...` verified green after the change.

---

---

## Rename pr_check (act validator) to act_check
[x] Status

**Date:** 2026-08-31

**Prompt:** Same session as ITDev's own entry of the same title --
full prompt text and rationale are recorded there, not repeated
here. Summary: the act-based local CI validator was renamed
throughout to `act_check` (from `pr_check`) to eliminate the
cognitive load of remembering it's a different thing from
`check_pr` (the `gh`-based single-PR-status script), rather than
just documenting the distinction.

**What changed in this repo:**
- `tools/scripts/build_utils/pr_check.py` → `act_check.py`,
  `//:pr_check` → `//:act_check`, `.pr_check_skip` →
  `.act_check_skip` (including this repo's own marker file, if
  present).
- `skill_pr_check`/`SkillPrCheckTest` in `pr_submit_plugin.py`/its
  test → `skill_act_check`/`SkillActCheckTest`.
- Updated every reference: `BUILD.bazel`, `tools/BUILD.bazel`,
  `pr_submit_plugin.py` (and its test), `pr_submit_plugin/skill.md`,
  `/pr_submit`'s and `/pr_check`'s own docs (the latter's "not to be
  confused with" caveat simplified away -- the collision it warned
  about no longer exists), `.gitignore`, and README.
- `/pr_check` (the slash command, wrapping `//:check_pr`) was left
  completely untouched throughout -- only the previously-colliding
  `//:pr_check` (act validator) target was renamed.
- `bazel build //...` and the three PR-tooling tests verified green;
  `//:act_check` and `//:check_pr` confirmed to build/run
  independently with no collision; `.act_check_skip` marker
  mechanism re-verified working.

---
