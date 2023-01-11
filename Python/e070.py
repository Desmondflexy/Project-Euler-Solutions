"""
Problem 70 - Totient permuation
"""
from sympy import totient


def num2array(num):
    """Converts the digits of num to array"""
    return [int(i) for i in str(num)]


def isperm(x, y):
    """Returns True if list x is a permutation of list y"""
    x.sort()
    y.sort()
    return x == y


xmin = 999999
nmin = 0
for n in range(2, 10 ** 7):
    m = totient(n)
    x0 = n / m
    if x0 < xmin:
        if isperm(num2array(n), num2array(m)):
            xmin = x0
            nmin = n
print(nmin)
