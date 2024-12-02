import math
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

    @classmethod
    def from_points(cls, points):
        if len(points) != 3:
            raise ValueError("Dokładnie trzy punkty są wymagane")
        p1, p2, p3 = points
        d = 2 * (p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y))
        if d == 0:
            raise ValueError("Punkty są współliniowe i nie definiują okręgu")
        ux = (
            (p1.x ** 2 + p1.y ** 2) * (p2.y - p3.y) +
            (p2.x ** 2 + p2.y ** 2) * (p3.y - p1.y) +
            (p3.x ** 2 + p3.y ** 2) * (p1.y - p2.y)
        ) / d
        uy = (
            (p1.x ** 2 + p1.y ** 2) * (p3.x - p2.x) +
            (p2.x ** 2 + p2.y ** 2) * (p1.x - p3.x) +
            (p3.x ** 2 + p3.y ** 2) * (p2.x - p1.x)
        ) / d
        center = Point(ux, uy)
        radius = center.distance(p1)
        return cls(center.x, center.y, radius)

    @property
    def top(self):
        return self.pt.y + self.radius

    @property
    def bottom(self):
        return self.pt.y - self.radius

    @property
    def left(self):
        return self.pt.x - self.radius

    @property
    def right(self):
        return self.pt.x + self.radius

    @property
    def width(self):
        return 2 * self.radius

    @property
    def height(self):
        return 2 * self.radius

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)
