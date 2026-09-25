# Investment committee and accountable review

## Decision context
Who may be harmed across the value chain, how severe is the risk, and what prevention, remedy and investment responses are evidenced?

## Assignment
Integrate findings without changing their qualification. Separate facts, inferences, assumptions and calculations; cite evidence IDs and dates. Preserve unknown conclusions. Complete the domain-assessment declarations, register unresolved material issues, and submit for human research review. Do not certify legal compliance or investment performance.

## Required output sections
- `investment_question_and_answer`: substantive analysis linked to claim IDs.
- `financial_vs_sustainability_conclusions`: substantive analysis linked to claim IDs.
- `evidence_and_calculations`: substantive analysis linked to claim IDs.
- `decision_conditions_and_limits`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use the mandate and registered primary evidence with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
Risks to people are not reduced to monetary loss or a supplier-spend score. Allegations, company responses and adjudicated findings remain distinct. No personal victim data should be published in public repositories.

Required typed domain-assessment fields (declarations, not automated truth verification):
```json
{
  "people_risk_separate": [
    true
  ],
  "allegations_treated_as_facts": [
    false
  ],
  "remedy_basis": [
    "independent_outcome_evidence",
    "company_claim_only",
    "not_established"
  ],
  "personal_data_public": [
    false
  ]
}
```
