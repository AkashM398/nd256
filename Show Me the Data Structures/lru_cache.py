from collections import deque


class LRU_Cache(object):

    def __init__(self, capacity=0):
        # Initialize class variables
        self.cache = deque([], capacity)

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        try:
            return self.cache[key - 1]
        except IndexError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len([self.cache]) == self.cache.maxlen:
            self.cache.append(value)
        else:
            try:
                if self.cache[key]:
                    self.cache[key] = value
            except IndexError:
                self.cache.append(value)


    def __repr__(self):
        return self.cache.__repr__()

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(3))       # return -1
print(our_cache)