# Salience, severity and evidence

## Decision context
Who may be harmed across the value chain, how severe is the risk, and what prevention, remedy and investment responses are evidenced?

## Assignment
Prioritise risks to people by scale, scope and difficulty of remedy; keep evidence confidence separate from severity. Distinguish cause, contribution and direct linkage without pretending the software determines legal liability. Preserve denials, responses and source conflicts.

## Required output sections
- `scale_scope_irremediability`: substantive analysis linked to claim IDs.
- `actual_vs_potential`: substantive analysis linked to claim IDs.
- `relationship_to_harm`: substantive analysis linked to claim IDs.
- `allegations_and_responses`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use UNGP with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
Risks to people are not reduced to monetary loss or a supplier-spend score. Allegations, company responses and adjudicated findings remain distinct. No personal victim data should be published in public repositories.
