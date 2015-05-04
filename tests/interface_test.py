"""
Tests for source.interface
"""
from source.interface import Interface
from unittest import TestCase


class TestInterface(TestCase):
    # Creates an interface object to be used in every test
    def setUp(self):
        self.interface = Interface()

    # Tests that the interface will stop running when it receives 'X'
    def test_acceptInput_X_stopsRunning(self):
        self.interface.acceptInput('X')
        self.assertFalse(self.interface.running)

    # Tests that other input will not stop the interface
    def test_acceptInput_quit_doesNotQuit(self):
        self.interface.acceptInput('quit')
        self.assertTrue(self.interface.running)

    # Tests that the interface will return its instructions when it receives '?'
    def test_acceptInput_QuestionMark_returnsInstructions(self):
        instructions = self.interface.acceptInput('?')
        self.assertEqual(instructions, '\'X\'- Quit alert system\n\'?\'- Show these instructions')

    # Tests that random orcs can be added for demo purposes
    def test_acceptInput_demo_randomOrcs(self):
        random_orc = self.interface.acceptInput('demo_addorc')
        random_orc2 = self.interface.acceptInput('demo_addorc')
        self.assertNotEqual(random_orc.id, random_orc2.id)

    # Tests that all threats can be wiped by the command 'ENTer the Trees'
    def test_acceptIntput_ENT_wipeThreats(self):
        random_orc = self.interface.acceptInput('demo_addorc')
        random_orc2 = self.interface.acceptInput('demo_addorc')
        self.assertNotEqual(random_orc.id, random_orc2.id) #A little sanity that the threats are created
        remainingThreats = self.interface.acceptInput('ENTer the Trees')
        self.assertEqual(remainingThreats, 0)