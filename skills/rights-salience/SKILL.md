---
name: rights-salience
description: Salience, severity and evidence for institutional sustainable-finance research; return evidence-linked findings, assumptions, gaps and reviewable outputs.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Salience, severity and evidence

Read `../../AGENTS.md` and `../../prompts/stages/salience.md` relative to this skill directory. Obtain the current stage packet using the repository CLI. Do not create or claim unavailable source access.

## Task
Prioritise risks to people by scale, scope and difficulty of remedy; keep evidence confidence separate from severity. Distinguish cause, contribution and direct linkage without pretending the software determines legal liability. Preserve denials, responses and source conflicts.

## Deliverable
Return the fields in `../../schemas/artifact.schema.json`; use the current run ID and input digest. Required sections: scale_scope_irremediability, actual_vs_potential, relationship_to_harm, allegations_and_responses. Include source IDs, scope, periods, methods and material gaps. Call only allowlisted calculations with explicit provenance; missing evidence means NEEDS_DATA, not invented values.

## Limit
Risks to people are not reduced to monetary loss or a supplier-spend score. Allegations, company responses and adjudicated findings remain distinct. No personal victim data should be published in public repositories.
