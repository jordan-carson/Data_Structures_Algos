#!/bin/python3

import os
import sys

print(83 % 5)
print(83 % 2)
print(82 % 5)
print(73 % 5)

import math
print(round(83, 1))
#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):

    # first we iterate over the length of the grades array
    # we setup a helper variable called item which we will use as our item of interest within the for loop
    # if the item is less than or equal to 38 do nothing, so get the opposite
    # then find the items that need to be rounded up
    # here we need to use the modulus function as it can help us determine which grades need to be
    # rounded up. if we take the modulus of 83 mod 5 it returns 3, we know this is 2 away from 85 so the
    # logic we can use is subtract the result of grade mod 5 from 5, resulting with 5 - (grade mod 5)
    # now if the difference is less than 3 then round up, we can solve this by indexing our grades array
    # for that particular item -> grades i and then add the difference to the item
    # finally return the final array after rounding! Voila!

    for i in range(len(grades)):
        item = grades[i]
        if item >= 38:
            diff = 5 - (item % 5)
            if diff < 3:
                grades[i] = item + diff
    return grades



if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
    # f.write('\n'.join(map(str, result)))
    # f.write('\n')
    #
    # f.close()
