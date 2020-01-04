class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # move to the tail
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def to_list(self):
        out_list = []
        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next

        return out_list


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return


if __name__ == '__main__':
    input_list = [2,1,4,3,5]
    # Test your method here
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(-1)
    linked_list.append(0.2)

    print(linked_list.to_list())
    print("Pass" if (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")

    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(-2)
    linked_list.append(4)

    print("Going forward through the list, should print 1, -2, 4")
    node = linked_list.head
    while node:
        print(node.value)
        node = node.next

    print("\nGoing backward through the list, should print 4, -2, 1")
    node = linked_list.tail
    while node:
        print(node.value)
        node = node.previous


