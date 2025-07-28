def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def summary(scores):
    average = sum(scores) / len(scores)
    maximum = max(scores)
    return (average, maximum)

from day3_utils import square

print(square(5))

import day3_utils

print(day3_utils.cube(3))