# Executable operation catalogue

Every operation requires supplied assumptions/provenance. No market or issuer data are inferred.

## `dscr`
```python
dscr(cash_available: 'float', debt_service: 'float') -> 'float'
```
See source code and domain methodology for assumptions.

Input units: `{"cash_available": "$money", "debt_service": "$money"}`. Output unit/type: `multiple`.

## `harm_triage`
```python
harm_triage(scale: 'str', scope: 'str', irremediability: 'str', likelihood: 'str') -> 'dict'
```
Original conservative escalation convention, NOT a UN/OECD scoring formula.

Input units: `{"scale": "severity_label", "scope": "severity_label", "irremediability": "severity_label", "likelihood": "likelihood_label"}`. Output unit/type: `human_rights_triage`.

## `holding_period_return`
```python
holding_period_return(initial_dirty_price: 'float', exit_dirty_price: 'float', cash_income: 'float', funding_cost: 'float', transaction_cost: 'float') -> 'float'
```
See source code and domain methodology for assumptions.

Input units: `{"initial_dirty_price": "$money", "exit_dirty_price": "$money", "cash_income": "$money", "funding_cost": "$money", "transaction_cost": "$money"}`. Output unit/type: `decimal_return`.

## `npv`
```python
npv(cashflows: 'list[float]', annual_discount: 'float') -> 'float'
```
Periodic NPV; cashflows[0] is at time zero, then annual periods.

Input units: `{"cashflows": "$money", "annual_discount": "decimal"}`. Output unit/type: `$money`.

## `remedy_coverage`
```python
remedy_coverage(verified_remedied: 'int', total_identified: 'int') -> 'dict'
```
See source code and domain methodology for assumptions.

Input units: `{"verified_remedied": "cases", "total_identified": "cases"}`. Output unit/type: `remedy_coverage`.

## `scale`
```python
scale(value: 'float', factor: 'float') -> 'float'
```
Explicit arithmetic conversion; external unit semantics need human review.

Input units: `{"value": "$input_unit", "factor": "conversion_factor"}`. Output unit/type: `$output_unit`.

## `supply_chain_coverage`
```python
supply_chain_coverage(mapped_exposure: 'float', total_exposure: 'float') -> 'dict'
```
See source code and domain methodology for assumptions.

Input units: `{"mapped_exposure": "$money", "total_exposure": "$money"}`. Output unit/type: `supply_chain_coverage`.

## `wage_gap_cost`
```python
wage_gap_cost(workers: 'int', current_period_wage: 'float', living_period_wage: 'float', periods_per_year: 'int', employer_load: 'float') -> 'dict'
```
See source code and domain methodology for assumptions.

Input units: `{"workers": "persons", "current_period_wage": "$money", "living_period_wage": "$money", "periods_per_year": "periods_per_year", "employer_load": "decimal"}`. Output unit/type: `wage_gap_scenario`.
