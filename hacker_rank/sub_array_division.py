#!/bin/python3

"""
  Page: https://www.hackerrank.com/challenges/the-birthday-bar/problem
"""

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    chocolates = 0
    for i in range(len(s) - (m - 1)):
        sum_chocolates = 0
        for j in range(m):
            sum_chocolates += s[i + j]
        if sum_chocolates == d:
            chocolates += 1
    return chocolates

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
