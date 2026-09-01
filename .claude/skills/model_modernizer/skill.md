---
name: model_modernizer
description: >
  Reports the model currently running this session, checks it
  against the latest available Claude models, and explains the two
  modes /replan and /execute actually use today (Plan Mode vs.
  normal mode) -- but never switches, pins, or unpins a model
  itself. Use when explicitly asked to check, review, or modernize
  which model this repo's skills use.
disable-model-invocation: true
triggers:
  - "check the model"
  - "modernize the model"
  - "which model"
  - "upgrade the model"
  - "model_modernizer"
_path: .claude/skills/model_modernizer/skill.md
---

# Model Modernizer

## Overview

**The real planning/execution differentiator today is Plan Mode, not
model tier.** `/replan` calls `EnterPlanMode` (per its own Step 1),
which is a workflow/tool-restriction mode enforced by the harness:
read-only tools plus plan-file edits only, forced exploration, a
written plan, and an explicit `ExitPlanMode` approval gate before any
change happens. `/execute` runs with none of that — normal tools, one
step at a time, no separate approve-the-approach phase. That is a
real, enforced difference in *process rigor* between the two
commands.

What this is **not**: a confirmed model-tier switch. Plan Mode's own
workflow suggests delegating to "Explore" and "Plan" subagent types
via the `Agent` tool, and those subagent types could in principle run
on a different model per their own definitions — but this skill has
no visibility into whether they actually do, and in practice that
delegation is often skipped when the person driving `/replan` already
has enough context. When skipped, `/replan` and `/execute` run on the
exact same model, in the exact same session — the only difference is
which workflow (Plan Mode vs. normal) is active.

**Decision: leave model-tier selection alone for now.** This repo has
no per-skill model-pinning config (no `model` field in
`.claude/settings.json` or `.claude/settings.local.json`, and no
`.claude/commands/*.md` passes an explicit `model` override to the
`Agent` tool), and that is deliberate, not an oversight. Actually
differentiating models would require either manual `/model` switching
around every `/replan`/`/execute` pair (unreliable — nothing enforces
it and it's easy to forget) or restructuring `/replan`/`/plan-step`
into real subagent definitions with pinned models (genuine
engineering effort, resting on undocumented platform internals that
could shift). Plan Mode's enforced rigor is already doing the real
work; the incremental benefit of a model-tier split is speculative
while the cost is concrete. Revisit only if a specific, observed
problem (not a hypothetical one) shows up that Plan Mode's workflow
rigor doesn't address.

## Execution Steps

1. **Report current state.**
   - State the model currently running this session (self-identify
     from the system prompt).
   - State plainly: `/replan` runs in Plan Mode (workflow/tool
     restriction, not a confirmed model change); `/execute` runs in
     normal mode; both use whatever model is active for the session
     unless the operator manually ran `/model` in between.
   - Check `.claude/settings.json` and `.claude/settings.local.json`
     for a `model` field; report it if present, or "not pinned —
     uses the CLI/session default" if absent.
   - Check whether any `.claude/commands/*.md` or subagent
     definition passes an explicit `model` override to the `Agent`
     tool; report any found.

2. **Compare against the latest models.**
   List the latest known Claude model family with a one-line
   capability/cost note for each. Do not hardcode a stale list
   blindly — if the model landscape may have moved on since this
   skill was last updated, say so explicitly rather than presenting
   possibly-outdated names as current.

3. **Propose, do not apply.**
   If a newer model family is available, note it as an option. Do
   **not** propose a planning-model/execution-model pairing as if it
   were an existing, enforceable split — it is not, per the Overview
   above. The default recommendation, absent a concrete observed
   problem, is: no change needed, keep relying on Plan Mode's
   workflow rigor for the planning/execution distinction.

4. **Confirm before any change.**
   If the user wants to act anyway, ask explicitly which of these
   they want:
   - (a) Pin a model by writing a `model` field into
     `.claude/settings.json` (create the file if needed).
   - (b) Just be told the `/model <name>` command to run themselves
     (no file written).
   - (c) Do nothing — this was informational only.
   Only write to `.claude/settings.json` if the user picks (a) and
   confirms. Never edit any config as part of Steps 1–3.

## Constraints
- Never silently switch, pin, or unpin a model.
- Never invoke automatically — this is a human-invoked check, not
  something that runs as part of `/replan`'s or `/execute`'s own
  flow.
- Never present the Plan-Mode-vs-normal-mode split as if it were a
  model-tier split — they are different mechanisms, and only the
  former is confirmed to be in effect today.
