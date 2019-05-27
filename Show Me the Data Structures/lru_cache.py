class DoubleLinkedListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class LRU_Cache(object):

    def __init__(self, capacity=0):
        # Initialize class variables
        self.capacity = capacity
        self.cache = dict()
        self.head = DoubleLinkedListNode(0, 0)
        self.tail = DoubleLinkedListNode(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            node = self.cache.get(key)
            self._refresh(node)
            return node.value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            self._remove(self.cache.get(key))
        elif len(self.cache) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]
        else:
            node = DoubleLinkedListNode(key, value)
            self._add(node)
            self.cache[key] = node

    def _add(self, node):
        last_node = self.tail.previous
        last_node.next = node
        self.tail.previous = node
        node.previous = last_node
        node.next = self.tail

    def _remove(self, node):
        previous_node = node.previous
        next_node = node.next
        previous_node.next = next_node
        next_node.previous = previous_node

    def _refresh(self, node):
        self._remove(node)
        self._add(node)


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(3))       # return -1
