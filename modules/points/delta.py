from abc import ABC, abstractmethod
import random

class Delta(ABC):
    def __init__(self, point):
        self.point = point
        self.value = self.calculate()

    # @property
    # def value(self):
    #     if not self._value:
    #         raise ValueError
    #         self._value = self.calculate()
    #
    #     return self._value

    @abstractmethod
    def calculate(self):
        pass

    def __lt__(self, d):
        return self.value < d.value

    def __gt__(self, d):
        return not self.__lt__(d)

    def __repr__(self):
        return str(self.value)

    # @classmethod
    # def one(cls, point):
    #     return cls

class Factory:
    def __init__(self, cls):
        self.cls = cls

    def one(self, point):
        return self.cls(point)

class DeltaStub(Delta):
    def calculate(self):
        return random.randint(1, 100)
