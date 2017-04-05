import unittest
import require
from bunch import bunchify

SpeedtestHelper = require('../helpers/speedtesthelper.py').SpeedtestHelper

class ReadTests(unittest.TestCase):
    def test_findOneByIpAddress(self):

        actual_ip = '127.0.0.1'
        result = SpeedtestHelper().lookupByIpAddress(actual_ip)
        speedtest = bunchify(result)
        
        self.assertEqual(actual_ip, speedtest.ipAddr)

    def test_findOneByDownloadSpeed(self):

        actual_speed = 100
        result = SpeedtestHelper().lookupByDownloadSpeed(actual_speed)
        speedtest = bunchify(result)

        self.assertEqual(actual_speed, speedtest.downloadSpeed)

    def test_findManyByDownloadSpeedGreaterThan50(self):

        actual_speed = 50
        result = SpeedtestHelper().lookupByDownloadSpeedGt(actual_speed)
        result_list = list(result)
        speedtests = map(lambda r: bunchify(r), result_list)

        self.assertGreater(speedtests[0].downloadSpeed, actual_speed)