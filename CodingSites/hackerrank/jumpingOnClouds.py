#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    numberOfGoodClouds = 0
    canSkip = True
    count = Counter(c)
    for cloud in c:
        if c[cloud] != 1:
            numberOfGoodClouds += 1

    # if count[]
    return numberOfGoodClouds


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
