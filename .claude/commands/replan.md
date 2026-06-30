# SDW Replan Skill

Execute the full Specification Driven Workbench (SDW) replan
cycle — orient, generate, approve, execute, commit.

`SDW_DIR` below means
`miscellaneous/software_defined_workbench`.

## Invocation

```
/replan [section-name]
```

- **No argument:** scan `SDW_DIR/prompt_history.md` for the last
  `## <Title>` heading whose immediately following line is
  `[ ] Status` (the most recently added unprocessed section).
- **With argument** (e.g. `/replan Skillify`): target the
  section whose `##` heading contains `$ARGUMENTS`, regardless
  of its `[ ]` / `[x]` state.

## Steps

### 1. Orient

Before reading any file, call the `EnterPlanMode` tool so
that phase-step generation and approval happen in plan mode.

Read these files in order:

1. `CLAUDE.md` — operating protocol and step template.
2. `SDW_DIR/plan.md` — scan all `## Phase N` headings; the new
   phase is the highest N found + 1.
3. `SDW_DIR/prompt_history.md`:
   - **No argument:** find the last `## <Title>` heading whose
     immediately following line is `[ ] Status`.
   - **With argument:** find the section whose heading contains
     `$ARGUMENTS`.
   Note the section title and its line range.

State before proceeding:
```
Target section : ## <title> (lines X–Y of prompt_history.md)
New phase      : Phase N+1
```

### 2. Generate Phase Steps

For each distinct deliverable in the target section, produce one
step using the format defined in `.claude/commands/plan-step.md`.
Apply the plan-step self-check to every step before writing it.

The **final step** of every phase must be a "Mark complete" step
that:
- Flips every `[ ] Status` → `[x] Status` in the Phase N+1
  block of `SDW_DIR/plan.md` (all steps should already be
  appended from Step 3 — only the status lines change here).
- Commits all changed files and tags
  `vN+1.K-<brief-summary>-step-completed`.

Note: `SDW_DIR/prompt_history.md` `[ ] Status` was already
changed to `[x] Status` and committed right after plan approval
(Step 3).

### 3. Present for Approval

Output the full Phase N+1 block as readable markdown.
Do **not** write any file yet.

End with:
```
Proposed Phase N+1 — awaiting approval.
Reply "Approve" to execute step by step.
```

### 3a. On Approval — Commit Plan Immediately

**Immediately after the user approves**, before executing any step:

1. Change `[ ] Status` → `[x] Status` on the line after
   `## <title>` in `SDW_DIR/prompt_history.md`.
2. Append the full Phase N+1 block to `SDW_DIR/plan.md`. Each
   step in the block must follow the plan-step template exactly
   — including its `[ ] Status` line — using a condensed
   (one-paragraph) body per field rather than multi-line.
3. Commit both files together:
   ```bash
   git add SDW_DIR/plan.md SDW_DIR/prompt_history.md
   git commit -m "chore: Phase N+1 - append plan + mark prompt complete"
   ```

This ensures `SDW_DIR/plan.md` always reflects the approved plan
and `SDW_DIR/prompt_history.md` is committed with the prompt
that drove the plan, regardless of how many steps are executed.

### 4. Execute (after approval)

Execute one step per turn following CLAUDE.md §One Step at a Time:

1. Make only the changes described in the current step.
2. Run the VERIFY command; confirm it passes.
3. Flip the step's `[ ] Status` → `[x] Status` in
   `SDW_DIR/plan.md`.
4. Commit the step changes AND the plan.md status update together
   per CLAUDE.md §Commit Protocol.
5. Wait for explicit approval before the next step.

### 5. Final Step — Mark All Complete

The final "Mark complete" step:
1. Confirms all `[ ] Status` lines in Phase N+1 of
   `SDW_DIR/plan.md` are already `[x] Status` (flipped per-step
   during execution).
2. Tags `vN+1.K-<brief-summary>-step-completed` and pushes.

After the final step, run the verification suite:
```bash
# All Phase N+1 steps marked complete
grep -A1 "### Step N+1\." SDW_DIR/plan.md | grep "\[ \] Status"
# → 0 matches

# prompt_history.md section already marked complete
grep -A1 "^## <title>" SDW_DIR/prompt_history.md | grep "\[x\] Status"
# → 1 match

# Tag pushed
git tag | grep "v<N+1>\."
```
