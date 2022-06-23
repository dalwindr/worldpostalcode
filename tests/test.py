

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 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12
from pyworldzipcode import pyinferzipcode as pz
import unittest


class TestModule(unittest.TestCase):
    """Checks for the sanity of all module methods"""

    def test_get__pincode(self):
        current_result = pz.WorldPostalSearch()._get("AD100","AD")
        self.assertTrue(bool(current_result[0]))

    def test_get__pincodeHasIN(self):
        current_result = pz.WorldPostalSearch()._get("110018","IN")
        print(current_result)
        self.assertTrue(bool(current_result[0]))

    def test_get__pincodelist(self):
        current_result = pz.WorldPostalSearch()._get(["AD100", "AD100"], "AD")
        self.assertTrue(bool(current_result[0]))

    def test_bulkget_pincode(self):
        current_result = pz.WorldPostalSearch().bulkget(
            [("AD100", "AD"), ("AD1000", "AD"), ("AD100", "AD"), ("AD200", "AD"), ("AD200", "IND")])
        print(current_result)
        self.assertTrue(bool(current_result[0]))

    def test_bulkget_pincode_us(self):
        current_result = pz.WorldPostalSearch().bulkget(
            [("99553", "US"), ("99506", "US")])
        print(current_result)
        self.assertTrue(bool(current_result[0]))

    def test_bulkget_notmatch(self):
        current_result = pz.WorldPostalSearch().bulkget(
            [("AD100", "IND"), ("AD100", "IND"),("AD100", "IND"), ("AD100", "IND")])
        self.assertTrue(not bool(current_result[0]))

    def test_valid_countries(self):
        current_result = pz.WorldPostalSearch().valid_countries()
        self.assertTrue(bool(current_result[0]))


if __name__ == "__main__":
    unittest.main()
