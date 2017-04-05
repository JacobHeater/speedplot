import require

MongoHelper = require('./mongohelper.py').MongoHelper

class SpeedtestHelper(MongoHelper):
    def __init__(self):
        MongoHelper.__init__(self)

    @property
    def speedtests(self):
        return self._db.speedtests

    def findOne(self, query):
        return self.speedtests.find_one(query)    
    
    def find(self, query):
        return self.speedtests.find(query)

    def addSpeedTestResult(self, result):
        speedtests = self.speedtests
        return speedtests.insert_one(result.__dict__).inserted_id

    def lookupByDownloadSpeed(self, speed):
        return self.findOne({ "downloadSpeed": speed })

    def lookupByIpAddress(self, ipAddr):
        return self.findOne({ "ipAddr" : ipAddr })

    def lookupByDownloadSpeedGt(self, speed):
        return self.find({ "downloadSpeed": { "$gt": speed } })

     