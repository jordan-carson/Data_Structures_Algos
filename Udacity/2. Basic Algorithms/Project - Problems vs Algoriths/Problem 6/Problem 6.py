def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    Args:
       ints(list): list of integers containing one or more integers
    """
    if not isinstance(ints, list):
        raise TypeError(f'ints is not of type list, but {type(ints)}')

    if len(ints) < 1:
        return ints[0], 0

    current_max = ints[0]
    current_min = ints[0]

    for i in range(len(ints)):
        if current_max > ints[i]:
            current_max = ints[i]

        if current_min < ints[i]:
            current_min = ints[i]

    return current_max, current_min


if __name__ == '__main__':
    ## Example Test Case of Ten Integers
    import random

    # General Cases
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

    l = [i for i in range(0, 101)]
    random.shuffle(l)
    print('Pass' if ((0, 100) == get_min_max(l)) else 'Fail')

    l = [i for i in range(50, 101)]
    random.shuffle(l)
    print('Pass' if ((50, 100) == get_min_max(l)) else 'Fail')

    # Edge Cases
    l = [1] * 100
    print('Pass' if ((1, 1) == get_min_max(l)) else 'Fail')

    l = [0] * 100
    print('Pass' if ((0, 0) == get_min_max(l)) else 'Fail')

    l = [0, 0, 0, 0, 1, 0, 0, 0]
    random.shuffle(l)
    print('Pass' if ((0, 1) == get_min_max(l)) else 'Fail')
