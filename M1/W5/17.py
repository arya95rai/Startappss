from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)

        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value

    def get(self, key):
        if key not in self.cache:
            return -1

        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def display(self):
        print(self.cache)


# ---------------- Driver Code ----------------

cache = LRUCache(3)

cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")
cache.display()

print(cache.get(2))
cache.display()

cache.put(4, "D")
cache.display()

print(cache.get(1))

cache.put(5, "E")
cache.display()