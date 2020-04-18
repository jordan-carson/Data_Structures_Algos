#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    # get the number of the base
    # calculate the number of blank spaces for the first row, (do we need an empty row)
    # so if we are at 1 and n = 10 then we need to print 1 '#' while also printing 9 ' '
    for i in range(1, n+1):
        print(' ' * (n-i) + '#' * i)
    # for i in range(1, n+1):
    #     print(' '*(n-i) + '#'*i)
    # [print(' '*(n-i) + '#'*i) for i in range(1,n+1)]

if __name__ == '__main__':
    n = int(input())
    staircase(n)
