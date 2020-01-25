import uuid
import numpy as np

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedListNaive:

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


# Solution
class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        # if input_list:
        #     for item in input_list:
        #         self.append(item)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __reversed__(self):
        return self.reverse()

    def __repr__(self):
        return str([v for v in self])

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        iter_node_A = self.head
        iter_node_B = other.head
        while iter_node_A and iter_node_B:
            if iter_node_A.data != iter_node_B.data:
                return False
            iter_node_A = iter_node_A.next
            iter_node_B = iter_node_B.next
        if not iter_node_A and not iter_node_B:
            return True
        else:
            return False

    def __len__(self):
        return self.size()

    def __getitem__(self, item):
        if not self.head:
            return None
        if item > len(self):
            raise IndexError
        else:
            node = self.head
            index = 0
            while node and index <= item:
                if index == item:
                    return node.value

                index += 1
                node = node.next
        raise IndexError    # just in case

    def __add__(self, other):
        for i in range(len(other)):
            self.append(other[i])
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def prepend(self, value):
        """ Prepend a node to the beginning of the list

        Example:
            >>> LinkedList([4, 3]).prepend(5)
            [4, 3] -> [5, 4, 3]

        Explanation: we prepend the 5 to the beginning of the list, setting the new head equal to the new value
        and swapping the head to be the next node. The head already has reference to the other existing nodes within
        the LinkedList.

        """

        if self.head is None:
            self.head = Node(value)
            return

        # set the head equal to the new Node(value)
        new_head = Node(value)

        # then set the previous head equal to the next node,
        new_head.next = self.head

        # finally change the head to the new head
        self.head = new_head

    def append(self, value):
        """ Append a node to the end of the list """
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return None

        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

        raise ValueError("Value not found in the list.")

    def remove(self, value):
        """
        Delete the first node with the desired data.
        @param value: the node.value to find
        @return: This operation doesn't need to return anything, just properly remove the given value from the
        LinkedList.
        
        Example:
            >>> LinkedList([1, 3]).remove(3)
        """
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        raise ValueError("Value not found in the list.")

    def pop(self):
        """ Return the first node's value and remove it from the list. 
        @return: the first node.value

        Example:
            >>> LinkedList([1, 3]).pop()
            >>> LinkedList([3])
        """
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next

        return node.value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if pos == 0:
            self.prepend(value)
            return

        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return

            index += 1
            node = node.next
        else:
            self.append(value)

    def size(self):
        """ Return the size or length of the linked list. """
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        """
        Translate the LinkedList into an list based data structure.
        @return: List based data structure
        """
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def to_array(self):
        """
        Translate the LinkedList into a <class 'numpy.ndarray'>, using numpy.
        @return: <numpy.ndarray>
        """
        return np.array(self.to_list())

    def reverse(self):
        new_list = self
        prev_node, next_node = None, None
        for val in linked_list:
            new_node = Node(val)
            new_node.next = prev_node
            prev_node = new_node
        new_list.head = prev_node
        return new_list

    def iscircular(self):
        """
        Determine whether the Linked List is circular.

        Returns:
           bool: Return True if the linked list is circular, return False otherwise
        """

        if self.head is None:
            return False

        slow = self.head
        fast = self.head

        while fast and fast.next:
            # slow pointer moves one node
            slow = slow.next
            # fast pointer moves two nodes
            fast = fast.next.next

            if slow == fast:
                return True

        # If we get to a node where fast doesn't have a next node or doesn't exist itself,
        # the list has an end and isn't circular
        return False


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

    # Test prepend
    linked_list_1 = LinkedList()
    linked_list_1.prepend(1)
    print(linked_list_1)
    assert linked_list_1.to_list() == [1], f"list contents: {linked_list_1.to_list()}"
    linked_list_1.append(3)
    linked_list_1.prepend(2)
    assert linked_list_1.to_list() == [2, 1, 3], f"list contents: {linked_list_1.to_list()}"
    print('Pass: LinkedList Prepend.\n' if (linked_list_1.to_list() == [2, 1, 3]) else 'False')

    # Test append
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"
    print('Pass: LinkedList Append.\n' if (linked_list.to_list() == [1, 3]) else 'False')

    # Test search
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(3)
    assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
    assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

    # Test remove
    linked_list.remove(1)
    assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

    # Test pop
    value = linked_list.pop()
    assert value == 2, f"list contents: {linked_list.to_list()}"
    assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

    # Test insert
    linked_list.insert(5, 0)
    assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(2, 1)
    assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(3, 6)
    assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

    # Test size
    assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"

    print(linked_list)
    print(reversed(linked_list))
    print(type(linked_list))
    ll2 = LinkedList()
    ll2.append(3)
    ll2.prepend(1)
    print(ll2)
    print(ll2.pop())
    print(ll2)
    new_list = LinkedList()
    alist = [1,2,3,4,5]
    for item in alist:
        new_list.append(item)

    print(alist)

    # print(type(new_list.to_array()))

    # LinkedList([1, 3]).remove(3)

    print(new_list)
    b = new_list + new_list
    print(b)

    c = b + new_list + new_list
    print(c)


