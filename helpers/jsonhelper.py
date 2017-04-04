import json

class JsonHelper:
    @staticmethod
    def serialize(obj):
        return json.dumps(obj.__dict__)

    @staticmethod
    def deserialize(str):
        return json.loads(str)