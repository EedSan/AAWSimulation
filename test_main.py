from unittest import TestCase

import main


class Test(TestCase):
    def test_point_on_sphere(self):
        point_coords = main.random_point_on_sphere_coords()
        point_formula = point_coords[0] ** 2 + point_coords[1] ** 2 + 4 * point_coords[2] ** 2
        print(point_formula)
        assert True if 9990 <= point_formula <= 10010 else self.fail()
