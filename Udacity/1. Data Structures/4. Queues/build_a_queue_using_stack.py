# Here is our Stack Class

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Queue:
    def __init__(self):
        # Code here
        self.in_storage = Stack()
        self.out_storage = Stack()

    def size(self):
        # Code here
        return self.in_storage.size() + self.out_storage.size()

    def enqueue(self, item):
        # Code here
        self.in_storage.push(item)

    def dequeue(self):
        # Code here
        if self.out_storage.is_empty():
            while not self.in_storage.is_empty():
                self.out_storage.push(self.in_storage.pop())
        return self.out_storage.pop()


if __name__== '__main__':
    # Setup
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test size
    print("Pass" if (q.size() == 3) else "Fail")

    # Test dequeue
    print("Pass" if (q.dequeue() == 1) else "Fail")

    # Test enqueue
    q.enqueue(4)
    print("Pass" if (q.dequeue() == 2) else "Fail")
    print("Pass" if (q.dequeue() == 3) else "Fail")
    print("Pass" if (q.dequeue() == 4) else "Fail")
    q.enqueue(5)
    print("Pass" if (q.size() == 1) else "Fail")