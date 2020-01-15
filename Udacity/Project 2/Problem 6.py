class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.num_elements += 1
            return

        self.tail.next = new_node
        self.tail = self.tail.next
        self.num_elements += 1

    def to_list(self):
        return [i for i in self]


def union(list1, list2): pass


def intersection(list1, list2): pass


if __name__ == '__main__':
    items = list(range(1, 20, 1))
    ll = LinkedList()
    for item in items:
        ll.append(item)

    print(ll.to_list())
