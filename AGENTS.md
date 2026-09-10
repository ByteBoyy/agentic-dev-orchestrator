# Repository operating instructions

## Purpose

This repository defines a portable, auditable workflow for agent-assisted software delivery. Prefer concrete artifacts and observable outcomes over claims about autonomy.

## Source of truth

- `AGENTS.md` contains rules that apply to every coding agent.
- `CLAUDE.md` imports this file and adds Claude-specific routing.
- `.agent/PLANS.md` defines living execution plans.
- `.claude/skills/` contains on-demand procedures.
- `.claude/agents/` contains reusable specialist roles.
- `plans/` and `examples/` contain task evidence.

## Required workflow

1. Convert the request into a task contract: outcome, scope, exclusions, acceptance, and risks.
2. For multi-file, risky, ambiguous, or longer-than-one-hour work, create an ExecPlan following `.agent/PLANS.md`.
3. Obtain human approval before widening scope, changing architecture, or causing an external side effect.
4. Delegate only concrete, bounded work. Give each worker exclusive file ownership when agents run concurrently.
5. Keep implementation and review separate. A worker does not approve its own work.
6. Record commands actually run and their results. Mark unavailable checks as not run.
7. The human owns the final commit, push, merge, deploy, and release decision.

## Delegation policy

- Use `explorer` for high-volume read-only discovery.
- Use `architect` for plans and trade-offs; it never edits implementation files.
- Use `backend-implementer` and `frontend-implementer` only after plan approval.
- Use `code-reviewer` after integration; it is read-only and lists blocking findings first.
- Use `verifier` to run the exact acceptance commands declared by the plan.
- Parallelize only independent work. If two agents need the same file, sequence them.

## Integrity rules

- Never fabricate a transcript, agent run, commit, review, benchmark, or test result.
- Never backdate work or imply this workflow was used before it existed.
- Do not add decorative agents, skills, or plans without an actual trigger and output contract.
- Do not expose credentials, personal data, `.env` contents, or private URLs.
- Instructions are guidance, not enforcement. Use permissions, sandboxing, hooks, and human review for hard controls.

## ExecPlans

Use an ExecPlan for substantial work, following `.agent/PLANS.md` from design through outcome. Keep Progress, Surprises & Discoveries, Decision Log, and Outcomes & Retrospective current.
