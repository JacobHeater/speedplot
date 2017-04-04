from pymongo import MongoClient

class MongHelper:
    def __init__(self):        
        self.__client = MongoClient('localhost', 5001)
        self.__db = self.__client.speedplot

    
    def addSpeedTestResult(self, result):
        #TODO: Add write to DB
        