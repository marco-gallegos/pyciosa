"""
@author Marco A. Gallegos
@date 2020/03/10
@description
pruebas unitarias locales
"""
import unittest

import pyciosa, pendulum


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

    def test_sql_date_diferent(self):
        expected_result = '2020-02-29'
        computed_result = pyciosa.periodo.get_date_for_sql_filter_from_periodo(periodo='202002')
        self.assertEqual(computed_result, expected_result)
    
    def test_sql_date_bad_periodo(self):
        computed_result = pyciosa.periodo.get_date_for_sql_filter_from_periodo(periodo='202000')
        self.assertEqual(computed_result, None)

    def test_sql_date_current_periodo(self):
        computed_result = pyciosa.periodo.get_date_for_sql_filter_from_periodo()
        self.assertEqual(computed_result, pendulum.now().format("YYYY-MM-DD"))

if __name__ == '__main__':
    unittest.main()