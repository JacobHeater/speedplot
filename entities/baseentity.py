from abc import ABCMeta, abstractmethod

class BaseEntity(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def writeToDb(self):
        pass
    