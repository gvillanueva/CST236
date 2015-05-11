import time
from unittest import TestCase
from ReqTracer import requirements
from pyTona.main import Interface
import pyTona.answer_funcs
from collections import Counter
from mock import patch, Mock

class TestPredictWeatherPerformance(TestCase):
    def setUp(self):
        self.qa = Interface()

    @requirements(['#0037', '#0038'])
    def test_predict_weather_2days_validWeather(self):
        answer = self.qa.ask('What will the weather be like in 2 days?')
        time.sleep(6)
        answer = self.qa.ask('What will the weather be like in 2 days?')
        self.assertIn(answer, pyTona.answer_funcs.WeatherPredictor.weatherTypes)

    @requirements(['#0037', '#0039'])
    def test_predict_weather_2days_returnsForecasting(self):
        answer = self.qa.ask('What will the weather be like in 2 days?')
        self.assertEqual(answer, 'Forecasting...')

    @requirements(['#0037', '#0046'])
    def test_predict_weather_2days_lessThan6secs(self):
        start = time.clock()
        pyTona.answer_funcs.predict_weather(2)
        elapsed = time.clock() - start
        self.assertTrue(elapsed)
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
