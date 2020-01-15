def binary_search(arr, target):
    return binary_search_func(arr, 0, len(arr) - 1, target)


def binary_search_func(arr, start_index, end_index, target):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2

    if arr[mid_index] == target:
        return mid_index
    elif arr[mid_index] > target:
        return binary_search_func(arr, start_index, mid_index - 1, target)
    else:
        return binary_search_func(arr, mid_index + 1, end_index, target)




def binary_search_recursive(alist, item):
    # Time is O(log n)
    if not alist:
        # Base Case: if list is empty
        return False

    midpoint = len(alist) // 2 # floor division
    if alist[midpoint] == item: # found it
        return True
    if item < alist[midpoint]:
        binary_search_recursive(alist[:midpoint], item)
    return binary_search_recursive(alist[midpoint + 1:], item)


def binary_search_iterative(alist, item):

    left, right = 0, len(alist)-1

    while left < right:

        midpoint = left + (right - left) // 2
        if alist[midpoint] == item:
            return True
        elif alist[midpoint] < item:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return False



def recursion_test(n):
    if n > 0:
        print(n)
        recursion_test(n - 1)



if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(binary_search(arr, 5))

    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative(testlist, 3))     # False
    print(binary_search_recursive(testlist, 13))    # True

    print(recursion_test(10))