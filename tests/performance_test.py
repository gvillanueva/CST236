from unittest import TestCase
from ReqTracer import requirements
from pyTona.main import Interface
import pyTona.answer_funcs
from pyTona.answer_funcs import FibSeqFinder
from pyTona.question_answer import QA
import random
import string
import uuid
import time

class TestPerformance(TestCase):
    def setUp(self):
        self.qa = Interface()
        self.testQ = 'Who was the most prolific classical composer?'
        self.testA = 'Wolfgang Amadeus Mozart'

    @requirements(['#0030'])
    def test_minimum_qa(self):
        start = time.clock()
        for x in xrange(0, 1000000):
            unique = uuid.uuid4()
            randomQuestion = 'How {0}?'.format(unique)#''.join(random.sample(s,5)))
            randomAnswer = '{0}'.format(unique)#''.join(random.sample(s,5)))
            qa = QA(randomQuestion, randomAnswer)
            self.qa.question_answers[randomQuestion] = qa
        elapsed = time.clock() - start
        pass

    @requirements(['#0031'])
    def test_answer_storage_speed(self):
        self.qa.ask(self.testQ)
        start = time.clock()
        self.qa.teach(self.testA)
        elapsed = time.clock() - start
        self.assertTrue(elapsed)
        self.assertLess(elapsed, 0.005)

    @requirements(['#0032'])
    def test_answer_retrieval_speed(self):
        self.qa.ask(self.testQ)
        self.qa.teach(self.testA)
        start = time.clock()
        self.qa.ask(self.testQ)
        elapsed = time.clock() - start
        self.assertTrue(elapsed)
        self.assertLess(elapsed, 0.005)

    @requirements(['#0033'])
    def test_stop_fibonacci_generation_after_1000(self):
        answer = self.qa.ask('What is the 1000 digit of the Fibonacci sequence?')
        while answer in ['Thinking...', 'One second', 'cool your jets']:
            answer = self.qa.ask('What is the 1000 digit of the Fibonacci sequence?')
        answer = self.qa.ask('What is the 1001 digit of the Fibonacci sequence?')
        self.assertIn(answer, ['Thinking...', 'One second', 'cool your jets'])

    @requirements(['#0034'])
    def test_fibonacci_generation_first1000InLessThan60s(self):
        answer = self.qa.ask('What is the 1000 digit of the Fibonacci sequence?')
        start = time.clock()
        while answer in ['Thinking...', 'One second', 'cool your jets']:
            answer = self.qa.ask('What is the 1000 digit of the Fibonacci sequence?')
        elapsed = time.clock() - start
        self.assertTrue(elapsed)
        self.assertLess(elapsed, 60)

    def test_woodChuck(self):
        answer = self.qa.ask('How much wood could a woodchuck chuck in 10 seconds?')

    def tearDown(self):
        if isinstance(pyTona.answer_funcs.seq_finder, FibSeqFinder):
            pyTona.answer_funcs.seq_finder.stop()
            pyTona.answer_funcs.seq_finder = None