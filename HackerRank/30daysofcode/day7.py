#!/bin/python3

import math
import os
import random
import re
import sys
n = int(input())

arr = str(input()).split(" ")
arr.reverse()

for num in arr:
    print(num + " ", end='')

# if __name__ == '__main__':
#     n = int(input())
#
#     arr = list(map(int, input().rstrip().split()))