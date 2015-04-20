from source.security import Security
from source.orc import Orc
from unittest import TestCase

class TestSecurity(TestCase):
    def setUp(self):
        self.security = Security()

    def test_isPerimeterBreached_False(self):
        self.assertFalse(self.security.perimeter_breached)

    def test_setEnemy_Orc(self):
        self.security.enemy = 'Orc'
        self.assertEqual(self.security.enemy, 'Orc')

    def test_isPerimeterBreached_byEnemy_True(self):
        self.security.enemy = 'Orc'
        self.security.breach_perimeter('Orc')
        self.assertTrue(self.security.perimeter_breached)

    def test_isPerimeterBreached_byNonEnemy_False(self):
        self.security.enemy = 'Orc'
        self.security.breach_perimeter('Human')
        self.assertFalse(self.security.perimeter_breached)

    def test_getDistance_25(self):
        orc = Orc(25)
        self.assertEqual(self.security.getDistance(orc), 25)

    def test_getDistance_unset_zero(self):
        orc = Orc()
        self.assertEqual(self.security.getDistance(orc), 0)

    def test_getVelocity_unset_zero(self):
        orc = Orc()
        self.assertEqual(self.security.getVelocity(orc), 0)

    def test_getVelocity_25(self):
        orc = Orc(velocity=25)
        self.assertEqual(self.security.getVelocity(orc), 25)