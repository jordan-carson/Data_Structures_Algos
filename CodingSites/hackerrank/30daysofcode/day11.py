#!/bin/python3

import math
import os
import random
import re
import sys

arr = []  # Define the array

# Input elements of Matrix and put it into array
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

# print(arr)

a = []

for i in range(0, 4):
    for j in range(0, 4):
        total = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] \
                + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
        a.append(total)

print(max(a))

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
