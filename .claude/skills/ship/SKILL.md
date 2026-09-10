---
name: ship
description: Prepare a truthful commit or pull-request handoff after review and verification; external actions require human approval.
argument-hint: <plan-path>
disable-model-invocation: true
---

Read `$ARGUMENTS`, the current diff, review findings, and verification record. Refuse to proceed while blocking findings or required failed checks remain. Inspect for secrets and scope drift. Draft a commit and pull-request summary with outcome, design, verification, remaining risk, and rollback. Do not commit, push, open a PR, merge, deploy, or publish unless the human explicitly requests that exact action.
