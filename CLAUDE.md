@AGENTS.md

# Claude Code routing

Keep this file concise because it is loaded every session. Procedures live in skills and specialist prompts live in `.claude/agents/`.

## Workflow

- Use `/plan` when the task requires an ExecPlan.
- Use `/orchestrate` only after the plan is accepted.
- Use `/review` in a separate read-only context after implementation.
- Use `/handoff` to preserve evidence and remaining work.
- Use `/ship` only when the human asks to prepare or perform a repository action.

## Agent selection

Delegate discovery to `explorer`, design to `architect`, scoped implementation to the relevant implementer, review to `code-reviewer`, and acceptance checks to `verifier`. Do not spawn a team for sequential work or overlapping file ownership.

Do not create or edit Claude's runtime team files. Claude Code owns `~/.claude/teams/` and `~/.claude/tasks/`.
