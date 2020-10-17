#!/bin/python3

"""
    Page: https://www.hackerrank.com/challenges/library-fine/problem
"""

import math
import os
import random
import re
import sys

# Complete the libraryFine function below.
# x1 the day the book was returned
# x2 the day the book was due to be returned
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 < y2:
        return 0
    if y1 > y2:
        print("year")
        return 10000
    if m1 < m2:
        return 0
    if m1 > m2:
        print("month")
        return (m1 - m2) * 500
    if d1 > d2:
        print("day")
        return (d1 - d2) * 15
    return 0

if __name__ == '__main__':
    result = libraryFine(28, 2, 2015, 15, 4, 2015)
    print(result)
