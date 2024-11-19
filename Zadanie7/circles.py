import math
import unittest
from points import Point

class Circle:
    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Promień nie może być ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * self.radius ** 2

    def move(self, x, y):
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        center_dist = self.pt.distance(other.pt)
        new_radius = (center_dist + self.radius + other.radius) / 2
        if center_dist == 0:
            new_center = Point(self.pt.x, self.pt.y)
        else:
            dx = (other.pt.x - self.pt.x) / center_dist
            dy = (other.pt.y - self.pt.y) / center_dist
            new_center = Point(
                self.pt.x + dx * (new_radius - self.radius),
                self.pt.y + dy * (new_radius - self.radius)
            )
        return Circle(new_center.x, new_center.y, new_radius)



class TestCircle(unittest.TestCase):
    def test_init(self):
        c = Circle(0, 0, 5)
        self.assertEqual(c.radius, 5)
        self.assertEqual(c.pt, Point(0, 0))
        with self.assertRaises(ValueError):
            Circle(0, 0, -1)

    def test_area(self):
        c = Circle(0, 0, 3)
        self.assertAlmostEqual(c.area(), math.pi * 9)

    def test_move(self):
        c = Circle(1, 1, 3)
        moved_circle = c.move(2, 3)
        self.assertEqual(moved_circle.pt, Point(3, 4))

    def test_cover(self):
        c1 = Circle(0, 0, 2)
        c2 = Circle(5, 0, 2)
        covering_circle = c1.cover(c2)
        self.assertAlmostEqual(covering_circle.radius, 4.5)

if __name__ == '__main__':
    unittest.main()
