def get_different_number(arr):
    if len(arr) == 1 and arr[0] != 0:
        return 0

    # we are looping through the entire array
    # we then compare the index of the array to the element of that array
    # if they do not equal we return the last element of the array + 1
    s = set(arr)
    # create a set from our array
    for i in range(len(arr)):
        # loop through the entire array from index 0 to the length of the array
        if i not in s:
            # then compare the index to the items in the set, if it does not exist, return it
            return i
    # otherwise return the length of the array, and the length
    # [0, 1, 2, 3]  the length will be 4, and the 4 will be the next minimum because its not in the
    # array
    return len(arr)



