"""
@Author Marco A. Gallegos
@Date 2020/03/10
@Description
    Pruebas unitarias para los periodos
"""

import unittest,pyciosa

class TestPeriodoMethods(unittest.TestCase):
    def test_regex(self):
        periodo_ok = "202003"
        periodo_bad = "202013"
        periodo_bad2 = "20200310"
        ok = pyciosa.periodo.is_valid(periodo=periodo_ok)
        bad = pyciosa.periodo.is_valid(periodo=periodo_bad)
        bad2 = pyciosa.periodo.is_valid(periodo=periodo_bad2)
        status = (ok and not bad and not bad2)
        self.assertTrue(status)

    def test_range(self):
        periodo_ok = "202003"
        rango = pyciosa.periodo.interpolate(periodo=periodo_ok)
        self.assertEqual(13, len(rango))

    def test_validate_date(self):
        valid_date = "01.04.2020"
        format = "DD.MM.YYYY"
        self.assertTrue(pyciosa.periodo.validate_date(valid_date, format))

    def test_invalid_date(self):
        invalid_date = "32.01.2020"
        format = "DD.MM.YYYY"
        self.assertFalse(pyciosa.periodo.validate_date(invalid_date, format))

    def test_full_period_label(self):
        period = '202004'
        expected = 'Abril 2020'
        self.assertEqual(pyciosa.periodo.get_period_full_label(period), expected)

    def test_full_period(self):
        period = '20200422'
        self.assertTrue(pyciosa.periodo.is_valid(periodo=period, full=True))
    
    def test_full_period_bad(self):
        period = '20200231'
        self.assertFalse(pyciosa.periodo.is_valid(periodo=period, full=True))