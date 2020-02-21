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
from typing import Union, List


class MaxHeap:
    def __init__(self, initial_size=10):
        self.complete_binary_tree = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go
        self.initial_size = initial_size

    def __str__(self):
        return str([node for node in self.complete_binary_tree])

    def __len__(self):
        return self.next_index

    def __iter__(self):
        return self.complete_binary_tree.__iter__()

    @staticmethod
    def _double_capacity_size(input: list) -> Union[List]:
        if len(input) == 0: return list()
        return [None for _ in range(2 * len(input))]

    def size(self):
        return self.next_index

    def is_empty(self):
        return self.size() == 0

    def insert(self, data):
        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.complete_binary_tree):
            temp = self.complete_binary_tree
            self.complete_binary_tree = self._double_capacity_size(temp)
            self.complete_binary_tree[:len(temp)] = temp
            # self.complete_binary_tree = [None for _ in range(2 * len(self.complete_binary_tree))]
            #
            # for index in range(self.next_index):
            #     self.complete_binary_tree[index] = temp[index]

        # insert element at the next index
        self.complete_binary_tree[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.complete_binary_tree[0]
        last_element = self.complete_binary_tree[self.next_index]

        # place last element of the cbt at the root
        self.complete_binary_tree[0] = last_element

        # we do not remove the elementm, rather we allow next `insert` operation to overwrite it
        self.complete_binary_tree[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

    def _up_heapify(self):
        # print("inside heapify")
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
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.complete_binary_tree[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.complete_binary_tree[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.complete_binary_tree[right_child_index]

            # compare with left child
            if left_child is not None:
                min_element = min(parent, left_child)

            # compare with right child
            if right_child is not None:
                min_element = min(right_child, min_element)

            # check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.complete_binary_tree[left_child_index] = parent
                self.complete_binary_tree[parent_index] = min_element
                parent = left_child_index

            elif min_element == right_child:
                self.complete_binary_tree[right_child_index] = parent
                self.complete_binary_tree[parent_index] = min_element
                parent = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.complete_binary_tree[0]



def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    # what we can do is put all of the elements in the input list into a MaxHeap so the largest number is
    # the root node, then we can pop each element off one at a time and put all the even ones together and the
    # odd ones together, simple
    max_heap = MaxHeap(len(input_list))
    for item in input_list:
        max_heap.insert(item)

    first, second = '', ''
    for i in range(len(max_heap)):
        if i % 2 == 0:
            first += str(max_heap.remove())
        else:
            second += str(max_heap.remove())
    print([int(first), int(second)])
    # pass/

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]