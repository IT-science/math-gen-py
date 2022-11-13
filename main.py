from modules.math.interval import Interval as I, randf
from modules.math.interval import Interval as I, randf
import random, sys

print('Start')
i1 = I(1, 2) + I(3, 4)
print(i1)
i2 = I(1, 2) + 5.3
print(i2)
i3 = 10 + I(1, 2)
print(i3)


i = I(10, 20) / I(5, 1)
print(i)

print(randf(-1, 1))
