class DoubleLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self):
        return str(self.value)


class LRU_Cache(object):
    def __init__(self, capacity: int):
        self._cache = dict()
        self.capacity = capacity
        self.head = DoubleLinkedListNode(0)
        self.tail = DoubleLinkedListNode(0)
        self.head.next = self.tail
        self.tail.previous = self.head

    def get(self, key):
        if key in self._cache:
            node = self._cache.get(key)
            self._remove(node)
            self._add(node)
            return node

        return -1

    def set(self, key, value):
        if key in self._cache:
            self._remove(self.cache.get(key))

        node = DoubleLinkedListNode(value)
        self._add(node)
        self._cache[key] = node

        if len(self._cache) > self.capacity:
            node = self.head.next
            self._remove(node)
            node_key = list(self._cache.keys())[list(self._cache.values()).index(node)]
            del self._cache[node_key]

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

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        return len(self._cache)

    def __repr__(self):
        cache_items = [node.value for node in self][1:-1]
        cache_items.reverse()
        return str(cache_items)


our_cache = LRU_Cache(3)
our_cache.set(1, 1)
print(our_cache)  # [1]
our_cache.set(2, 2)
print(our_cache)  # [2, 1]
our_cache.set(3, 3)
print(our_cache)  # [3, 2, 1]
our_cache.set(4, 4)
print(our_cache)  # [4, 3, 2]
our_cache.get(3)
print(our_cache)  # [3, 4, 2]
print(our_cache.get(1))  # returns -1
print(our_cache.get(2))  # returns 2
print(our_cache.get(3))  # return 3
print(our_cache.get(9))  # return -1
