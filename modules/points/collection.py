class Collection:
    def __init__(self):
        self._items = {};

    @property
    def items(self):
        return self._items

    def add(self, item):
        # self._items.insert(item.key, item)
        self._items[item.key] = item

    def get(self, key):
        return self._items.get(key)

    def remove(self, key):
        del self._items[key]

    def __len__(self):
        return len(self._items)

    def pluck(self, name):
        # return array_column($this->items->toArray(), $name);
        pass

    def random(self):
        # return $this->items->random();
        pass

    # def __additem__(self):
    #     pass
