#!/bin/python3

"""
    Page: https://www.hackerrank.com/challenges/day-of-the-programmer/problem
    Help: https://www.timeanddate.com/date/leapyear.html
"""

import math
import os
import random
import re
import sys


# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    feb = 28
    if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
        feb = 29
    days = 215 + feb
    day = 256 - days
    if year == 1918:
        day += 13
    return str(day) + ".09." + str(year)


if __name__ == '__main__':
    result = dayOfProgrammer(1800)
    print(result)
