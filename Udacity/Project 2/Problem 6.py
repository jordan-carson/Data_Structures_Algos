class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __len__(self):
        return self.size()

    def __contains__(self, item):
        for val in self:
            if val == item:
                return True
        return False

    def union(self, other):
        """ Simple union all between self and other."""
        union = LinkedList()
        for item in self:
            if not union.__contains__(item):
                union.append(item)

        for item in other:
            if not union.__contains__(item):
                union.append(item)
        return union

    def intersection(self, other):
        """ Simple inner join between self and other. """
        new = LinkedList()
        for value in self:
            if other.__contains__(value):
                if not new.__contains__(value):
                    new.append(value)

        return new

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(list1, list2):
    """
    Union between two lists are all the unique elements in list1 and list2.
    Algo:
        Loop through both lists and append items to new LinkedList
    """
    return list1.union(list2)


def intersection(list1, list2):
    """
    An intersection between two lists are the common items between the two lists.
    Lets try to solve this in Linear time.
    @param list1:
    @param list2:
    @return:
    """
    return list1.intersection(list2)


if __name__ == '__main__':
    # Test case 1
    one = [1, 2, 3, 4]
    two = [1,5,6,7]
    print(list(set(one).intersection(two)))

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2)) # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
    print(intersection(linked_list_1, linked_list_2))

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))
