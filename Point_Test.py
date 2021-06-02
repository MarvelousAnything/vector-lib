import unittest

from Point import Point


class PointOperatorTests(unittest.TestCase):
    def test_equality(self):
        point1 = Point(1, 2, 3)
        point2 = Point(1, 2, 3)
        point3 = Point(3, 2, 1)
        self.assertTrue(point1 == point2)
        self.assertFalse(point1 == point3 or point2 == point3)

    def test_addition(self):
        point1 = Point(1, 2, 3)
        point2 = Point(3, 2, 1)
        point3 = point1 + point2
        self.assertEqual(point3, Point(4, 4, 4))

    def test_subtraction(self):
        point1 = Point(1, 2, 3)
        point2 = Point(3, 2, 1)
        point3 = point1 - point2
        self.assertEqual(point3, Point(-2, 0, 2))


class PointConstructorTests(unittest.TestCase):
    def test_constructor_to_many_parameters_error(self):
        with self.assertRaisesRegex(ValueError, "Too many parameters"):
            Point(1, 2, 3, 4)

    def test_constructor_not_enough_parameters_error(self):
        with self.assertRaisesRegex(ValueError, "Not enough parameters"):
            Point()

    def test_iterable_parameter(self):
        self.assertIsNotNone(point1 := Point([2, 4, 6]))
        point2 = Point(2, 4, 6)
        self.assertEqual(point1, point2)


if __name__ == '__main__':
    unittest.main()
