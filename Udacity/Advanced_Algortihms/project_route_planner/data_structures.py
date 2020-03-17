from typing import Union


class Node:
    def __init__(self, element, priority: Union[int, float]):
        self.element = element
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority


class PriorityQueue:
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, element, priority):
        node = Node(element, priority)
        if self.size() == 0:
            self.queue.append(node)
        else:
            added = False
            for i, item in enumerate(self.queue):
                if node < item:
                    # nodes priority is less than the items priority,
                    # add the item one element before, enumerate will help us find the right index
                    self.queue.insert(i, node)
                    added = True
                    break
                # else:
                #     self.queue.append(node)
            if added is False:
                # there are no elements that are greater than this, thus we add it to the end of the queue
                self.queue.append(node)

    def dequeue(self):
        return self.queue.pop(0)

    def pop_item(self):
        popped_item = self.dequeue()
        return popped_item.element, popped_item.priority

    def __str__(self):
        return ''.join([
            str(i) + ' - ' + str(item.priority) + ' - ' + str(item.element) + ' - ' + '\n'
            for i, item in enumerate(self.queue)
        ])
