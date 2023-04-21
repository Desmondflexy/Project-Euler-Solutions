"""
Problem 34: Digit factorials
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial
of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import math


def sumfac(num):
    digits = [int(i) for i in str(num)]
    return sum([math.factorial(x) for x in digits])


s = 0
for n in range(3, 10000000):
    if n == sumfac(n):
        print(n)
        s += n
print(s)
