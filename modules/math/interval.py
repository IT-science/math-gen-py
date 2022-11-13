class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @property
    def width(self):
        return abs(self.left - self.right)

    @property
    def middle(self):
        return (self.left + self.right) / 2

    def is_crossed(self, v):
        v = self._check_type(v)
        return self.left < v.right and self.right > v.left

    def __add__(self, v):
        v = self._check_type(v)
        return Interval(self.left + v.left, self.right + v.right)

    def __sub__(self, v):
        v = self._check_type(v)
        bounds = [self.left - v.right, self.right - v.left]
        return Interval(min(bounds), max(bounds))

    def __mul__(self, v):
        v = self._check_type(v)
        bounds = [
            self.left * v.left,
            self.left * v.right,
            self.right * v.left,
            self.right * v.right
        ]

        return Interval(min(bounds), max(bounds))

    def __truediv__(self, v):
        v = self._check_type(v)
        bounds = [
            self.left / v.left,
            self.left / v.right,
            self.right / v.left,
            self.right / v.right
        ]

        return Interval(min(bounds), max(bounds))

    def __eq__(self, v):
        v = self._check_type(v)
        return self.left == v.left and self.right == v.right

    def __and__(self, v):
        # intersection
        v = self._check_type(v)
        if not self.is_crossed(v):
            raise ValueError

        return Interval(max(self.left, v.left), min(self.right, v.right))

    def __str__(self):
        return "[{0},{1}]".format(self.left, self.right)

    def _check_type(self, val):
        if not isinstance(val, Interval):
            val = Interval(val, val)

        return val

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__
    __req__ = __eq__
    __rand__ = __and__
    __rtruediv__ = __truediv__
