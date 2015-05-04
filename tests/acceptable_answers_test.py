from pyTona.main import Interface
from ReqTracer import requirements
from unittest import TestCase
import getpass
from datetime import datetime, date, time

def inchesToMillimetersWrong(inches):
    return inches * 4.52

def inchesToMillimeters(inches):
    return inches * 25.4

class TestAcceptableAnswers(TestCase):
    def setUp(self):
        self.qa = Interface()

    @requirements(['#0001', '#0002', '#0003'])
    def test_ask_invalidKeyword(self):
        answer = self.qa.ask('Is anyone there?')
        self.assertEqual('Was that a question?', answer)

    @requirements(['#0002', '#0004'])
    def test_ask_missingQuestionMark(self):
        answer = self.qa.ask('How do you feel')
        self.assertEqual('Was that a question?', answer)

    @requirements(['#0009'])
    def test_ask_validQuestion_noMatch(self):
        answer = self.qa.ask('How do you feel?')
        self.assertEqual('I don\'t know, please provide the answer', answer)

    @requirements(['#0005'])
    def test_ask_validQuestion_dashesInsteadOfSpaces(self):
        answer = self.qa.ask('How-do-you-feel?')
        self.assertEqual('Was that a question?', answer)

    @requirements(['#0006'])
    def test_ask_90percentMatch_InitialAnswer5_matches(self):
        answer = self.qa.ask('Why dun\'t yu undrstnd me?')
        self.assertEqual('Because you do not speak 1s and 0s', answer)

    @requirements(['#0006'])
    def test_ask_below90percent_InitialAnswer5_noMatch(self):
        answer = self.qa.ask('Why dun\'t you understnd?')
        self.assertEqual('I don\'t know, please provide the answer', answer)

    @requirements(['#0007', '#0019'])
    def test_ask_excludeNumbersFromValid(self):
        answer = self.qa.ask('Why don\'t you understand me 2 2 2 2 2 2?')
        self.assertEqual('Because you do not speak 1s and 0s', answer)

    @requirements(['#0010', '#0011', '#0012'])
    def test_teach_noPreviousQuestion(self):
        response = self.qa.teach("Wolfgang Amadeus Mozart");
        self.assertEqual('Please ask a question first', response)

    @requirements(['#0009', '#0010', '#0011', '#0012'])
    def test_teach_previousQuestion_learns(self):
        answer = self.qa.ask('Who was the most prolific classical composer?')
        self.assertEqual('I don\'t know, please provide the answer', answer)
        self.qa.teach("Wolfgang Amadeus Mozart");
        answer = self.qa.ask('Who was the most prolific classical composer?')
        self.assertEqual('Wolfgang Amadeus Mozart', answer)

    @requirements(['#0009', '#0010', '#0011', '#0013'])
    def test_teach_alreadyAnswered(self):
        answer = self.qa.ask('Who was the most prolific classical composer?')
        self.assertEqual('I don\'t know, please provide the answer', answer)
        self.qa.teach("Wolfgang Amadeus Mozart");
        answer = self.qa.ask('Who was the most prolific classical composer?')
        self.assertEqual('Wolfgang Amadeus Mozart', answer)
        response = self.qa.teach("Ludwig Van Beethoven")
        self.assertEqual('I don\'t know about that. I was taught differently', response)

    @requirements(['#0009', '#0010', '#0011'])
    def test_teach_functionPointer(self):
        answer = self.qa.ask('What is 1 inch in millimeters?')
        self.assertEqual('I don\'t know, please provide the answer', answer)
        self.qa.teach(inchesToMillimeters)
        answer = self.qa.ask('What is 1 inch in millimeters?')
        self.assertEqual(25.4, answer)

    @requirements(['#0010', '#0011'])
    def test_teach_numericAnswer(self):
        answer = self.qa.ask('What year was Mozart born?')
        self.assertEqual('I don\'t know, please provide the answer', answer)
        self.qa.teach(1756)
        answer = self.qa.ask('What year was Mozart born?')
        self.assertEqual(1756, answer)

    @requirements(['#0014', '#0015', '#0016'])
    def test_correct_noPreviousQuestion(self):
        response = self.qa.teach('Ludwig Van Beethoven')
        self.assertEqual('Please ask a question first', response)

    @requirements(['#0014', '#0015'])
    def test_correct_alreadyAnswered(self):
        self.qa.ask('Who was the most prolific classical composer?')
        self.qa.teach("Wolfgang Amadeus Mozart")
        self.qa.correct("Ludwig Van Beethoven")
        answer = self.qa.ask('Who was the most prolific classical composer?')
        self.assertEqual('Ludwig Van Beethoven', answer)

    @requirements(['#0014', '#0015'])
    def test_correct_numericAnswer_invalid(self):
        self.qa.ask('What year was Mozart born?')
        self.qa.teach('1752')
        self.qa.correct(1756)
        answer = self.qa.ask('What year was Mozart born?')
        self.assertEqual(1756, answer)

    @requirements(['#0009', '#0014', '#0015'])
    def test_correct_functionPointer(self):
        answer = self.qa.ask('What is 1 inch in millimeters?')
        self.assertEqual('I don\'t know, please provide the answer', answer)
        self.qa.teach(inchesToMillimetersWrong)
        answer = self.qa.ask('What is 1 inch in millimeters?')
        self.assertEqual(4.52, answer)
        self.qa.correct(inchesToMillimeters)
        answer = self.qa.ask('What is 1 inch in millimeters?')
        self.assertEqual(25.4, answer)

    @requirements(['#0008', '#0017'])
    def test_ask_validQuestion_initialAnswer1(self):
        feet = 1284.5
        miles = feet / 5280
        answer = self.qa.ask('What is {0} feet in miles?'.format(feet))
        self.assertEqual('{0} miles'.format(miles), answer)

    @requirements(['#0008', '#0019'])
    def test_ask_validQuestion_initialAnswer2(self):
        answer = self.qa.ask('Who invented Python?')
        self.assertEqual('Guido Rossum(BDFL)', answer)

    @requirements(['#0008', '#0020'])
    def test_ask_validQuestion_initialAnswer3(self):
        answer = self.qa.ask('Why don\'t you understand me?')
        self.assertEqual('Because you do not speak 1s and 0s', answer)

    @requirements(['#0008', '#0021'])
    def test_ask_validQuestion_initialAnswer4(self):
        answer = self.qa.ask('Why don\'t you shutdown?')
        self.assertEqual('I\'m afraid I can\'t do that {0}'.format(getpass.getuser()), answer)
