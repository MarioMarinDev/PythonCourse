#!/bin/python3

"""
  Page: https://www.hackerrank.com/challenges/compare-the-triplets/problem 
"""

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    # 
    # [5 6 7 5] [3 6 10 5]
    # [1, 1]
    lista = [0, 0] 
    for x in range(len(a)):
        if a[x] > b[x]:
            lista[0] += 1
        elif a[x] < b[x]:
            lista[1] += 1
    return lista

if __name__ == '__main__':
    # [5 6 7 5] [3 6 10 5]
    a = [5, 6, 7, 5]
    b = [3, 6, 10, 5]
    result = compareTriplets(a, b)
    print(result
