"""Original HHFinAi domain arithmetic tests; all numbers are synthetic."""
import copy, math, random, unittest
from sf_agent.analytics import *
from sf_agent.validation import DataError

class HumanRights(unittest.TestCase):
    def test_wage_gap(self):self.assertAlmostEqual(wage_gap_cost(1000,300,400,12,.1)['loaded_annual_cost'],1320000)
    def test_above_living_no_negative_cost(self):self.assertEqual(wage_gap_cost(100,500,400,12,0)['loaded_annual_cost'],0)
    def test_workers_integer_not_bool(self):
        with self.assertRaises(DataError):wage_gap_cost(True,300,400,12,.1)
    def test_wage_period_guard(self):
        with self.assertRaises(DataError):wage_gap_cost(1000,300,400,0,.1)
    def test_remedy_coverage(self):self.assertEqual(remedy_coverage(20,100)['verified_remedy_fraction'],.2)
    def test_no_cases_unknown(self):self.assertIsNone(remedy_coverage(0,0)['verified_remedy_fraction'])
    def test_remedy_overclaim(self):
        with self.assertRaises(DataError):remedy_coverage(11,10)
    def test_supply_coverage(self):self.assertEqual(supply_chain_coverage(25,100)['mapped_fraction'],.25)
    def test_severe_harm_priority_despite_low_likelihood(self):self.assertEqual(harm_triage('HIGH','LOW','LOW','LOW')['action'],'PRIORITY_HUMAN_REVIEW')
    def test_unknown_severity_needs_data(self):self.assertEqual(harm_triage('LOW','UNKNOWN','LOW','LOW')['action'],'NEEDS_DATA')
    def test_harm_no_legal_finding(self):self.assertIs(harm_triage('LOW','LOW','LOW','ACTUAL')['legal_liability_determined'],False)
    def test_invalid_severity(self):
        with self.assertRaises(DataError):harm_triage('EXTREME','LOW','LOW','LOW')

if __name__=='__main__':unittest.main()
