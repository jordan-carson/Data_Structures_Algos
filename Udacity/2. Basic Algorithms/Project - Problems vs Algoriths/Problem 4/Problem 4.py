def swap(l, a, b):
    # print(f'{a} swaps with  {b}.')
    l[a], l[b] = l[b], l[a]
    return l


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    begin, middle, end = 0, 0, len(input_list) - 1

    # We want to create three pointers or indexes that will eventually
    # provide us with the ending / starting index locations of the numbers 0, 1, 2

    while middle <= end:
        if input_list[middle] == 0: # move the 0s to the front,
            swap(input_list, begin, middle)
            begin += 1
            middle += 1
        elif input_list[middle] == 1: # consider the 1s to just be where they need to be
            middle += 1
        else: # move all the two to the end
            swap(input_list, middle, end)
            end -= 1
    # print(begin, middle, end)
    print(f'The 0s begin at index {0} and end at index {begin - 1}')
    print(f'The 1s begin at index {begin} and end at index {middle -1}')
    print(f'The 2s begin at index {middle} and end at index {len(input_list) -1} or {-end}')
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])