"""
Test for source.source1
"""
from source.source1 import get_triangle_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(1, 1, 2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_invalid_a_equals_0(self):
        result = get_triangle_type(0, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_b_equals_0(self):
        result = get_triangle_type(1, 0, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_c_equals_0(self):
        result = get_triangle_type(1, 1, 0)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float(self):
        result = get_triangle_type(1.0, 1.0, 1.0)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_invalid_a_is_string(self):
        result = get_triangle_type('error', 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_a_is_dict(self):
        result = get_triangle_type({0: 1, 1: 1, 2: 1})
        self.assertEqual(result, 'equilateral')
