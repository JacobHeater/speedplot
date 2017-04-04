import require

JsonHelper = require('../helpers/jsonhelper.py').JsonHelper


class BaseEntity(object):
    def __init__(self):
        object.__init__(self)

    def toJson(self):
        return JsonHelper.serialize(self)