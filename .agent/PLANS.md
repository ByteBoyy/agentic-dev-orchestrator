# Execution Plans

An ExecPlan is a self-contained, living specification that lets a contributor deliver observable behavior without relying on chat history.

## When required

Create one for multi-step or multi-file changes, new features, refactors, material risk, unclear architecture, or work expected to take more than about an hour. A typo or narrowly obvious edit does not need one.

## Required qualities

- Start with the user-visible purpose and how to observe success.
- Define repository-specific terms and identify exact files and entry points.
- State scope, exclusions, dependencies, risks, and assumptions.
- Divide work into independently verifiable milestones.
- Give exact acceptance commands and expected observable results.
- Stay usable by someone with only the working tree and this plan.
- Record changes in direction and the reason for each decision.

## Living sections

Every ExecPlan must maintain these sections:

- `Progress`: timestamped checkboxes for completed and remaining work.
- `Surprises & Discoveries`: unexpected facts with concise evidence.
- `Decision Log`: decisions, rationale, date, and owner.
- `Outcomes & Retrospective`: achieved behavior, remaining gaps, and lessons.

## Execution

The implementer proceeds milestone by milestone after approval. Update the plan at every stopping point. If scope changes, revise the plan before continuing. A plan is complete only when its acceptance behavior is observed or the unmet condition is clearly recorded.

## Skeleton

```markdown
# <Action-oriented title>

This ExecPlan is a living document governed by `.agent/PLANS.md`.

## Purpose / Big Picture

## Scope and exclusions

## Context and repository map

## Progress

- [ ] (YYYY-MM-DD HH:MMZ) Work item.

## Surprises & Discoveries

## Decision Log

## Milestones

## Concrete steps

## Validation and acceptance

## Safety and recovery

## Outcomes & Retrospective
```
