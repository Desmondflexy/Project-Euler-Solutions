"""
Problem 23
"""

from myfunc import divisors

d = lambda n: sum(divisors(n)) - n

for n in range(1, 101):
    if d(n) < n:
        print(str(n) + ' is deficient.')
    elif d(n) == n:
        print(str(n) + ' is perfect.')
    else:
        print(str(n) + ' is ABUNDANT.')
