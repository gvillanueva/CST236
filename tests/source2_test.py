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

    def test_get_quadrilateral_other_or_invalid(self):
        result = get_quadrilateral_type(0, 2.0, 1.0, 2.0)
        self.assertEqual(result, 'other_or_invalid')