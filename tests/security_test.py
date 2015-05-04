"""
Tests for source.security
"""
from source.security import Security
from source.orc import Orc
from source.threat import Threat
from unittest import TestCase
import uuid


class TestSecurity(TestCase):
    # Instantiates a security object for use in each test
    def setUp(self):
        self.security = Security()

    # Tests whether the security perimeter is initially breached
    def test_isPerimeterBreached_False(self):
        self.assertFalse(self.security.perimeter_breached)

    # Tests the ability to specify the security's enemy type
    def test_setEnemy_Orc(self):
        self.security.enemy = 'Orc'
        self.assertEqual(self.security.enemy, 'Orc')

    # Tests whether the perimeter has been breached by an enemy
    def test_isPerimeterBreached_byEnemy_True(self):
        self.security.enemy = 'Orc'
        self.security.breach_perimeter('Orc')
        self.assertTrue(self.security.perimeter_breached)

    # Tests that perimeter may be breached by non-enemy without raising alarm
    def test_isPerimeterBreached_byNonEnemy_False(self):
        self.security.enemy = 'Orc'
        self.security.breach_perimeter('Human')
        self.assertFalse(self.security.perimeter_breached)

    # Tests that the security system can get an enemy's distance
    def test_getDistance_25(self):
        orc = Orc(25)
        self.assertEqual(self.security.getDistance(orc), 25)

    # Tests that an unspecified enemy distance is zero
    def test_getDistance_unset_zero(self):
        orc = Orc()
        self.assertEqual(self.security.getDistance(orc), 0)

    # Tests that an unspecified enemy velocity is 0
    def test_getVelocity_unset_zero(self):
        orc = Orc()
        self.assertEqual(self.security.getVelocity(orc), 0)

    # Tests that the security system can get an enemy's velocity
    def test_getVelocity_25(self):
        orc = Orc(velocity=25)
        self.assertEqual(self.security.getVelocity(orc), 25)

    # Tests that the security system can get an enemy's type
    def test_getType_swordsman(self):
        orc = Orc(type='swordsman')
        self.assertEqual(self.security.getType(orc), 'swordsman')

    # Tests that the security system doesn't return swordsman for every type
    def test_getType_notSwordsman(self):
        orc = Orc(type='archer')
        self.assertNotEqual(self.security.getType(orc), 'swordsman')

    # Tests that removal of a non-existent threat does nothing
    def test_removeThreat_doesNotExist(self):
        self.security.removeThreat(uuid.uuid4())

    # Tests that adding a threat returns its unique identifier
    def test_addThreat_nonThreatType_returnsNone(self):
        orc = Orc()
        threatId = self.security.addThreat(orc)
        self.assertEqual(threatId, None)

    # Tests that adding a threat returns its unique identifier
    def test_addThreat_threatType_returnsUuid(self):
        threat = Threat()
        threatId = self.security.addThreat(threat)
        self.assertIsInstance(threatId, uuid.UUID)

    # Tests that an added threat can be found by UUID
    def test_containsThreat_returnsTrue(self):
        threat = Threat()
        threatId = self.security.addThreat(threat)
        self.assertEqual(self.security.containsThreat(threatId), True)

    # Tests that an added threat can be removed
    def test_removeThreat_exists(self):
        orc = Orc()
        threatId = self.security.addThreat(orc)
        self.security.removeThreat(threatId)
        self.assertEqual(self.security.containsThreat(threatId), False)

    # Tests that a nonexistant threat returns 0 priority
    def test_getPriority_threatDoesNotExist(self):
        self.security.getPriority(None)

    # Tests that an existant threat returns its priority
    def test_getPriority_threatExists_returnsThreatPriority(self):
        threat = Threat(priority=10)
        threatId = self.security.addThreat(threat)
        self.assertEqual(self.security.getPriority(threatId), 10)

    # Tests that the threat count is 0 when no threats added
    def test_threatCount_noThreats_returns0(self):
        self.assertEqual(self.security.threatCount, 0)

    # Tests that the treat count i 1 when one threat is added
    def test_threatCount_oneThreat_returns1(self):
        self.security.addThreat(Threat())
        self.assertEqual(self.security.threatCount, 1)

    # Tests that threats can be reset
    def test_resetThreats_twoThreats_threatCountReturns0(self):
        self.security.addThreat(Threat())
        self.security.addThreat(Threat())
        self.security.resetThreats()
        self.assertEqual(self.security.threatCount, 0)
