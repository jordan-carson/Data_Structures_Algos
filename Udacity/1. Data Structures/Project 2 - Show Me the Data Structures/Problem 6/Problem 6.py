class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None
        self.num_elements = 0

    def __str__(self):
        cur_head = self.head
        out_string = ''
        while cur_head:
            out_string += str(cur_head.value) + ' -> '
            cur_head = cur_head.next
        return out_string #+ 'NULL'

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __len__(self):
        return self.num_elements

    def __contains__(self, item):
        for val in self:
            if val == item: return True
        return False
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

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

    def union(self, other):
        new_list = LinkedList()
        unique = set()

        for item in self:
            if item not in unique:
                unique.add(item)

        for item in other:
            if item not in unique:
                unique.add(item)
        for item in unique:
            new_list.append(item)
        return new_list

    def intersection(self, other):
        # new_list = LinkedList()
        # for item in self:
        #     if other.__contains__(item):
        #         if not new_list.__contains__(item):
        #             new_list.append(item)

        new_list = LinkedList()
        first = set()
        second = set()

        for item in self:
            if item not in first:
                first.add(item)

        for item in other:
            if item in first:
                second.add(item)

        for item in second:
            new_list.append(item)

        return new_list

    def to_list(self):
        return [i for i in self]


def union(list1, list2):
    """
    Union between two lists are all the unique elements in list1 and list2.
    Algo:
        Loop through both lists and append items to new LinkedList
    """
    return list1.union(list2)


def intersection(list1, list2):
    """
    An intersection between two lists are the rice_notgit items between the two lists.
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


    # Test case 3
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_5.append(i)
    for i in element_2:
        linked_list_6.append(i)

    print(union(linked_list_5, linked_list_6))
    print(intersection(linked_list_5, linked_list_6))





    # Test case 4
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = [0, 1, 2, 3]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_7.append(i)
    for i in element_2:
        linked_list_8.append(i)

    print(union(linked_list_7, linked_list_8))
    print(intersection(linked_list_3, linked_list_8))


    # Test case 5
    linked_list_9 = LinkedList()
    linked_list_10 = LinkedList()

    element_1 = [1]
    element_2 = []

    for i in element_1:
        linked_list_9.append(i)
    for i in element_2:
        linked_list_10.append(i)

    print(union(linked_list_9, linked_list_10))
    print(intersection(linked_list_9, linked_list_10))