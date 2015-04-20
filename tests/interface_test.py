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