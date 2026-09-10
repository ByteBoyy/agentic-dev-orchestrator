---
name: review
description: Run an independent review of current changes against the task contract and ExecPlan.
argument-hint: <plan-path-or-diff-scope>
context: fork
agent: code-reviewer
disable-model-invocation: true
---

Review `$ARGUMENTS`. If it is a plan, compare the working diff with its purpose, scope, exclusions, and acceptance. Return blocking findings first, then non-blocking suggestions, then missing evidence. Do not edit files.
