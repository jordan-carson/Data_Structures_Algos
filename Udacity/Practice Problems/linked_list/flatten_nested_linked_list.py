# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)


def merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_node = list1.head
    list2_node = list2.head
    while list1_node is not None and list2_node is not None:
        if list1_node is None:
            merged.append(list2_node)
            list2_node = list2_node.next
        elif list2_node is None:
            merged.append(list1_node)
            list1_node = list1_node.next
        elif list1_node.value <= list2_node.value:
            merged.append(list1_node)
            list1_node = list1_node.next
        else:
            merged.append(list2_node)
            list2_node = list2_node.next
    return merged


class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))


if __name__ == '__main__':
    # First Test scenario
    linked_list = LinkedList(Node(1))
    linked_list.append(Node(3))
    linked_list.append(Node(5))

    nested_linked_list = NestedLinkedList(Node(linked_list))

    second_linked_list = LinkedList(Node(2))
    second_linked_list.append(4)

    nested_linked_list.append(Node(second_linked_list))

    solution = nested_linked_list.flatten()
    assert solution == [1,2,3,4,5]