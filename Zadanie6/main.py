import unittest
import math

class Poly:
    def __init__(self, c=0, n=0):
        self.size = n + 1
        self.a = [0] * self.size
        self.a[-1] = c

    def __str__(self):
        return str(self.a)

    def __add__(self, other):
        result_coeffs = [a + b for a, b in zip(self.a, other.a)]
        if len(self.a) > len(other.a):
            result_coeffs.extend(self.a[len(other.a):])
        else:
            result_coeffs.extend(other.a[len(self.a):])
        return Poly.from_coeffs(result_coeffs)

    def __sub__(self, other):
        result_coeffs = [a - b for a, b in zip(self.a, other.a)]
        if len(self.a) > len(other.a):
            result_coeffs.extend(self.a[len(other.a):])
        else:
            result_coeffs.extend(-b for b in other.a[len(self.a):])
        return Poly.from_coeffs(result_coeffs)

    def __mul__(self, other):
        result_coeffs = [0] * (len(self.a) + len(other.a) - 1)
        for i, coef1 in enumerate(self.a):
            for j, coef2 in enumerate(other.a):
                result_coeffs[i + j] += coef1 * coef2
        return Poly.from_coeffs(result_coeffs)

    def __pos__(self):
        return self

    def __neg__(self):
        return Poly.from_coeffs([-a for a in self.a])

    def __eq__(self, other):
        return self.a == other.a

    def eval(self, x):
        result = 0
        for coeff in reversed(self.a):
            result = result * x + coeff
        return result

    @staticmethod
    def from_coeffs(coeffs):
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        poly = Poly()
        poly.size = len(coeffs)
        poly.a = coeffs
        return poly

    def is_zero(self):
        return all(coeff == 0 for coeff in self.a)

class TestPoly(unittest.TestCase):
    def test_add(self):
        p1 = Poly.from_coeffs([2, 1])  # 2 + x
        p2 = Poly.from_coeffs([3, 2])  # 3 + 2x
        self.assertEqual((p1 + p2).a, [5, 3])  # 5 + 3x

    def test_sub(self):
        p1 = Poly.from_coeffs([5, 3])  # 5 + 3x
        p2 = Poly.from_coeffs([2, 1])  # 2 + x
        self.assertEqual((p1 - p2).a, [3, 2])  # 3 + 2x

    def test_mul(self):
        p1 = Poly.from_coeffs([1, 1])  # 1 + x
        p2 = Poly.from_coeffs([1, 1])  # 1 + x
        self.assertEqual((p1 * p2).a, [1, 2, 1])  # 1 + 2x + x^2

    def test_eval(self):
        p = Poly.from_coeffs([2, 3, 4])  # 2 + 3x + 4x^2
        self.assertEqual(p.eval(2), 24)  # 2 + 3*2 + 4*4 = 24

    def test_is_zero(self):
        p = Poly.from_coeffs([0, 0, 0]) 
        self.assertTrue(p.is_zero())

    def test_eq(self):
        p1 = Poly.from_coeffs([1, 2, 3])
        p2 = Poly.from_coeffs([1, 2, 3])
        p3 = Poly.from_coeffs([1, 2, 4])
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def cross(self, other):
        return self.x * other.y - self.y * other.x
    
    def __hash__(self):
        return hash((self.x, self.y))


class TestPoint(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Point(1, 2)), "(1, 2)")

    def test_repr(self):
        self.assertEqual(repr(Point(1, 2)), "Point(1, 2)")

    def test_eq(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertFalse(Point(1, 2) == Point(2, 3))

    def test_ne(self):
        self.assertTrue(Point(1, 2) != Point(2, 3))
        self.assertFalse(Point(1, 2) != Point(1, 2))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))

    def test_sub(self):
        self.assertEqual(Point(3, 4) - Point(1, 2), Point(2, 2))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(3, 4), 11)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(3, 4)), -2)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)

    def test_hash(self):
        self.assertEqual(hash(Point(1, 2)), hash((1, 2)))


if __name__ == '__main__':
    unittest.main()
