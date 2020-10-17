#!/bin/python3

"""
    Not perfect code...
    Page: https://www.hackerrank.com/challenges/picking-numbers/problem
"""

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def get_frequency(a):
    frequencies = {}
    for num in a:
        if num not in frequencies:
            frequencies[num] = 1
        else:
            frequencies[num] += 1
    return frequencies

def get_max_frequency(a):
    data = get_frequency(a)
    max_frequency = 0
    for value in data.values():
        if value > max_frequency:
            max_frequency = value
    max_frequencies = []
    for key in data:
        if data[key] == max_frequency:
            max_frequencies.append(key)
    return max_frequencies

def pickingNumbers(a):
    a.sort()
    numbers = []
    for i in range(len(a) - 1):
        if abs(a[i] - a[i + 1]) <= 1:
            numbers.append(a[i])
    mode_numbers = get_max_frequency(a)
    max_value = 0
    for mode_number in mode_numbers:
        right_numbers = 0
        left_numbers = 0
        middle_numbers = 0
        for number in a:
            if number == mode_number:
                middle_numbers += 1
            if number == mode_number + 1:
                right_numbers += 1
            if number == mode_number - 1:
                left_numbers += 1
        if right_numbers >= left_numbers:
            value = middle_numbers + right_numbers
        else:
            value = middle_numbers + left_numbers
        # print(value)
        if value > max_value:
            max_value = value
    return max_value


if __name__ == '__main__':
    # data = [4,97,5,97,97,4,97,4,97,97,97,97,4,4,5,5,97,5,97,99,4,97,5,97,97,97,5,5,97,4,5,97,97,5,97,4,97,5,4,4,97,5,5,5,4,97,97,4,97,5,4,4,97,97,97,5,5,97,4,97,97,5,4,97,97,4,97,97,97,5,4,4,97,4,4,97,5,97,97,97,97,4,97,5,97,5,4,97,4,5,97,97,5,97,5,97,5,97,97,97]
    # data = [7,12,13,19,17,7,3,18,9,18,13,12,3,13,7,9,18,9,18,9,13,18,13,13,18,18,17,17,13,3,12,13,19,17,19,12,18,13,7,3,3,12,7,13,7,3,17,9,13,13,13,12,18,18,9,7,19,17,13,18,19,9,18,18,18,19,17,7,12,3,13,19,12,3,9,17,13,19,12,18,13,18,18,18,17,13,3,18,19,7,12,9,18,3,13,13,9,7]
    data = [4,2,3,4,4,9,98,98,3,3,3,4,2,98,1,98,98,1,1,4,98,2,98,3,9,9,3,1,4,1,98,9,9,2,9,4,2,2,9,98,4,98,1,3,4,9,1,98,98,4,2,3,98,98,1,99,9,98,98,3,98,98,4,98,2,98,4,2,1,1,9,2,4]
    result = pickingNumbers(data)
    print(get_frequency(data))
    print(get_max_frequency(data))
    print(result)
