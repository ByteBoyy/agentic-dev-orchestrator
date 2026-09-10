# Operating model

## Roles are boundaries, not personas

The specialist definitions limit context, tools, and responsibility. The explorer and architect cannot edit. The reviewer cannot approve its own implementation. Implementers receive exclusive files when they work concurrently. The verifier reports evidence but does not reinterpret requirements.

## Choosing the execution shape

Use the main session for a small sequential change. Use one subagent when investigation would flood the main context or a repeatable specialist can return a compact result. Use several subagents for independent work that the lead integrates. Use an experimental agent team only when workers genuinely need a shared task list and direct communication.

Do not parallelize tasks that touch the same files. Worktree isolation prevents accidental overlap in the main checkout, but it does not resolve semantic conflicts.

## Approval gates

The human approves material scope and architecture, external side effects, destructive actions, and shipping. The lead may coordinate accepted work but cannot silently convert a documentation task into an implementation or a local change into a deployment.

## Evidence chain

Each substantial change has a task brief and ExecPlan. The living plan records discoveries and decisions. Review produces severity-ranked findings. Verification lists exact commands and results. Handoff names remaining risk. Git commits and pull requests link these artifacts into a durable history.
