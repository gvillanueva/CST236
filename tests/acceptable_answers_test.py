from pyTona.main import Interface
from ReqTracer import requirements
from unittest import TestCase


class TestAcceptableAnswers(TestCase):

    @requirements(['#0001'])
    def test_ask_validQuestion_invalidPrefix(self):
        qa = Interface()
        answer = qa.ask('Is anyone there?')
        self.assertEqual('Was that a question?', answer)