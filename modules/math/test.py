# import os, sys
#
# p = os.path.abspath('.')
# sys.path.insert(1, p)

from interval import Interval as I
from helpers import *

r = I(1, 2) + I(3, 4)
print(r)
r = I(1, 2) + 5.3
print(r)
r = 10 + I(1, 2)
print(r)

r = I(10, 20) / I(5, 1)
print(r)

print(randf(-1, 1))
