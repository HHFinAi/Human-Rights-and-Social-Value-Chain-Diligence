# Methodology and model boundaries

Risks to people are not reduced to monetary loss or a supplier-spend score. Allegations, company responses and adjudicated findings remain distinct. No personal victim data should be published in public repositories.

## Analytical outputs
- Affected-stakeholder and value-chain map
- Salient-harm and evidence register
- Prevention/remedy milestones and coverage
- Separate financial-transmission and stewardship handoffs

## Calculation library
The implementation is in `sf_agent/analytics.py`; generic helpers are in `sf_agent/maths.py`. Every exposed operation has argument-unit and result-unit metadata and is callable with `python -m sf_agent calc`. Arguments are not sourced automatically. See the operation inventory below, the worked example and domain regression tests.

### Human-rights calculations and non-financial safeguards
`wage_gap_cost` computes workers × max(living-period wage−current-period wage,0) × periods per year × (1+employer load). Population, wage definition, geography, period, benefits and living-wage benchmark require evidence. This is a direct-cost scenario, not a complete remedy model, wage-standard certification or legal calculation.

`remedy_coverage` reports independently verified remedied cases / identified cases; when no cases are identified, the fraction is null, not a claim of no harm. `supply_chain_coverage` is a mapping-coverage metric, not human-rights severity. `harm_triage` is an original conservative workflow convention: any HIGH scale, scope or irremediability goes to priority human review, regardless of a low declared likelihood; missing severity becomes NEEDS_DATA. It is not an OHCHR/OECD numeric rating, a legal finding or a substitute for affected-person evidence. People-risk and financial-risk conclusions remain separate.


## Evidence status
Causal and legal interpretations remain human judgments. The software is not a complete implementation or certification of the referenced standards. Read the exact applicable original documents; the dated source register gives the verification scope. Proposed changes and future validation dates must not be applied retrospectively or represented as current law.
