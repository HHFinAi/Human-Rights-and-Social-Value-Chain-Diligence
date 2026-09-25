# Operational economics and financial transmission

## Decision context
Who may be harmed across the value chain, how severe is the risk, and what prevention, remedy and investment responses are evidenced?

## Assignment
Quantify transparent wage-gap, disruption or remedial-cost scenarios with dates, populations and currency. Do not use the arithmetic to justify a rights violation or equate compensation with full remedy. Keep risk-to-people conclusions separate from investor economics.

## Required output sections
- `wage_gap_scenario`: substantive analysis linked to claim IDs.
- `supply_disruption`: substantive analysis linked to claim IDs.
- `litigation_and_contracts`: substantive analysis linked to claim IDs.
- `separate_people_risk`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use IFRS-S1, UNGP with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
Risks to people are not reduced to monetary loss or a supplier-spend score. Allegations, company responses and adjudicated findings remain distinct. No personal victim data should be published in public repositories.

A domain calculation must pass recomputation. The minimal runnable illustration is `wage_gap_cost`; other needed specialist models must remain explicitly external and independently reviewed.
