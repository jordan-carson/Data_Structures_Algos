"""
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum.
Return these two numbers. You can assume that all array elements are in the range [0, 9].
The number of digits in both the numbers cannot differ by more than 1.
You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31].
In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
"""


class CustomHeap:
    def __init__(self, initial_size=10, heap_property=max):
        self.complete_binary_tree = [None for _ in range(initial_size)]
        self.next_index = 0

        self.heap_property = heap_property

    def __str__(self):
        return str([node for node in self.complete_binary_tree])

    def __len__(self):
        return self.size()

    def size(self):
        return self.next_index

    def insert(self, data):
        if self.next_index == len(self.complete_binary_tree):
            newArray = [None for _ in range(len(self.complete_binary_tree) * 2)]
            newArray[:len(self.complete_binary_tree)] = self.complete_binary_tree
            self.complete_binary_tree = newArray
        self.complete_binary_tree[self.next_index] = data
        self._up_heapify()
        self.next_index += 1

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.complete_binary_tree[0]
        last_element = self.complete_binary_tree[self.next_index]

        self.complete_binary_tree[0] = last_element

        self.complete_binary_tree[self.next_index] = None
        self._down_heapify()

        return to_remove

    def _up_heapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.complete_binary_tree[parent_index]
            child_element = self.complete_binary_tree[child_index]

            if parent_element < child_element:
                self.complete_binary_tree[parent_index] = child_element
                self.complete_binary_tree[child_index] = parent_element
                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        """
        Modifying _down_heapify to provide us with a a MaxHeap Property
        @return:
        """
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.complete_binary_tree[parent_index]
            left_child = None
            right_child = None

            max_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.complete_binary_tree[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.complete_binary_tree[right_child_index]

            # compare with left child
            if left_child is not None:
                max_element = self.heap_property(parent, left_child)

            # compare with right child
            if right_child is not None:
                max_element = self.heap_property(right_child, max_element)

            # check if parent is rightly placed
            if max_element == parent:
                return

            if max_element == left_child:
                self.complete_binary_tree[left_child_index] = parent
                self.complete_binary_tree[parent_index] = max_element
                parent = left_child_index

            elif max_element == right_child:
                self.complete_binary_tree[right_child_index] = parent
                self.complete_binary_tree[parent_index] = max_element
                parent = right_child_index


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is
    maximum.
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0 or input_list in [None, list()]:
        return None
    max_heap = CustomHeap(len(input_list), heap_property=max)
    for input in input_list:
        max_heap.insert(input)

    first = ''
    second = ''

    for i in range(len(max_heap)):
        if i % 2 == 0:
            first += str(max_heap.remove())
        else:
            second += str(max_heap.remove())

    return [int(first), int(second)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")



test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
