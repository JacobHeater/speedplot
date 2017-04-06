from datetime import datetime
from entities.baseentity import BaseEntity
from helpers.speedtesthelper import SpeedtestHelper

class SpeedTestResult(BaseEntity):
    def __init__(self):

        self.uploadSpeed = 0
        self.downloadSpeed = 0
        self.speedUnits = ''
        self.ipAddr = ''
        self.testDateTime = datetime.utcnow()

    def writeToDb(self):
        db = SpeedtestHelper()
        return db.addSpeedTestResult(self)