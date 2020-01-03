class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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
        new_list = list()
        node = self.head
        while node is not None:
            new_list.append(node.value)
            node = node.next
        return new_list


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