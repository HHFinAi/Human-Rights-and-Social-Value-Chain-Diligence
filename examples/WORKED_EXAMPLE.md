# Worked example — Human-Rights and Social-Value-Chain Diligence Agent

**SYNTHETIC / RESEARCH_ONLY. All company, portfolio, instrument and outcome values are fictional. No capital should be deployed from this example.**

## Investment-relevant observation
For 1,000 workers paid 300 per period versus a supplied living-wage scenario of 400, 12 periods and a 10% employer load, the direct annual gap is **1.2 million**, and the loaded annual direct cost is **1.32 million** in the stated currency.

## Reproduce the arithmetic
From the repository root:
```bash
python -m sf_agent calc --operation wage_gap_cost --arguments examples/calculation-arguments.json
```

### Inputs
```json
{
  "workers": 1000,
  "current_period_wage": 300,
  "living_period_wage": 400,
  "periods_per_year": 12,
  "employer_load": 0.1
}
```

### Recomputed result
```json
{
  "period_gap_per_worker": 100.0,
  "direct_annual_cost": 1200000.0,
  "loaded_annual_cost": 1320000.0,
  "not_a_complete_living_wage_or_remedy_assessment": true
}
```

## What the result does not establish
Validate the geography, household/benefits convention, worker population and wage benchmark. The cost estimate is not proof of remedy or a licence to tolerate harm. Human-rights severity and affected-person outcomes remain distinct from investor materiality.

## Diligence handoff
Fictional supply chain: a low-spend supplier can present severe risks; an audit or a closed complaint is not automatically evidence of remedy.

Register source-backed inputs, contrary evidence, material data gaps and the investment constraints before replacing this illustrative result with actual research. Unit, boundary, timing, attribution and legal judgments are not supplied by arithmetic alone. No human research approval is recorded for this example.
