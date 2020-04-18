import math


def root_previous(x, n):
    # n**a = x # a == 2 square root

    # ok so we need a lower and upper bound
    # https://stackoverflow.com/questions/19255120/is-there-a-short-hand-for-nth-root-of-x-in-python
    lower_bound, upper_bound = 0, x

    approx_root = (upper_bound + lower_bound) // 2.0

    while (approx_root - lower_bound >= 0.001):
        if math.pow(approx_root, n) > x:
            upper_bound = approx_root
        else:
            lower_bound = approx_root
        approx_root = (upper_bound + lower_bound) / 2
    return approx_root


def root(x, n):
    return x ** (1 / float(n))


if __name__ == '__main__':
    test_cases = [[4,2, 2.0], [27, 3, 3.0], [16, 4, 2.0], [3, 2, 1.732], [10, 3, 2.154], [160, 3, 5.429]]

    for case in test_cases:
        actual = root(case[0], case[1])
        answer = case[2]
        print('Pass' if round(actual, 3) == answer else 'Fail')












