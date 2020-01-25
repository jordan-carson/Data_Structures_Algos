class DoubleLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache:
    """
    Least Recently Used Cache

    Notes:
        While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If however,
        the entry is not found, it is known as a cache miss.

        When designing a cache, we also place an upper bound on the size of the cache. If the cache is full
        and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element,
        we use the put() operation to insert the new element. The remove operation should also be fast.

    """
    def __init__(self, capacity):
        self.capacity = capacity
        self._capacity_check(self.capacity)

        self.hash_cache = dict()
        self.num_elements = 0

        # Create the pointers
        self.head, self.tail = None, None

    def __str__(self):
        # """Taken from online, provides a nice print function."""
        # node = self.head
        # print(f'[Head = {self.head.value}, Tail={self.tail.value}]', end=' ')
        # # print(f'[head = {self.head.value}, tail = {self.tail.value}]', end=' ')
        # while node:
        #     print(f'{node} -> ', end=" ")
        #     node = node.prev
        # print('NULL')
        n = self.head
        print(f"[head={self.head.value}, end={self.tail.value}]", end=' ')
        while n is not None:
            print('%s -> ' % n.value, end='')
            n = n.prev
        print('NULL')
        return ''

    def __len__(self):
        return self.num_elements

    def size(self):
        """Return the length of the LRU"""
        return len(self)

    def _capacity_check(self, capacity):
        """If we reach capacity, should we automatically remove the least recently used?"""
        if capacity <= 0:
            raise ValueError('Capacity must be greater than 0')

    def get(self, key):
        """
        Retreive item from provided key, return -1 if it doesn't exist
        :param key:
        :return:
        """
        # if key not in self.hash_cache:
        #     return -1
        # node = self.hash_cache[key]
        # # if self.head == node: return node.value
        # self._remove_node(node)
        # self._set_head(node)
        # return node.value
        if key in self.hash_cache:
            node = self.hash_cache[key]
            self._remove_node(node)
            self._set_head(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        """
        Set the value if the key is not present in the cache. If the cache is at capcity remove the oldest
        (LRU) item
        :param key:
        :param value:
        :return:
        """
        # check if we are at capcity
        if self.num_elements > self.capacity:
            self._remove_lru()

        if key in self.hash_cache:
            node = self.hash_cache[key]
            # if the node already exists, just update the nodes value
            node.value = value
            if self.head != node:
                self.remove(node)
                self._set_head(node)
        else:
            # create a new node using our Doubly Linked List Node class
            new_node = DoubleLinkedListNode(value)
            self.hash_cache[key] = new_node
            self._set_head(new_node)
            self.num_elements += 1
        # Update the pointers
        # if key in self.hash_cache:
        #     # we neeed to update the value for an existing key in the cache using the set operation.
        #     get_node = self.hash_cache[key]
        #     get_node.value = value
        #     self.hash_cache[key] = get_node
        #     self._set_head(get_node)
        #     self.num_elements += 1
        # else:

    def _set_head(self, node):
        # if not self.head:
        #     self.head = node
        #     self.tail = node
        # else:
        #     node.prev = self.head
        #     self.head.next = node
        #     self.tail = self.head if self.head.prev is None else None
        #     self.head = node
        # self.num_elements += 1
        if self.head is None:
            self.head, self.tail = node, node
        else:
            self.head.next = node
            node.prev = self.head
            if self.head.prev is None:
                self.tail = self.head
            self.head = node

    def remove(self, node):
        self._remove_node(node)

    def _remove_node(self, node):
        if self.num_elements == 1:
            self.head, self.tail = None, None
        elif node == self.head:
            self.head = self.head.prev
            self.head.next = None
        elif node == self.tail:
            self.tail.next.prev = None
            self.tail = self.tail.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        # pass

    def _remove_lru(self):
        """
        Here we want to remove the tail from our cache as this would be the LRU based on our logic above.
        :return:
        """
        del self.hash_cache[self.tail.value]
        self._remove_node(self.tail)
        self.num_elements -= 1


if __name__ == '__main__':
    print('Test Case 1')
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))
    print(our_cache.get(2))
    print(our_cache.get(9))

    print(our_cache)

    print('Test Case 2')

    our_cache = LRU_Cache(10)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    our_cache.set(7, 7)
    our_cache.set(8, 8)
    our_cache.set(9, 9)
    our_cache.set(10, 10)
    print(our_cache)

    print(our_cache.get(1))
    print(our_cache.get(2))
    print(our_cache.get(9))
    print(our_cache.get(19))
    print(our_cache)

    print('Test Case 3')
    last_cache = LRU_Cache(20)
    for idx, num in enumerate(list(range(1, 21))):
        last_cache.set(idx, num)

    print(last_cache)
    last_cache.get(1)
    last_cache.set(1, 18)
    last_cache.set(20, 200)
    print(last_cache)

    print('Edge Cases')

    our_cache = LRU_Cache(3)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.get(1)

    print(our_cache)

    our_cache.get(2)
    print(our_cache)
    our_cache.set(1, 5)

    print(our_cache)

    our_cache = LRU_Cache(0)
    our_cache.set(1, 1)

    print(our_cache)
    # raises Error