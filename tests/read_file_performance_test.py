import time
from unittest import TestCase
from ReqTracer import requirements
from pyTona.main import Interface
import pyTona.answer_funcs
import os
import string
import random
import multiprocessing
import threading

class TestReadDataPerformance(TestCase):
    def setUp(self):
        self.qa = Interface()
        global stopEvent
        stopEvent = threading.Event()

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
        self.setUpBigRandomData()
        start = time.clock()
        answer = self.qa.ask('What are the contents of data.txt?')
        elapsed = time.clock() - start
        perSec = len(answer) / elapsed
        self.assertGreaterEqual(perSec, 10)
        self.outputPerformanceNumber('test_read_data_10CharsPerSec', perSec)

    @requirements(['#0040', '#0050'])
    def test_read_data_10CharsPerSec_underStress(self):
        self.setUpBigRandomData()
        simultaneousFiles = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt', 'g.txt', 'h.txt', 'i.txt', 'j.txt']
        pool = multiprocessing.Pool(10)# Create 10 simultaneous writers
        r = pool.map_async(bigWrites, simultaneousFiles, 1)
        try:
            r.get(1)
        except multiprocessing.TimeoutError:
            pass
        start = time.clock()
        answer = self.qa.ask('What are the contents of data.txt?')
        elapsed = time.clock() - start
        perSec = len(answer) / elapsed
        self.assertGreaterEqual(perSec, 10)
        pool.close()        # Close
        pool.terminate()    # The dang
        pool.join()         # Jobs
        global stopEvent    # Like
        stopEvent.set()     # For real
        pass

    def tearDown(self):
        self.deleteData()

def bigWrites(file):
    with open(file, 'w') as f:
        while not stopEvent.isSet():
            f.write(random.choice(string.lowercase))
