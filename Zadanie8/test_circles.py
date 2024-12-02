import pytest
from circles import Circle
from points import Point
import math

def test_init():
    c = Circle(0, 0, 5)
    assert c.radius == 5
    assert c.pt == Point(0, 0)
    with pytest.raises(ValueError):
        Circle(0, 0, -1)

def test_area():
    c = Circle(0, 0, 3)
    assert pytest.approx(c.area()) == math.pi * 9

def test_move():
    c = Circle(1, 1, 3)
    moved_circle = c.move(2, 3)
    assert moved_circle.pt == Point(3, 4)

def test_cover():
    c1 = Circle(0, 0, 2)
    c2 = Circle(5, 0, 2)
    covering_circle = c1.cover(c2)
    assert pytest.approx(covering_circle.radius) == 4.5

def test_from_points():
    p1 = Point(0, 0)
    p2 = Point(1, 0)
    p3 = Point(0, 1)
    c = Circle.from_points((p1, p2, p3))
    assert pytest.approx(c.pt.x) == 0.5
    assert pytest.approx(c.pt.y) == 0.5
    assert pytest.approx(c.radius) == math.sqrt(0.5)

def test_bounding_box():
    c = Circle(0, 0, 3)
    assert c.top == 3
    assert c.bottom == -3
    assert c.left == -3
    assert c.right == 3
    assert c.width == 6
    assert c.height == 6
    assert c.topleft == Point(-3, 3)
    assert c.bottomleft == Point(-3, -3)
    assert c.topright == Point(3, 3)
    assert c.bottomright == Point(3, -3)
