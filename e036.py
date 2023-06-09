"""
Problem 36: Double-base palindrome
"""
from time import time


def ispal(n):
    """Checks if a number is palindrome"""
    return str(n) == str(n)[::-1]


def bin2(num):
    """Converts a number in base10 to base2"""
    return int(bin(num)[2:])


tic = time()
print(sum(i for i in range(1, 1000000, 2) if ispal(i) and ispal(bin2(i))))
print(time() - tic)
