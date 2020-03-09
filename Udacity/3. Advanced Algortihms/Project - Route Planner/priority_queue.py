# from queue import PriorityQueue


class Queue(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)


class Deque(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)


class BinaryHeap(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items) - 1

    def percolate_up(self):
        i = len(self)
        while i // 2 > 0:
            if self.items[i] < self.items[i // 2]:
                self.items[i // 2], self.items[i] = \
                    self.items[i], self.items[i // 2]
            i = i // 2

    def insert(self, k):
        self.items.append(k)
        self.percolate_up()

    def percolate_down(self, i):
        while i * 2 <= len(self):
            mc = self.min_child(i)
            if self.items[i] > self.items[mc]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > len(self):
            return i * 2

        if self.items[i * 2] < self.items[i * 2 + 1]:
            return i * 2

        return i * 2 + 1

    def delete_min(self):
        return_value = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.percolate_down(1)
        return return_value

    def build_heap(self, alist):
        i = len(alist) // 2
        self.items = [0] + alist
        while i > 0:
            self.percolate_down(i)
            i = i - 1


# class for Node with data and priority
class Node:

    def __init__(self, info, priority):
        self.info = info
        self.priority = priority


# class for Priority queue
class PriorityQueue:

    def __init__(self):
        self.queue = list()
        # if you want you can set a maximum size for the queue

    def insert(self, node):
        # if queue is empty
        if self.size() == 0:
            # add the new node
            self.queue.append(node)
        else:
            # traverse the queue to find the right place for new node
            for x in range(0, self.size()):
                # if the priority of new node is greater
                if node.priority >= self.queue[x].priority:
                    # if we have traversed the complete queue
                    if x == (self.size() - 1):
                        # add new node at the end
                        self.queue.insert(x + 1, node)
                    else:
                        continue
                else:
                    self.queue.insert(x, node)
                    return True

    def delete(self):
        # remove the first node from the queue
        return self.queue.pop(0)

    def show(self):
        for x in self.queue:
            print(str(x.info) + " - " + str(x.priority))

    def size(self):
        return len(self.queue)

    def empty(self):
        return self.size() == 0
