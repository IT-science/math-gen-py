import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from modules.points.generator import Generator as ABC

class Generator(ABC):
    pass
