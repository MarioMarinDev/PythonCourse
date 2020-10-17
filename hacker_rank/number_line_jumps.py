#!/bin/python3

"""
    Page: https://www.hackerrank.com/challenges/kangaroo/problem
"""

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (x1 > x2 and v1 >= v2) or (x2 > x1 and v2 >= v1):
        return "NO"
    iterations = 0
    while x1 != x2:
        x1 += v1
        x2 += v2
        iterations += 1
        if iterations >= 10000:
            return "NO"
    return "YES"


if __name__ == '__main__':
    result = kangaroo(1571, 4240, 9023, 4234)
    print(result)
