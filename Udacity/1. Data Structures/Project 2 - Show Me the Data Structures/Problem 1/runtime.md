# Problem 1
### Least-Recently Used (LRU) Cache

In this problem, the goal was to create a data
structure that had a few specific properties.

First, we need quick retrieval for the cached values. This
implies constant lookup time O(1).

To do this, I choose to use a hash map in conjunction with a DoublyLinkedList.
A hashmap is a preferred data structure because `set()` and `get()` operations both
operate in O(1) constant look-up time.

The space complexity for both `set()` and `get()` is O(n) and O(1) respectively, as
get only 1 variable is allocated, while the set method is O(n) as its as large as the
number of keys in our cache dictionary.

