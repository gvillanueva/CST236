"""
Tests for source.unit
"""
from source.unit import Unit
from unittest import TestCase

class TestUnit(TestCase):

    # Tests whether the Unit class can be set to use the imperial system
    def test_unit_setSystem_imperial(self):
        units = Unit.setSystem('imperial')
        self.assertEqual(Unit.upi, 1)

    # Tests whether the Unit class can be set to use the metric system
    def test_unit_setSystem_metric(self):
        units = Unit.setSystem('metric')
        self.assertEqual(Unit.upi, 25.4)

    # Tests whether the Unit class can be set to use parsecs
    def test_unit_setSystem_parsecs(self):
        units = Unit.setSystem('parsecs')
        self.assertEqual(Unit.upi, 1.21483369e18)

    # Tests whether the Unit class can be set to use nautical miles
    def test_unit_setSystem_nautical(self):
        units = Unit.setSystem('nautical')
        self.assertEqual(Unit.upi, 1.37149e-5)
