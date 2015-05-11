import time
from unittest import TestCase
from ReqTracer import requirements
from pyTona.main import Interface
import pyTona.answer_funcs
import os
import string
import random
import threading

class TestReadDataPerformance(TestCase):
    def setUp(self):
        self.qa = Interface()

    def setUpDefaultData(self):
        with open('data.txt', 'w') as f:
            f.write("How do you know so much about swallows?")

    def setUpBigRandomData(self):
        with open('data.txt', 'w') as f:
            for i in xrange(1048576):
                f.write(random.choice(string.lowercase))

    def deleteData(self):
        try:
            os.remove('data.txt')
        except OSError:
            pass

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

    @requirements(['#0040'])
    def test_read_data(self):
        self.setUpDefaultData()
        answer = self.qa.ask('What are the contents of data.txt?')
        self.assertEqual(answer, 'How do you know so much about swallows?')

    @requirements(['#0040'])
    def test_read_data_fileMissing(self):
        self.deleteData()
        answer = self.qa.ask('What are the contents of data.txt?')
        self.assertEqual(answer, 'Unknown')

    @requirements(['#0040', '#0050'])
    def test_read_data_10CharsPerSec(self):
        self.setUpDefaultData()
        start = time.clock()
        answer = self.qa.ask('What are the contents of data.txt?')
        elapsed = time.clock() - start
        perSec = len(answer) / elapsed
        self.assertGreaterEqual(perSec, 10)
        self.outputPerformanceNumber('test_read_data_10CharsPerSec', perSec)

    @requirements(['#0040', '#0050'])
    def test_read_data_10CharsPerSec_underStress(self):
        self.setUpBigRandomData()


    def tearDown(self):
        self.deleteData()