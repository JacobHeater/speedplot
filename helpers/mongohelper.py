from pymongo import MongoClient

class MongoHelper(object):
    def __init__(self):        
        self._client = MongoClient('localhost', 27017)
        self._db = self._client.speedplot