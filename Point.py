import typing


class Point:
    def __init__(self, *args):
        if len(args) > 3:
            raise ValueError("Too many parameters")
        elif len(args) < 1:
            raise ValueError("Not enough parameters")
        if all(isinstance(arg, (float, int)) for arg in args[:3]) and len(args) == 3:
            self.x = float(args[0])
            self.y = float(args[1])
            self.z = float(args[2])
        elif isinstance(args[0], typing.Iterable) and len(args[0]) == 3 and len(args) == 1:
            self.__init__(args[0][0], args[0][1], args[0][2])
        elif isinstance(args[0], Point) and len(args) == 1:
            self.__init__(args[0].x, args[0].y, args[0].z)
        else:
            raise ValueError("Improper parameters")

    def clone(self):
        return Point(self)

    def __add__(self, other):
        if isinstance(other, Point):
            self.x += float(other.x)
            self.y += float(other.y)
            self.z += float(other.z)
            return self.clone()
        elif (other is typing.Iterable[float] or other is typing.Iterable[int]) and len(other) == 3:
            self.x += float(other[0])
            self.y += float(other[1])
            self.z += float(other[2])
            return self.clone()
        else:
            raise ValueError("Improper value")

    def __sub__(self, other):
        if isinstance(other, Point):
            self.x -= float(other.x)
            self.y -= float(other.y)
            self.z -= float(other.z)
            return self.clone()
        elif (other is typing.Iterable[float] or other is typing.Iterable[int]) and len(other) == 3:
            self.x -= float(other[0])
            self.y -= float(other[1])
            self.z -= float(other[2])
            return self.clone()
        else:
            raise ValueError("Improper value")

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y and self.z == other.z
        elif (other is typing.Iterable[float] or other is typing.Iterable[int]) and len(other) == 3:
            return self.x == float(other[0]) and self.y == float(other[1]) and self.z == float(other[2])
        else:
            return False

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
