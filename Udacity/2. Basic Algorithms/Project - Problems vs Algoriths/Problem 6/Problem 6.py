def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    current_max = ints[0]
    current_min = ints[0]

    for i in range(len(ints)):
        if current_max > ints[i]:
            current_max = ints[i]

        if current_min < ints[i]:
            current_min = ints[i]

    return current_max, current_min


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

