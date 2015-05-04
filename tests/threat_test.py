"""
Tests for source.threat
"""
from source.threat import Threat
from source.orc import Orc
from unittest import TestCase


class TestThreat(TestCase):

    # Tests that a threat can be assigned a priority
    def test_init_priority10_equals10(self):
        threat = Threat(priority=10)
        self.assertEqual(threat.priority, 10)

    # Tests that a threat without an assigned priority has priority 0
    def test_init_priorityUnset_equals0(self):
        threat = Threat()
        self.assertEqual(threat.priority, 0)

    # Test that a threat's object, when unset, is None
    def test_init_objUnset_equalsNone(self):
        threat = Threat()
        self.assertEqual(threat.obj, None)

    # Tests that a threat can be assigned an object
    def test_init_objSet_equalsObj(self):
        orc = Orc()
        threat = Threat(obj=orc)
        self.assertEqual(threat.obj, orc)

    # Tests that two threats do not have the same id
    def test_init_idSet_unique(self):
        threat = Threat()
        threat2 = Threat()
        self.assertNotEqual(threat.id, threat2.id)