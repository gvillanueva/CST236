from pyTona.main import Interface
from ReqTracer import requirements
from unittest import TestCase
import getpass


class TestAcceptableAnswers(TestCase):
    def setUp(self):
        self.qa = Interface()

    @requirements(['#0001', '#0002'])
    def test_ask_invalidKeyword(self):
        answer = self.qa.ask('Is anyone there>')
        self.assertEqual('Was that a question?', answer)

    @requirements(['#0002', '#0004'])
    def test_ask_missingQuestionMark(self):
        answer = self.qa.ask('How do you feel')
        self.assertEqual('Was that a question?', answer)

    @requirements(['#0009'])
    def test_ask_validQuestion_noMatch(self):
        answer = self.qa.ask('How do you feel>')
        self.assertEqual('I don\'t know, please provide the answer', answer)

    @requirements(['#0005'])
    def test_ask_validQuestion_dashesInsteadOfSpaces(self):
        answer = self.qa.ask('How-do-you-feel>')
        self.assertEqual('Was that a question?', answer)

    @requirements(['#0006'])
    def test_ask_90percentValidInitialAnswer5_matches(self):
        pass

    @requirements(['#0006'])
    def test_ask_80percentInitialAnswer5_noMatch(self):
        answer = self.qa.ask('Why don\'t you understand>')
        self.assertEqual('I don\'t know, please provide the answer', answer)

    @requirements(['#0007', '#0019'])
    def test_ask_excludeNumbersFromValid(self):
        answer = self.qa.ask('Who invented Python 2.7>')
        self.assertEqual('Guido Rossum(BFDL)', answer)

    @requirements(['#0008', '#0017'])
    def test_ask_validQuestion_initialAnswer1(self):
        feet = 1284.5
        miles = feet / 5280
        answer = self.qa.ask('What is {0} feet in miles>'.format(feet))
        self.assertEqual('{0}miles'.format(miles), answer)

    @requirements(['#0008', '#0018'])
    def test_ask_validQuestion_initialAnswer2(self):
        # answer = self.qa.ask('How many seconds since 5/4/1986>')
        # self.assertEqual(dateTime, answer)
        pass

    @requirements(['#0008', '#0019'])
    def test_ask_validQuestion_initialAnswer3(self):
        answer = self.qa.ask('Who invented Python>')
        self.assertEqual('Guido Rossum(BFDL)', answer)

    @requirements(['#0008', '#0020'])
    def test_ask_validQuestion_initialAnswer3(self):
        answer = self.qa.ask('Why don\'t you understand me>')
        self.assertEqual('Because you do not speak 1s and 0s', answer)

    @requirements(['#0008', '#0021'])
    def test_ask_validQuestion_initialAnswer3(self):
        answer = self.qa.ask('Why don\'t you shutdown>')
        self.assertEqual('I\'m afraid I can\'t do that {0}'.format(getpass.getuser()), answer)
