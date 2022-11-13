from collection import Collection

class Point:
    def __init__(self, key, coordinates):
        self.key = key
        self.coordinates = coordinates
        self.fails = 0

        self._delta = None

    @property
    def delta(self):
        return self._delta

    @delta.setter
    def delta(self, delta):
        self._delta = delta

    def __repr__(self):
        return "{0}, d: {1} [{2}]".format(self.key, self.delta, self.coordinates)

    # @classmethod
    # def make(cls, count = 1):
    #     pass
    #
    # @classmethod
    # def make_one(cls, key):
    #     pass

class Points(Collection):
    def replace(self, point):
        self.add(point)

class Factory:
    def __init__(self, generator, delta_factory):
        self.generator = generator
        self.delta_factory = delta_factory

    def make(self, count = 1):
        points =  Points()

        for key in range(1, count + 1):
            points.add(self.one(key))

        return points

    def one(self, key):
        self.generator.point_key = key
        coordinates = self.generator.execute()

        point = Point(key, coordinates)
        point.delta = self.delta_factory.one(point)

        return point
