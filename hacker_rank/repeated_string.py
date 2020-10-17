#!/bin/python3

"""
    Page: https://www.hackerrank.com/challenges/repeated-string/problem
"""

import math
import os
import random
import re
import sys

# s = string to repeat
# n = integer
# Complete the repeatedString function below.
def repeatedString(s, n):
    s_len = len(s)
    min_full_repetitions = math.floor(n / s_len)
    a_num = 0
    for letter in s:
        if letter == "a":
            a_num += 1
    a_num = a_num * min_full_repetitions
    for i in range(n - min_full_repetitions * s_len):
        if s[i] == "a":
            a_num += 1
    return a_num


if __name__ == '__main__':
    result = repeatedString("a", 1000000000000)
    # result =  repeatedString("aba", 10)
    print(result)
