"""
@Author Marco A. Gallegos
@Date 2020/08/01
@Description
    Pruebas unitarias para los periodos
"""

import unittest,pyciosa

class TestPeriodoFullMethods(unittest.TestCase):
    def test_regex(self):
        periodo_ok = "20200322"
        periodo_bad = "20201333"
        periodo_bad2 = "2020031010"
        ok = pyciosa.periodo_full.is_valid(periodo=periodo_ok)
        bad = pyciosa.periodo_full.is_valid(periodo=periodo_bad)
        bad2 = pyciosa.periodo_full.is_valid(periodo=periodo_bad2)
        status = (ok and not bad and not bad2)
        self.assertTrue(status)

    def test_full_period(self):
        period = '20200422'
        expected = list([2020,4,22])
        year, month, day = pyciosa.periodo_full.split(period)
        result = list([year, month, day])
        self.assertEqual(expected, result)