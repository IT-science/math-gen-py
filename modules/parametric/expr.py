import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from modules.math.helpers import *

# from abc Import ABC

# class Expression(ABC):


class PointSeekerInitial:
    def expr(self, min, max):
        return max + randf(0, 1) * (min - max)

class PointSeeker:
    def __init__(self, points, point_key, coordinate_key):
        self.points = points
        self.point_key = point_key
        self.coordinate_key = coordinate_key

    def expr(self, min, max):
        # !!! need: currentCoord, otherCoord, min, max
        distance = randf(-1, 1)
        direction = currentCoord + distance * (currentCoord - otherCoord)

        if direction > max or direction < min:
            direction = currentCoord + (distance * -1) * (currentCoord - otherCoord)

        return direction


class DeltaCrossed:
    def __init__(self, v, z):
        self.v = v
        self.z = z

    def expr(self):
        """
        abs(wid(intr(v)) - wid(intersect(intr(v), intr(z))))
        """
        v = self.v
        z = self.z

        return abs(v.width - (v & z).width)

class DeltaNotCrossed:
    def __init__(self, v, z):
        self.v = v
        self.z = z

    def expr(self):
        """
        abs(mid(intr(v)) - mid(intr(z)))
        """
        v = self.v
        z = self.z

        return abs(v.middle - z.middle)
