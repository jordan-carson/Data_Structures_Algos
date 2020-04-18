#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bonAppetit function below.
# def bonAppetit(bill, k, b):
#
#     sumofbill = sum(bill)
#     for k in range(k):
#         charged = (sumofbill - )

def counter(arr):
    dict = {}
    for a in arr:
        if a in dict:
            dict[a] += 1
        else:
            dict[a] = 1

    largest = max(dict.keys())

    return dict.get(largest)


    # return dict

print(counter([3, 3, 2, 1]))


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
