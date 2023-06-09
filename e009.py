"""
Problem 9: Special Pythagorean Triplet
There exists exactly one Pythagorean triplet for which a+b+c = 1000.
Find the product abc.
"""
from math import sqrt

for b in range(4, 1000):
    for a in range(1, b + 1):
        c = sqrt(a ** 2 + b ** 2)
        if c == int(c) and a + b + c == 1000:
            print(a * b * int(c))
            break
