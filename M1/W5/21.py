from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_value = {}                    # key -> value
        self.key_freq = {}                     # key -> frequency
        self.freq_keys = defaultdict(OrderedDict)  # frequency -> OrderedDict of keys
        self.min_freq = 0

    def get(self, key):
        if key not in self.key_value:
            return -1

        self._update_frequency(key)
        return self.key_value[key]

    def put(self, key, value):
        if self.capacity == 0:
            return

        # Update existing key
        if key in self.key_value:
            self.key_value[key] = value
            self._update_frequency(key)
            return

        # Cache full → remove LFU item
        if len(self.key_value) >= self.capacity:
            old_key, _ = self.freq_keys[self.min_freq].popitem(last=False)
            del self.key_value[old_key]
            del self.key_freq[old_key]

        # Insert new key
        self.key_value[key] = value
        self.key_freq[key] = 1
        self.freq_keys[1][key] = None
        self.min_freq = 1

    def _update_frequency(self, key):
        freq = self.key_freq[key]

        # Remove key from old frequency list
        del self.freq_keys[freq][key]

        # If old frequency list becomes empty
        if not self.freq_keys[freq]:
            del self.freq_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Increase frequency
        self.key_freq[key] = freq + 1
        self.freq_keys[freq + 1][key] = None

    def display(self):
        print("Cache:", self.key_value)
        print("Frequency:", self.key_freq)
        print()


# ---------------- Driver Code ----------------

cache = LFUCache(3)

cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")

cache.display()

print(cache.get(1))
print(cache.get(1))
print(cache.get(2))

cache.display()

cache.put(4, "D")

cache.display()