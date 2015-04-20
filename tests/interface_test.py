from source.interface import Interface
from unittest import TestCase

class TestInterface(TestCase):
    def setUp(self):
        self.interface = Interface()

    def test_acceptInput_X_stopsRunning(self):
        self.interface.acceptInput('X')
        self.assertFalse(self.interface.running)

    def test_acceptInput_quit_doesNotQuit(self):
        self.interface.acceptInput('quit')
        self.assertTrue(self.interface.running)