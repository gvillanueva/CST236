"""
Test for source.source2
"""
from source.source2 import get_quadrilateral_type
from unittest import TestCase

class  TestGetQuadrilateralType(TestCase):

    def test_get_quadrilateral_square_all_float(self):
        result = get_quadrilateral_type(1.0, 1.0, 1.0, 1.0)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_rectangle_all_float(self):
        result = get_quadrilateral_type(1.0, 2.0, 1.0, 2.0)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_invalid(self):
        result = get_quadrilateral_type(0, 2.0, 1.0, 2.0)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_rhombus(self):
        result = get_quadrilateral_type(2.0, 2.0, 2.0, 2.0, 30, 150, 30, 150)
        self.assertEqual(result, 'rhombus')

    def test_get_quadrilateral_disconnect(self):
        result = get_quadrilateral_type(1.0, 1.0, 1.0, 1.0, 3, 150, 30, 150)
        self.assertEqual(result, 'disconnected')

    def test_get_quadrilateral_other(self):
        result = get_quadrilateral_type(216.0, 133.0, 216.0, 133.0, 97, 83, 97, 83)
        self.assertEqual(result, 'other')