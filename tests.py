import unittest
import pyciosa

class TestStringMethods(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()