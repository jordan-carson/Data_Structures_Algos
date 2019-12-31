#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    # we can use the Counter dictionary from the collections library which keys are the values in the
    # list and the values are the number of occurrences
    d = Counter(ar)
    largest_key = max(Counter.keys(d))
    print(largest_key)
    # select the key's value with the max key in the d dictionary
    return d.get(largest_key)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    print(ar)
    print(Counter(ar))

    result = birthdayCakeCandles(ar)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
