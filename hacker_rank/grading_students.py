#!/bin/python3

"""
  Page: https://www.hackerrank.com/challenges/diagonal-difference/problem
"""

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # [73, 67, 38, 33]
    students = len(grades)
    x = 0
    for grade in grades:
        mult5 = math.ceil(grade / 5) * 5
        if abs(grade - mult5) < 3 and mult5 >= 40:
            grades[x] = mult5
        x += 1
    return grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
