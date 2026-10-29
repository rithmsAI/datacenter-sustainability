import unittest
import numpy as np
from analysis import withdrawal_intensity,load_clean,cooling_scenarios
class AnalysisTests(unittest.TestCase):
    def test_units(self): self.assertEqual(float(withdrawal_intensity(1,1000)),1)
    def test_invalid_denominators(self):
        for value in [0,-1,np.inf,np.nan]:
            with self.assertRaises(ValueError): withdrawal_intensity(1,value)
    def test_censored_is_not_zero(self): self.assertTrue(np.isnan(withdrawal_intensity(np.nan,1000)))
    def test_negative_water(self):
        with self.assertRaises(ValueError): withdrawal_intensity(-1,1000)
    def test_source_shape_and_reconciliation(self):
        annual,sites=load_clean(); self.assertEqual(len(annual),6); self.assertEqual(len(sites),29)
        self.assertEqual(sites.water_withdrawal_ml.isna().sum(),1)
        self.assertTrue(((annual.water_withdrawal_ml-annual.water_discharge_ml)==annual.water_consumption_ml).all())
    def test_location_fixture_prevents_column_shift(self):
        _,s=load_clean(); q=s.set_index('location')
        self.assertEqual(q.loc['San Antonio','water_withdrawal_ml'],420)
        self.assertEqual(q.loc['Quincy','water_withdrawal_ml'],1292)
    def test_scenario_energy_balance(self):
        s=cooling_scenarios(); np.testing.assert_allclose(s.facility_mwh,s.it_mwh+s.non_it_mwh)
        with self.assertRaises(ValueError): cooling_scenarios(0)
if __name__=='__main__': unittest.main()
