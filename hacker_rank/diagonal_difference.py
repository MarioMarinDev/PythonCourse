#!/bin/python3

"""
  Page: https://www.hackerrank.com/challenges/diagonal-difference/problem
"""

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # 0 1 2
    # [1, 2, 3] = 3
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n = len(arr)
    # Diagonal \
    diag1 = 0
    for x in range(n):
        diag1 += arr[x][x]
    # Diagonal |
    index = len(arr[1]) - 1
    diag2 = 0
    index2 = 0
    for x in range(n):
        index2 += -1
        diag2 += arr[x][index2]
    # Resta absoluta
    return abs(diag1 - diag2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
