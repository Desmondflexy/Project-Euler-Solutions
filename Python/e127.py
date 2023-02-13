"""
Problem 127: abc-hits
"""
from math import prod, gcd

from myfunc import factor


def rad(n):
    return prod(set(factor(n)))


k = 0
c = 0
b = 2
while c < 1000:
    for a in range(1, b):
        c = a + b
        if gcd(a, b) == gcd(a, c) == gcd(b, c) == 1:
            if rad(a * b * c) < c:
                k += 1
                print(k, a, b, c)
    b += 1
print(k)
