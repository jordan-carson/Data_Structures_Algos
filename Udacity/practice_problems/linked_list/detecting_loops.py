class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return


def iscircular(linked_list):

    if linked_list.head is None:
        return False

    slow = linked_list.head
    fast = linked_list.head

    while slow and fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


if __name__ == '__main__':
    list_with_loop = LinkedList([2, -1, 3, 0, 5])

    # Creating a loop where the last node points back to the second node
    loop_start = list_with_loop.head.next

    node = list_with_loop.head
    while node.next:
        node = node.next
    node.next = loop_start

    small_loop = LinkedList([0])
    small_loop.head.next = small_loop.head
    print ("Pass" if iscircular(list_with_loop) else "Fail")
    print ("Pass" if not iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")
    print ("Pass" if not iscircular(LinkedList([1])) else "Fail")
    print ("Pass" if iscircular(small_loop) else "Fail")
    print ("Pass" if not iscircular(LinkedList([])) else "Fail")
