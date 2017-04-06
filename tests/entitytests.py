import unittest
from random import randint
from entities.speedtestresult import SpeedTestResult

class SpeedTestResultTest(unittest.TestCase):
    def test_writeToDb(self):
        
        result = SpeedTestResult()

        generateSpeedInt = lambda: randint(50, 100)

        result.uploadSpeed = generateSpeedInt()
        result.downloadSpeed = generateSpeedInt()
        result.speedUnits = 'Mb/s'
        result.ipAddr = '127.0.0.1'

        result_id = result.writeToDb()

        self.assertIsNotNone(result_id)

    def test_writeToDbStatic(self):

        result = SpeedTestResult()

        result.uploadSpeed = 100
        result.downloadSpeed = 100
        result.speedUnits = 'Mb/s'
        result.ipAddr = '127.0.0.1'

        result_id = result.writeToDb()

        self.assertIsNotNone(result_id)
        