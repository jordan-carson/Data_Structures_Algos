# from unittest import
from collections import Counter
def square_digits(num):
    empty = ''
    numstr = str(num)
    for i in numstr:
        empty += str(int(i)**2)
        # print(empty)
    return int(empty)


def square_digits_theirs(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

print(square_digits(9414))