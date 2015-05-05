from pyTona.main import Interface
import pyTona.answer_funcs
from ReqTracer import requirements
from unittest import TestCase
from subprocess import Popen, PIPE
import getpass
from datetime import datetime, date, time
import time as sleepytime
from mock import Mock, patch, MagicMock
import socket
from pyTona.answer_funcs import seq_finder, FibSeqFinder
import random
import os

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

    @requirements(['#0022'])
    @patch('pyTona.answer_funcs.get_git_branch')
    def test_ask_validQuestion_initialAnswer5(self, mockFunc):
        mockFunc.return_value='lab4'
        answer = self.qa.ask('Where am I?')
        self.assertEqual('lab4', answer)

    @requirements(['#0023'])
    @patch('pyTona.answer_funcs.get_git_url')
    def test_ask_validQuestion_initialAnswer6(self, mockFunc):
        mockFunc.return_value = 'http://github.com/gvillanueva/CST236'
        answer = self.qa.ask('Where are you?')
        self.assertEqual('http://github.com/gvillanueva/CST236', answer)

    class mockSocket():
        def __init__(self):
            self.ip = None
            self.port = None
            self.message = None
        def connect(self, (ip, port)):
            self.ip = ip
            self.port = port
        def send(self, message):
            self.message = message
        def recv(self, a):
            return 'Huey$Dewey$Louie'
        def close(self):
            pass

    class mockSocketNoReponse(mockSocket):
        def recv(self, a):
            return None

    @requirements(['#0024', '#0026'])
    @patch('socket.socket')
    def test_ask_validQuestion_initialAnswer7(self, patchedSocket):
        patchedSocket.return_value = self.mockSocket()
        answer = self.qa.ask('Who else is here?')
        self.assertListEqual(['Huey', 'Dewey', 'Louie'], answer)

    @requirements(['#0025'])
    @patch('socket.socket')
    def test_ask_initialAnswer7_connectionInfoAndMessageReqs(self, patchedSocket):
        mockObj = self.mockSocket()
        patchedSocket.return_value = mockObj
        answer = self.qa.ask('Who else is here?')
        self.assertEqual('192.168.64.3', mockObj.ip)
        self.assertEqual('1337', mockObj.port)
        self.assertEqual('Who?', mockObj.message)

    @requirements(['#0027'])
    @patch('socket.socket')
    def test_ask_initialAnswer7_noResponse(self, patchedSocket):
        patchedSocket.return_value = self.mockSocketNoReponse()
        answer = self.qa.ask('Who else is here?')
        self.assertEqual('IT\'S A TRAAAPPPP', answer)

    @requirements(['#0028'])
    def test_ask_initialAnswer8_immediateResponse(self):
        answer = self.qa.ask('What is the 1 digit of the Fibonacci sequence?')
        self.assertEqual(1, answer)

    @requirements(['#0029'])
    @patch('random.randint')
    def test_ask_initialAnswer8_Thinking(self, mockRandint):
        mockRandint.return_value = 7
        answer = self.qa.ask('What is the 200 digit of the Fibonacci sequence?')
        self.assertEqual('Thinking...', answer)

    @requirements(['#0029'])
    @patch('random.randint')
    def test_ask_initialAnswer8_OneSecond(self, mockRandint):
        mockRandint.return_value = 4
        answer = self.qa.ask('What is the 200 digit of the Fibonacci sequence?')
        self.assertEqual('One second', answer)

    @requirements(['#0029'])
    @patch('random.randint')
    def test_ask_initialAnswer8_CoolYourJets(self, mockRandint):
        mockRandint.return_value = 0
        answer = self.qa.ask('What is the 200 digit of the Fibonacci sequence?')
        self.assertEqual('cool your jets', answer)

    @requirements(['#0008', '#0018'])
    def test_ask_validQuestion_initialAnswer2(self):
        answer = self.qa.ask('How many seconds since?')
        result = datetime.now() - datetime.combine(date.today(), time(12))
        # self.assertEqual(result.seconds, answer)
        self.assertEqual('42 seconds', answer)

    @requirements(['#0030'])
    def test_ask_invalidQuestion_notAString(self):
        self.assertRaises(Exception, self.qa.ask, 1233)

    @requirements(['#0031'])
    def test_ask_invalidQuestion_tooManyExtraParams(self):
        self.assertRaises(Exception, self.qa.ask, 'Why don\'t 21 you shutdown?')

    @requirements(['#0022'])
    def test_ask_whereAmI_notInAGitRepo(self):
        cwd = os.getcwd()
        os.chdir('..')
        answer = self.qa.ask('Where am I?')
        self.assertEqual('Unknown', answer)
        os.chdir(cwd)

    @requirements(['#0023'])
    def test_ask_whereAreYou_notInAGitRepo(self):
        cwd = os.getcwd()
        os.chdir('..')
        answer = self.qa.ask('Where are you?')
        self.assertEqual('Unknown', answer)
        os.chdir(cwd)

    class mockProcess():
        def communicate(self):
            return [None]

    @requirements(['#0022'])
    @patch('subprocess.Popen')
    def test_ask_whereAmI_outputIsNone(self, mockObj):
        mockObj.return_value = self.mockProcess()
        answer = self.qa.ask('Where am I?')
        self.assertEqual('Unknown', answer)

    @requirements(['#0023'])
    @patch('subprocess.Popen')
    def test_ask_whereAreYou_outputIsNone(self, mockObj):
        mockObj.return_value = self.mockProcess()
        answer = self.qa.ask('Where are you?')
        self.assertEqual('Unknown', answer)

    @requirements(['#0032'])
    def test_stop_fibonacciSeqFinder(self):
        answer = self.qa.ask('What is the 5 digit of the Fibonacci sequence?')
        self.assertNotEqual(5, answer) #needs time to find the value
        if isinstance(pyTona.answer_funcs.seq_finder, FibSeqFinder):
            pyTona.answer_funcs.seq_finder.stop()
        sleepytime.sleep(5) #wait for the value
        answer = self.qa.ask('What is the 5 digit of the Fibonacci sequence?')
        self.assertNotEqual(5, answer) #Answer should not be found since we stopped the thread
        pass

    def tearDown(self):
        if isinstance(pyTona.answer_funcs.seq_finder, FibSeqFinder):
            pyTona.answer_funcs.seq_finder.stop()