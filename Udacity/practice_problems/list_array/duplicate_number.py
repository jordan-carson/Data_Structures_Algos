def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """

    set_of = set()

    for i in arr:
        if i in set_of:
            return i
        set_of.add(i)
    return None


print(duplicate_number([1, 2, 3, 1]))