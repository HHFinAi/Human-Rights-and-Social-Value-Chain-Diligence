"""Operational scenarios and coverage. These do not monetise the value of human rights."""
from __future__ import annotations
from .maths import COMMON_OPERATIONS, checked, fraction, number, operation, positive, require

@operation({'workers':'persons','current_period_wage':'$money','living_period_wage':'$money','periods_per_year':'periods_per_year','employer_load':'decimal'},'wage_gap_scenario')
def wage_gap_cost(workers: int,current_period_wage: float,living_period_wage: float,periods_per_year: int,employer_load: float) -> dict:
    require(type(workers) is int and workers>=0,'workers must be a nonnegative integer')
    require(type(periods_per_year) is int and 1<=periods_per_year<=366,'periods_per_year must be 1..366')
    c=checked(current_period_wage,'current_period_wage',0);l=positive(living_period_wage,'living_period_wage');load=checked(employer_load,'employer_load',0)
    gap=max(0,l-c);direct=workers*gap*periods_per_year
    return {'period_gap_per_worker':gap,'direct_annual_cost':direct,'loaded_annual_cost':direct*(1+load),
            'not_a_complete_living_wage_or_remedy_assessment':True}

@operation({'verified_remedied':'cases','total_identified':'cases'},'remedy_coverage')
def remedy_coverage(verified_remedied: int,total_identified: int) -> dict:
    require(type(total_identified) is int and total_identified>=0,'total_identified must be integer >=0')
    require(type(verified_remedied) is int and 0<=verified_remedied<=total_identified,'invalid remedy count')
    return {'verified_remedy_fraction':verified_remedied/total_identified if total_identified else None,
            'remaining_identified_cases':total_identified-verified_remedied,'zero_cases_proves_no_harm':False}

@operation({'mapped_exposure':'$money','total_exposure':'$money'},'supply_chain_coverage')
def supply_chain_coverage(mapped_exposure: float,total_exposure: float) -> dict:
    total=positive(total_exposure,'total_exposure');mapped=checked(mapped_exposure,'mapped_exposure',0,total)
    return {'mapped_fraction':mapped/total,'unmapped_fraction':1-mapped/total,'coverage_is_not_severity':True}

@operation({'scale':'severity_label','scope':'severity_label','irremediability':'severity_label','likelihood':'likelihood_label'},'human_rights_triage')
def harm_triage(scale: str,scope: str,irremediability: str,likelihood: str) -> dict:
    """Original conservative escalation convention, NOT a UN/OECD scoring formula."""
    for value in (scale,scope,irremediability): require(value in {'HIGH','MEDIUM','LOW','UNKNOWN'},'invalid severity label')
    require(likelihood in {'HIGH','MEDIUM','LOW','UNKNOWN','ACTUAL'},'invalid likelihood')
    if 'HIGH' in (scale,scope,irremediability):action='PRIORITY_HUMAN_REVIEW'
    elif 'UNKNOWN' in (scale,scope,irremediability) or likelihood=='UNKNOWN':action='NEEDS_DATA'
    else:action='HUMAN_REVIEW_REQUIRED'
    return {'action':action,'likelihood_does_not_cancel_severe_harm':True,'legal_liability_determined':False}
OPERATIONS=dict(COMMON_OPERATIONS)
OPERATIONS.update({f.__name__:f for f in (wage_gap_cost,remedy_coverage,supply_chain_coverage,harm_triage)})
