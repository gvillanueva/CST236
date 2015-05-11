import time
from unittest import TestCase
from ReqTracer import requirements
from pyTona.main import Interface
import pyTona.answer_funcs
import os

class TestReadDataPerformance(TestCase):
    def setUp(self):
        self.qa = Interface()

    def setUpDefaultData(self):
        with open('data.txt', 'w') as f:
            f.write("How do you know so much about swallows?")

    def deleteData(self):
        try:
            os.remove('data.txt')
        except OSError:
            pass

    def test_read_data(self):
        self.setUpDefaultData()
        answer = self.qa.ask('What are the contents of data.txt?')
        self.assertEqual(answer, 'How do you know so much about swallows?')

    def test_read_data_fileMissing(self):
        self.deleteData()
        answer = self.qa.ask('What are the contents of data.txt?')
        self.assertEqual(answer, 'Unknown')

    def test_read_data_10CharsPerSec(self):
        self.setUpDefaultData()
        start = time.clock()
        answer = self.qa.ask('What are the contents of data.txt?')
        elapsed = time.clock() - start
        perSec = len(answer) / elapsed
        self.assertGreaterEqual(len(answer) / elapsed, 10)

    def tearDown(self):
        self.deleteData()