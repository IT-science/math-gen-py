import random as r, sys

def v(**kwargs):
    pass

def randf(min, max, precision = 4):
    n = r.randint(min, max - 1) + r.randint(0, sys.maxsize - 1) / sys.maxsize
    if precision:
        n = round(n, precision)

    return n
