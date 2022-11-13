from abc import ABC, abstractmethod
import random as r
from coordinate import *

class Generator(ABC):
    def __init__(self, point_key):
        self.point_key = point_key

    @abstractmethod
    def execute(self):
        pass

class GeneratorStub(Generator):
    def execute(self):
        coordinates = Coordinates()
        for key in range(1, 3):
            coordinates.add(Coordinate(key, 'g' + str(key), r.random()))

        return coordinates
