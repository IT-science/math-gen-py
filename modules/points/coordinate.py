from collection import Collection

class Coordinate:
    def __init__(self, key, name, value):
        """
        key - the "i" parameter in math models
        e.g. i = 1, ..., n
        """
        self.key = key
        self.name = name
        self.value = value

    def __repr__(self):
        return str(self.value)

class Coordinates(Collection):
    def __repr__(self):
        # for i in self._items:
        items = map(lambda i: str(round(i.value, 6)), self._items.values())
        return ', '.join(items)
