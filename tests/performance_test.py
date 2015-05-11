from unittest import TestCase
from ReqTracer import requirements
from pyTona.main import Interface
import pyTona.answer_funcs
from pyTona.answer_funcs import FibSeqFinder, WoodChuck
from pyTona.question_answer import QA
import uuid
import time
import os

class TestPerformance(TestCase):
    def setUp(self):
        self.qa = Interface()
        self.testQ = 'Who was the most prolific classical composer?'
        self.testA = 'Wolfgang Amadeus Mozart'

    def outputPerformanceNumber(self, function, results):
        if not os.path.exists('results'):
            os.mkdir('results')

        outFile = os.path.join('results', '{0}.csv'.format(function))
        exists = os.path.isfile(outFile)
        with open(outFile, 'a') as f:
            if (exists):
                f.write(',{0}'.format(results))
            else:
                f.write('{0}'.format(results))

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
        self.outputPerformanceNumber('test_minimum_qa', elapsed)

    @requirements(['#0031'])
    def test_answer_storage_speed(self):
        self.qa.ask(self.testQ)
        start = time.clock()
        self.qa.teach(self.testA)
        elapsed = time.clock() - start
        self.assertLess(elapsed, 0.005)

    @requirements(['#0032'])
    def test_answer_retrieval_speed(self):
        self.qa.ask(self.testQ)
        self.qa.teach(self.testA)
        start = time.clock()
        self.qa.ask(self.testQ)
        elapsed = time.clock() - start
        self.assertLess(elapsed, 0.005)
        self.outputPerformanceNumber('test_answer_retrieval_speed', elapsed)

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
        self.outputPerformanceNumber('test_fibonacci_generation_first1000InLessThan60s', elapsed)

    @requirements(['#0035', '#0039'])
    def test_woodChuck_busyChucking(self):
        answer = self.qa.ask('How much wood could a woodchuck chuck in 10 seconds?')
        self.assertEqual(answer, 'Busy chucking')

    @requirements(['#0035', '#0040'])
    def test_woodChuck_10cords_in_10secs(self):
        answer = self.qa.ask('How much wood could a woodchuck chuck in 10 seconds?')
        while answer == 'Busy chucking':
            answer = self.qa.ask('How much wood could a woodchuck chuck in 10 seconds?')
        self.assertEqual(answer, 10)

    @requirements(['#0035', '#0041'])
    def test_woodChuck_check_every_5secs(self):
        answer = self.qa.ask('How much wood could a woodchuck chuck in 20 seconds?')
        start = time.clock()
        while answer == 'Busy chucking':
            answer = self.qa.ask('How much wood could a woodchuck chuck in 20 seconds?')
            elapsed = time.clock() - start
            if elapsed % 5 == 0:
                self.assertEqual(pyTona.answer_funcs.woodChuck.chuckedCords % 5, 0)
        self.assertEqual(answer, 20)

    @requirements(['#0036', '#0037'])
    def test_find_the_answer_returnsNone(self):
        answer = self.qa.ask('What is the answer to the ultimate question of life, the universe, and everything?')
        self.assertIsNone(answer)

    @requirements(['#0036', '#0038'])
    def test_find_the_answer_wait7500000usecs(self):
        self.qa.ask('What is the answer to the ultimate question of life, the universe, and everything?')
        time.sleep(7.5)
        answer = self.qa.ask('What is the answer to the ultimate question of life, the universe, and everything?')
        self.assertEqual(answer, 42)

    def tearDown(self):
        if isinstance(pyTona.answer_funcs.seq_finder, FibSeqFinder):
            pyTona.answer_funcs.seq_finder.stop()
            pyTona.answer_funcs.seq_finder = None

        if isinstance(pyTona.answer_funcs.woodChuck, WoodChuck):
            pyTona.answer_funcs.woodChuck.stop()
            pyTona.answer_funcs.woodChuck = None

        if  pyTona.answer_funcs.t is not None:
            pyTona.answer_funcs.t.cancel()
            pyTona.answer_funcs.t = None

        if len(pyTona.answer_funcs.predictors) > 0:
            for wp in pyTona.answer_funcs.predictors:
                wp.stop()
