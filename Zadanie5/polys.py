import unittest

def add_poly(poly1, poly2):
    length = max(len(poly1), len(poly2))
    result = [(poly1[i] if i < len(poly1) else 0) + (poly2[i] if i < len(poly2) else 0) for i in range(length)]
    return result

def sub_poly(poly1, poly2):
    length = max(len(poly1), len(poly2))
    result = [(poly1[i] if i < len(poly1) else 0) - (poly2[i] if i < len(poly2) else 0) for i in range(length)]
    return result

def mul_poly(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i, coef1 in enumerate(poly1):
        for j, coef2 in enumerate(poly2):
            result[i + j] += coef1 * coef2
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result

def is_zero(poly):
    return all(coef == 0 for coef in poly)

def eq_poly(poly1, poly2):
    return is_zero(sub_poly(poly1, poly2))

def eval_poly(poly, x0):
    result = 0
    for coef in reversed(poly):
        result = result * x0 + coef
    return result

def combine_poly(poly1, poly2):
    result = [0]
    for coef in reversed(poly1):
        result = add_poly(mul_poly(result, poly2), [coef])
    return result

def pow_poly(poly, n):
    result = [1]
    for _ in range(n):
        result = mul_poly(result, poly)
    return result

def diff_poly(poly):
    result = [i * coef for i, coef in enumerate(poly)][1:]
    return result

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x^2

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p2, self.p1), [0, -1, 1])

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 0, 0]))
        self.assertFalse(is_zero([1, 0, 0]))

    def test_eq_poly(self):
        self.assertTrue(eq_poly([1, 0], [1, 0]))
        self.assertFalse(eq_poly([1, 0], [1, 1]))

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p1, 2), 2)
        self.assertEqual(eval_poly(self.p2, 3), 9)

    def test_combine_poly(self):
        self.assertEqual(combine_poly(self.p1, self.p2), [0, 0, 1])
        self.assertEqual(combine_poly(self.p2, [1, 0, 1]), [1, 0, 2, 0, 1])
        self.assertEqual(combine_poly( [1, 0, 1], self.p2), [1, 0, 0, 0, 1])

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p2, 3), [0, 0, 0, 0, 0, 0, 1])

    def test_diff_poly(self):
        self.assertEqual(diff_poly([3, 2, 1]), [2, 2])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()