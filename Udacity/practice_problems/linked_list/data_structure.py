class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node
            return

        # move to the tail
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def to_list(self):
        new_list = list()
        node = self.head
        while node.next:
            new_list.append(node.value)
            node = node.next
        return new_list