#!/bin/python3

"""
    Page: https://www.hackerrank.com/challenges/kaprekar-numbers/problem
    Help: https://www.geeksforgeeks.org/kaprekar-number/
"""

import math
import os
import random
import re
import sys

def kaprekar(n):
    square = str(pow(n, 2))
    print("{}^2 = {}".format(n, square))
    square_len = len(square)
    second_chars = math.ceil(square_len / 2)
    first_chars = square_len - second_chars
    # Get first number
    print("First chars:", first_chars)
    first_number = ""
    if first_chars != 0:
        for number in range(first_chars):
            first_number += square[number]
        print("First number:", first_number)
        first_number = int(first_number)
        if first_number == 0:
            return False
    else:
        first_number = 0
    # Get second number
    print("Second chars:", second_chars)
    second_number = ""
    for number in range(second_chars):
        second_number += square[first_chars + number]
    print("Second number:", second_number)
    second_number = int(second_number)
    if first_number + second_number == n:
        return True
    return False

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    result = ""
    for i in range(p, q + 1):
        if kaprekar(i):
            result += str(i) + " "
    if result == "":
        return "INVALID RANGE"
    return result

if __name__ == '__main__':
    result = kaprekarNumbers(1, 300)
    # result = kaprekar(9)
    print(result)
