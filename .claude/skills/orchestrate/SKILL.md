---
name: orchestrate
description: Execute an approved ExecPlan through bounded specialist delegation and integration.
argument-hint: <path-to-approved-plan>
disable-model-invocation: true
---

Read `$ARGUMENTS` and confirm it follows `.agent/PLANS.md` and records approval. Build a task graph from its milestones. Delegate only independent tasks concurrently and give every implementer exclusive file ownership. Keep dependent or overlapping tasks sequential. Integrate returned work, update the plan's living sections, and stop before any push, merge, deploy, or unapproved scope change.
