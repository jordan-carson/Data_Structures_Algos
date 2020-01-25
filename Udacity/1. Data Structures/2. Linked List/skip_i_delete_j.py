# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    if i == 0: return None
    if head is None or i < 0 or j < 0: return head

    current = head
    previous = None

    while current:
        for _ in range(1, i):
            if current is None: return
            current = current.next

            if current is None: return

        t = current.next
        for count in range(1, j + 1):
            if t is None: break
            t = t.next

        current.next = t

        # set the current pointer for next iteration
        current = t


if __name__ == '__main__':
    # helper functions for testing purpose
    def create_linked_list(arr):
        if len(arr)==0:
            return None
        head = Node(arr[0])
        tail = head
        for data in arr[1:]:
            tail.next = Node(data)
            tail = tail.next
        return head

    def print_linked_list(head):
        while head:
            print(head.data, end=' ')
            head = head.next
        print()


    def test_function(test_case):
        head = test_case[0]
        i = test_case[1]
        j = test_case[2]
        solution = test_case[3]

        temp = skip_i_delete_j(head, i, j)
        index = 0
        try:
            while temp is not None:
                if temp.data != solution[index]:
                    print("Fail")
                    return
                index += 1
                temp = temp.next
            print("Pass")
        except Exception as e:
            print("Fail")


    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    i = 2
    j = 2
    head = create_linked_list(arr)
    solution = [1, 2, 5, 6, 9, 10]
    test_case = [head, i, j, solution]
    test_function(test_case)

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    i = 2
    j = 3
    head = create_linked_list(arr)
    solution = [1, 2, 6, 7, 11, 12]
    test_case = [head, i, j, solution]
    test_function(test_case)

    arr = [1, 2, 3, 4, 5]
    i = 2
    j = 4
    head = create_linked_list(arr)
    solution = [1, 2]
    test_case = [head, i, j, solution]
    test_function(test_case)