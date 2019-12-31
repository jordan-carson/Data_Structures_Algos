#!/bin/python3

import math
import os
import random
import re
import sys


# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.

def isOdd(n):
    return n % 2 != 0


def isEven(n):
    return n % 2 == 0


def solution(inp):
    N = inp
    if isOdd(N):
        print('Weird')
    elif isEven(N) and N >= 2 and N <= 5:
        print('Not Weird')
    elif isEven(N) and N >= 6 and N <= 20:
        print('Weird')
    elif isEven(N) and N > 20:
        print('Not Weird')


if __name__ == '__main__':
    N = int(input())

    solution(N)
