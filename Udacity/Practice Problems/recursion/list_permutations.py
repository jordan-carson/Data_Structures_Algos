# Code

import copy


def permute(l: list):
    """
    Return a list of permutations

    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]

    Args:
      l(list): list of items to be permuted

    Returns:
      list of permutation with each permuted item being represented by a list
    """

    list_one = sorted(l)
    list_two = l
    master = list()
    for i in list_one:
        for j in list_two:
            master.append(list([i, j]))

    return master


print(permute([1,0]))


if __name__ =='__main__':
    # Test Cases

    # Helper Function
    def check_output(output, expected_output):
        """
        Return True if output and expected_output
        contains the same lists, False otherwise.

        Note that the ordering of the list is not important.

        Examples:
            check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

        Args:
            output(list): list of list
            expected_output(list): list of list

        Returns:
            bool
        """
        o = copy.deepcopy(output)  # so that we don't mutate input
        e = copy.deepcopy(expected_output)  # so that we don't mutate input

        o.sort()
        e.sort()
        return o == e


    print("Pass" if (check_output(permute([]), [[]])) else "Fail")
    print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
    print("Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
    print("Pass" if (check_output(permute([0, 1, 2]),
                                  [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")

    from itertools import permutations

    sample = [ch for ch in 'abcd'] #.split()
    print(sample)
    print(len(list(permutations(sample))))