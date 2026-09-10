# Bootstrap a repository-native agent orchestration workbench

This ExecPlan is a living document governed by `.agent/PLANS.md`.

## Purpose / Big Picture

Create an inspectable public repository showing how Omar plans, delegates, reviews, and hands off agent-assisted engineering work. A reviewer can understand the workflow from the README, inspect each role and slash workflow, and run one local audit that detects missing or malformed configuration.

## Scope and exclusions

In scope are shared instructions, Claude-specific routing, specialist subagents, reusable skills, planning rules, templates, an honest bootstrap record, and a static configuration audit. This plan does not claim historical daily usage, install Claude Code, enable experimental teams, operate on another repository, or publish to GitHub without explicit approval.

## Context and repository map

Claude Code loads `CLAUDE.md`; that file imports the tool-neutral `AGENTS.md`. Task procedures live under `.claude/skills/`, reusable roles under `.claude/agents/`, and living plans under `plans/`. `.agent/PLANS.md` defines what makes a plan resumable and verifiable.

## Progress

- [x] (2026-09-11 00:00Z) Audited current official documentation for project memory, skills, subagents, agent teams, AGENTS.md, and ExecPlans.
- [x] (2026-09-11 00:00Z) Defined shared instructions and Claude-specific routing without duplicating the source of truth.
- [x] (2026-09-11 00:00Z) Added bounded explorer, architect, implementer, reviewer, and verifier roles.
- [x] (2026-09-11 00:00Z) Added plan, orchestration, review, handoff, and ship workflows as current skills.
- [x] (2026-09-11 00:00Z) Added templates, evidence policy, and this bootstrap record.
- [x] (2026-09-11 00:00Z) Ran `python3 scripts/audit_config.py`; observed `configuration audit passed: 6 agents, 5 skills`.
- [x] (2026-09-11 00:00Z) Reviewed the full repository structure, frontmatter, claims, and publication boundary; no blocking finding remained.
- [ ] Obtain human approval before creating and pushing the GitHub repository.

## Surprises & Discoveries

Claude Code does not natively load `AGENTS.md`; the supported interoperability pattern is importing it from `CLAUDE.md` with `@AGENTS.md`. Custom commands have been merged into skills, while `.claude/commands/` remains a legacy-compatible path. Claude's agent-team runtime files are generated under the user's home directory and should not be pre-authored or committed.

## Decision Log

- **2026-09-11, agent with human direction:** Use project skills instead of legacy command files because both create slash workflows and skills are the current recommended structure.
- **2026-09-11, agent with human direction:** Build a dedicated operational repository in addition to project-specific instructions.
- **2026-09-11, agent:** Do not fabricate historical transcripts or “daily use” evidence. Record this bootstrap as the first truthful artifact.
- **2026-09-11, agent:** Keep experimental agent teams opt-in; make focused subagents the default.

## Milestones

The first milestone creates the instruction hierarchy and planning contract. It is observable when `CLAUDE.md` imports `AGENTS.md` and the latter points substantial work to `.agent/PLANS.md`.

The second milestone creates bounded specialist roles and user-invoked workflows. It is observable by inspecting unique YAML frontmatter names and the `/plan`, `/orchestrate`, `/review`, `/handoff`, and `/ship` skill directories.

The third milestone adds durable task artifacts and a static audit. It is complete when the audit exits successfully and the review/handoff state only observed evidence.

## Concrete steps

Create the repository files named above. Run the local audit. Inspect `git diff --check` and the complete staged diff. Update Progress and Outcomes. After explicit approval, create the remote repository, push a feature branch or main as directed, and link the commit from the application material.

## Validation and acceptance

Run `python3 scripts/audit_config.py`; it must report every required agent and skill and exit zero. Run `git diff --check`; it must emit no errors. Inspect the repository tree and confirm no `.env`, key, token, generated Claude team state, or fabricated transcript is present.

## Safety and recovery

All changes are additive in a new local repository. Publishing is a separate external action requiring approval. Before publication, files can be revised without affecting existing projects.

## Outcomes & Retrospective

The local repository now has one shared instruction source, Claude-specific routing, six bounded specialists, five user-invoked workflows, a living-plan contract, reusable task artifacts, and a passing static audit. The review found no secret material, fabricated runtime transcript, legacy command duplication, or unsupported claim of historical use. Claude Code runtime invocation remains unobserved because the CLI is not installed. Publication remains pending human approval and GitHub authentication.
