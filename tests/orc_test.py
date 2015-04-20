"""
Tests for source.orc
"""
from source.orc import Orc
from unittest import TestCase


class TestOrc(TestCase):
    # Tests that the type of the orc can be set in the constructor
    def test_getType_archer_isArcher(self):
        obj = Orc(type='archer')
        self.assertEqual(obj.type, 'archer')

    # Tests that default type of orc is builder
    def test_getType_orcArcher_none_isBuilder(self):
        obj = Orc()
        self.assertEqual(obj.type, 'builder')

    # Tests that a newly instantiated Orc is alive
    def test_isAlive_newOrc_returnsTrue(self):
        obj = Orc()
        self.assertEqual(obj.isAlive, True)

    # Tests that an Orc can be "killed"
    def test_isAlive_deadOrc_returnsFalse(self):
        obj = Orc()
        obj.kill()
        self.assertEqual(obj.isAlive, False)