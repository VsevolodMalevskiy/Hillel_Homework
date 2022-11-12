import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_for_original(self):
        return math.hypot(self.x, self.y)

    def __str__(self):
        return (f"Point({self.x}, {self.y})")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


if __name__ == "__main__":
    a = Point(5, 4)
    b = Point(5, 5)

    print(a == b)
    print(Point.mro())
    b.y = 4
    print(a == b)