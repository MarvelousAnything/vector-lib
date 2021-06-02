from Point import Point


class Vector:
    def __init__(self, point: Point):
        self.point = point

    @property
    def vector(self):
        return self.point.point
