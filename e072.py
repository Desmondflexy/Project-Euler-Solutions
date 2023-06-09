"""
Problem 72 - Counting fractions
"""
from time import time
from sympy.ntheory import sieve

tic = time()
n = 1000000
print(1 + sum(sieve.totientrange(1, n)) - 2)
toc = time()
print(f"Time elapsed: {toc - tic}")
