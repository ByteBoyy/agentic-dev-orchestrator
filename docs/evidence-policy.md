# Evidence policy

## Allowed claims

A claim is supported when it points to code, a committed instruction, an observed command result, a review artifact, a pull request, a deployment, or another inspectable source.

## Disallowed claims

- Backdated or reconstructed transcripts presented as original runs
- “Daily use” inferred from adding configuration files
- Tests marked passed because code appears correct
- External integrations described as verified without an observed credentialed run
- Agent output presented as independent review when the same context implemented the change

## Recording agent work

Capture the task given, agent or role used, returned decision or artifact, human correction, resulting change, and observed verification. Summaries are acceptable; fabricated verbatim conversations are not.

The first plan in this repository states clearly that the configuration was created during a repository-hardening task. It does not imply that earlier projects used this exact workflow.
