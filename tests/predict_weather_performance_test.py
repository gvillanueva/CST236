import time
from unittest import TestCase
from ReqTracer import requirements
from pyTona.main import Interface
import pyTona.answer_funcs
import os

class TestPredictWeatherPerformance(TestCase):
    def setUp(self):
        self.qa = Interface()

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

    @requirements(['#0037', '#0038'])
    def test_predict_weather_2days_validWeather(self):
        start = time.clock()
        answer = self.qa.ask('What will the weather be like in 2 days?')
        while answer == 'Forecasting...':
            try:
                answer = self.qa.ask('What will the weather be like in 2 days?')
            except Exception:# Working this way will certainly raise exceptions
                answer = 'Forecasting...'
        elapsed = time.clock() - start
        self.assertIn(answer, pyTona.answer_funcs.WeatherPredictor.weatherTypes)
        self.outputPerformanceNumber('test_predict_weather_2days_validWeather', elapsed)

    @requirements(['#0037', '#0039'])
    def test_predict_weather_2days_returnsForecasting(self):
        answer = self.qa.ask('What will the weather be like in 2 days?')
        self.assertEqual(answer, 'Forecasting...')

    @requirements(['#0037', '#0046'])
    def test_predict_weather_2days_lessThan6secs(self):
        start = time.clock()
        pyTona.answer_funcs.predict_weather(2)
        elapsed = time.clock() - start
        self.assertLess(elapsed, 6)

    @requirements(['#0037', '#0047'])
    def test_predict_weather_tooManyPredictors(self):
        for i in xrange(3):
            pyTona.answer_funcs.predict_weather(10000)
        self.assertRaises(Exception, pyTona.answer_funcs.predict_weather, 10000)

    @requirements(['#0037', '#0048', '#0049'])
    def test_predict_weather_cache_sameResult_day3(self):
        self.qa.ask('What will the weather be like in 4 days?')
        time.sleep(4)
        answer1 = self.qa.ask('What will the weather be like in 3 days?')
        answer2 = self.qa.ask('What will the weather be like in 3 days?')
        self.assertEqual(answer1, answer2)

    def tearDown(self):
        if len(pyTona.answer_funcs.predictors) > 0:
            for wp in pyTona.answer_funcs.predictors:
                wp.stop()
