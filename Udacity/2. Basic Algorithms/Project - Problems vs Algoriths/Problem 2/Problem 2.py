def rotated_array_search(input_list, number):
    return _rotated_array_search(input_list, 0, len(input_list) - 1, number)


def _rotated_array_search(input_list, left, right, number):
    if left > right:
        return -1

    mid_index = (left + right) // 2
    mid_element = input_list[mid_index]

    if input_list[mid_index] == number:
        return mid_index

    # left to the mid element
    if input_list[left] <= mid_element:
        if input_list[left] <= number <= mid_element:
            # search the left side of the input list
            return _rotated_array_search(input_list, left, mid_index - 1, number)
        return _rotated_array_search(input_list, mid_index + 1, right, number) # search the right

    if mid_element <= number <= input_list[right]:
        # search the right side of the input list
        return _rotated_array_search(input_list, mid_index + 1, right, number)
    return _rotated_array_search(input_list, left, mid_index - 1, number)   # search the left


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])