"""
Test coordinate: class, collection
"""
from coordinate import *

g1 = Coordinate(1, 'g1', 0.123)
print(g1)

g2 = Coordinate(2, 'g2', -0.5)
print(g2)

coord = Coordinates()
coord.add(g1)
coord.add(g2)

print(coord)

print(coord.get(2))

"""
Test generator
"""
from generator import *

print('------')

generator = GeneratorStub(1)

print(generator.execute())

"""
Test delta: class, factory
"""
from delta import *

print('------')

d1 = DeltaStub(None).calculate()
d2 = DeltaStub(None).calculate()
print(d1)
print(d2)
print(d1 > d2)
print(d1 < d2)

deltaFactory = Factory(DeltaStub)

"""
Test point: class, factory, collection
"""
from point import *

print('------')

p = Point(1, coord)
print(p)

pp = Points()

pp.add(p)

print(len(pp), pp.get(1))

print('------')

points = Factory(generator, deltaFactory).make(3)

print(len(points), points.get(1))
