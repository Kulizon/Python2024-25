from math import gcd
import unittest

def simplify_frac(frac):
    common_divisor = gcd(frac[0], frac[1])
    numerator = frac[0] // common_divisor
    denominator = frac[1] // common_divisor
    if denominator < 0:
        numerator, denominator = -numerator, -denominator
    return [numerator, denominator]

def add_frac(frac1, frac2):
    numerator = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    denominator = frac1[1] * frac2[1]
    return simplify_frac([numerator, denominator])

def sub_frac(frac1, frac2):
    numerator = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    denominator = frac1[1] * frac2[1]
    return simplify_frac([numerator, denominator])

def mul_frac(frac1, frac2):
    numerator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    return simplify_frac([numerator, denominator])

def div_frac(frac1, frac2):
    if frac2[0] == 0:
        raise ValueError("Dzielenie przez zero!")
    numerator = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[0]
    return simplify_frac([numerator, denominator])

def is_positive(frac):
    return frac[0] * frac[1] > 0

def is_zero(frac):
    return frac[0] == 0

def cmp_frac(frac1, frac2):
    difference = sub_frac(frac1, frac2)
    if difference[0] < 0:
        return -1
    elif difference[0] > 0:
        return 1
    return 0

def frac2float(frac):
    return frac[0] / frac[1]


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2, 3], [3, 4]), [1, 2])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [3, 4]), [2, 3])
        with self.assertRaises(ValueError):
            div_frac([1, 2], [0, 1])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertFalse(is_zero([1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 3]), 0)
        self.assertEqual(cmp_frac([1, 4], [1, 3]), -1)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([1, 2]), 0.5)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
