from pymongo import MongoClient

class MongoHelper(object):
    def __init__(self):        
        self._client = MongoClient()
        self._db = self._client.speedplot