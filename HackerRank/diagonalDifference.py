#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    primaryDiagonal = 0
    secondaryDaiagonal = 0

    # part 1 initialize two helper variables called primary and secondary diagonal
    # loop through the array all columns and rows
    # create a conditional which looks for values if they should belong to the primary
    # create a conditional which looks for values if they should belong to the secondary
    # trap the values above
    # return the absolute value of the difference between two helper variables

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                primaryDiagonal += arr[i][j]
            if i == len(arr) - j - 1:
                secondaryDaiagonal += arr[i][j]
    return abs(primaryDiagonal - secondaryDaiagonal)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
