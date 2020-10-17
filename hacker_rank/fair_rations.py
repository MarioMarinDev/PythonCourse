#!/bin/python3

"""
    NOT OPTIMAL CODE
    Page: https://www.hackerrank.com/challenges/fair-rations/problem
"""

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    given = 0
    # print(B)
    iterations = 0
    while iterations <= 500:
        iterations += 1
        # Get number of odd numbers
        odds = []
        for index, b in enumerate(B):
            if b % 2 != 0:
                odds.append(index)
        # print("Odds:", odds)
        if len(odds) == 0:
            return given
        elif len(odds) == 1:
            return "NO"
        # Get shortest jump between odd numbers
        shortest = len(B)
        short_i = 0
        short_j = 0
        for i in range(len(odds) - 1):
            for j in range(i + 1, len(odds)):
                if abs(odds[i] - odds[j]) <= shortest:
                    short_i = odds[i]
                    short_j = odds[j]
        # print("Shortest jump:", short_i, short_j)
        # Give bread to odd numbers using the shortest jump
        for i in range(short_i, short_j):
            B[i] += 1
            B[i + 1] += 1
            given += 2

if __name__ == '__main__':
    result = fairRations([2, 3, 4, 5, 6])
    print(result)
