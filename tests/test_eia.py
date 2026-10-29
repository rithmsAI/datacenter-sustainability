import unittest
import pandas as pd
from analysis import ROOT
from scripts.extract_eia import extract
class EiaTests(unittest.TestCase):
    def test_extraction_matches_shipped_data(self):
        expected=pd.read_csv(ROOT/'data/raw/eia_regional_sales.csv')
        pd.testing.assert_frame_equal(extract(),expected,check_dtype=False)
    def test_complete_panel_and_scale(self):
        data=extract(); self.assertEqual(data.groupby('state').size().tolist(),[16]*5)
        self.assertTrue(data.sales_mwh.between(1e7,1e9).all())
