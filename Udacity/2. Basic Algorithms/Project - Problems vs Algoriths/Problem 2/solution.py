# """
# Search in a Rotated Sorted Array
# You are given a sorted array which is rotated at some random pivot point.
#
# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).
#
# Example:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
#
# Here is some boilerplate code and test cases to start with:
#
#
# """
#
# def rotated_array_search(input_list, number):
#     """
#     Find the index by searching in a rotated sorted array
#
#     Args:
#        input_list(array), number(int): Input array to search and the target
#     Returns:
#        int: Index or -1
#     """
#
#     # use binary search to find the index to start
#     pivot = _binary_search(input_list, number)
#     print(pivot)
#
#     if input_list[pivot] == number:
#         return pivot
#
#     elif input_list[pivot] > number:
#         rotated_array_search(input_list[pivot:], number)
#
#     elif input_list[pivot] > number:
#         rotated_array_search(input_list[:pivot], number)
#
#     return -1
#
#
#
#
#
# def binary_search_recursive(alist, item):
#     # Time is O(log n)
#     if not alist:
#         # Base Case: if list is empty
#         return False
#
#     midpoint = len(alist) // 2 # floor division
#     if alist[midpoint] == item: # found it
#         return True
#     if item < alist[midpoint]:
#         binary_search_recursive(alist[:midpoint], item)
#     return binary_search_recursive(alist[midpoint + 1:], item)
#
#
# def _binary_search(alist, item):
#
#     left, right = 0, len(alist)-1
#
#     while left < right:
#
#         midpoint = left + (right - left) // 2
#         if alist[midpoint] == item:
#             return midpoint
#         elif alist[midpoint] < item:
#             left = midpoint + 1
#         else:
#             right = midpoint - 1
#     return -1
#
#
#
#
#
#
# def linear_search(input_list, number):
#     for index, element in enumerate(input_list):
#         if element == number:
#             return index
#     return -1
#
#
# def test_function(test_case):
#     input_list = test_case[0]
#     number = test_case[1]
#     if linear_search(input_list, number) == rotated_array_search(input_list, number):
#         print("Pass")
#     else:
#         print("Fail")
#
# test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# test_function([[6, 7, 8, 1, 2, 3, 4], 10])

x = 15


def change():
    # using a global keyword
    global x

    # increment value of a by 5
    x = x + 5
    print("Value of x inside a function :", x)


change()
print("Value of x outside a function :", x)
