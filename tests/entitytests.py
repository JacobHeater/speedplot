import unittest
import require
from bunch import bunchify

SpeedTestResult = require('../entities/speedtestresult.py').SpeedTestResult
JsonHelper = require('../helpers/jsonhelper.py').JsonHelper

class SpeedTestResultTest(unittest.TestCase):
    def test_toJson(self):
        
        result = SpeedTestResult()

        result.uploadSpeed = 100
        result.downloadSpeed = 100
        result.speedUnits = 'Mb/s'
        result.ipAddr = '127.0.0.1'

        json = result.toJson()
        obj = bunchify(JsonHelper.deserialize(json))

        self.assertEqual(result.uploadSpeed, obj.uploadSpeed)
        self.assertEqual(result.downloadSpeed, obj.downloadSpeed)
        self.assertEqual(result.speedUnits, obj.speedUnits)
        self.assertEqual(result.ipAddr, obj.ipAddr)

        