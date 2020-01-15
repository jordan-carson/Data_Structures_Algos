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
        node = self.head
        print(f'Head = {self.head.value}, Tail={self.tail.value}', end=' ')
        # print(f'[head = {self.head.value}, tail = {self.tail.value}]', end=' ')
        while node:
            print(f'{node.value} -> ', end=" ")
            node = node.prev
        print('NULL')

    def __len__(self):
        return self.num_elements

    def size(self):
        return len(self)

    def _capacity_check(self, capacity):
        if capacity <= 0: raise ValueError('Capcity must be greater than 0')

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
        if self.num_elements == self.capacity:
            self._remove_lru()
        # create a new node using our Doubly Linked List Node class
        new_node = DoubleLinkedListNode(value)
        # add the new node into our cache
        self.hash_cache[key] = new_node
        # set our new head, and increase the number of elements
        self._set_head(new_node)
        self.num_elements += 1
        # pass

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
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))
    print(our_cache.get(2))
    print(our_cache.get(9))

    print(our_cache)



if __name__ == '__main__':

    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)

    our_cache.print_elements()

    print(our_cache.get(3))       # returns 1
    our_cache.print_elements()
    #
    # our_cache.get(2)       # returns 2
    # our_cache.get(9)      # returns -1 because 9 is not present in the cache
    #
    # our_cache.set(5, 5)
    # our_cache.set(6, 6)
    # our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    # our_cache.print_elements()
    #
    # print(our_cache.get(6))
    #
    # our_cache.print_elements()
    #
    # our_cache.set(2, 10)
    #
    # (our_cache.print_elements())