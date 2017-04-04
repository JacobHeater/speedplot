import require

BaseEntity = require('./baseentity.py').BaseEntity

class SpeedTestResult(BaseEntity):
    def __init__(self):
        
        BaseEntity.__init__(self)

        self.uploadSpeed = 0
        self.downloadSpeed = 0
        self.speedUnits = ''
        self.ipAddr = ''
    