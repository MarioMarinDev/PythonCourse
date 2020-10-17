#!/bin/python3

"""
    Page: https://www.calculatorsoup.com/calculators/math/factors.php
    Help: https://www.calculatorsoup.com/calculators/math/factors.php
"""

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getFactors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def getTotalX(a, b):
    all_numbers = set(a + b)
    aFactors = []
    bFactors = []
    for i in range(max(all_numbers) + 1):
        # First condition
        iFactors = getFactors(i)
        aFactor = True
        for aNum in a:
            if aNum not in iFactors:
                aFactor = False
        if aFactor:
            aFactors.append(i)
        # Second condition
        bFactor = True
        for bNum in b:
            if i not in getFactors(bNum):
                bFactor = False
        if bFactor:
            bFactors.append(i)
    between = 0
    for num in aFactors:
        if num in bFactors:
            between += 1
    return between

if __name__ == '__main__':
    result = getTotalX([1], [100])
    # result = getTotalX([3, 4], [24, 48])
    print("Result:", result)

