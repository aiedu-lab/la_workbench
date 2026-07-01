# SDW Execute Skill

Execute the next pending step of the current SDW plan phase,
then wait for human approval before continuing.

`SDW_DIR` means `miscellaneous/software_defined_workbench`.

## Invocation

```
/execute
```

No arguments. Reads the active phase and next pending step from
`SDW_DIR/plan.md`.

## Steps

### 4. Orient and Execute

Read `SDW_DIR/plan.md`:
- Identify the highest `## Phase N` block
- Within that block, find the first step whose status is
  `[ ] Status` (not yet executed). 
- Read that step's CONTEXT, ACTION, CONSTRAINTS, OUTPUT, and
  VERIFY fields in full.

State before proceeding:

```
Current phase : Phase N
Executing     : Step N.K — <step name>
```

Perform only the changes described in the step's ACTION field.
Respect all CONSTRAINTS.

Run the VERIFY command. If it fails, fix the issue before
committing. Confirm the expected result is produced.

Then:

1. Flip the step's `[ ] Status` → `[x] Status` in
   `SDW_DIR/plan.md`.
2. Stage the step's changed files and `SDW_DIR/plan.md`.
3. Commit:
   ```
   <type>: Phase N: Step K - <summary>
   ```
4. Show the diff and **stop**. Wait for explicit human approval
   before the next step.

### 5. Final Step — Mark All Complete

If the step just executed is the final "Mark complete" step:

1. Confirm all `[ ] Status` lines in the phase are `[x] Status`.
2. Tag:
   ```bash
   git tag -a vN.K-<brief-summary>-step-completed \
       -m "Completed Phase N Step K: <summary>"
   ```
3. Push branch and tags:
   ```bash
   git push origin <branch> --tags
   ```

Run the verification suite:

```bash
# All steps in the phase marked complete
grep -A2 "### Step N\." SDW_DIR/plan.md | grep "\[ \] Status"
# → 0 matches

# Tag pushed
git tag | grep "v<N>\."
```
