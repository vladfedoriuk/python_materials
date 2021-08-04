class LRU(object):
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.vals = {}
        self.keys = []

    def set(self, key, val: object) -> None:
        self.keys.insert(0, key)
        self.vals[key] = val
        if len(self.keys) == self.capacity + 1:
            last_key = self.keys.pop(-1)
            self.vals.pop(last_key, None)

    def get(self, key) -> object:
        try:
            key_id = self.keys.index(key)
        except ValueError:
            return None
        self.keys.pop(key_id)
        self.keys.insert(0, key)
        return self.vals[key]


if __name__ == "__main__":
    cache = LRU(4)
    cache.set("a", 1)
    cache.set("b", 2)
    print(cache.keys)
    print(cache.get("a"))
    print(cache.keys)
    cache.set("c", 3)
    cache.set("d", 4)
    cache.set("e", 5)
    print(cache.get("c"))
    print(cache.keys)
