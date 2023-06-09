"""
Problem 123: Prime square remainders
"""
from time import time

from myfunc import primes

tic1 = time()
p = primes(100000)
tic2 = time()
print(f'primes generated in {tic2 - tic1} seconds')
r = 0
n = 1  # n is odd
while r < 10 ** 9:
    r = ((p[n] - 1) ** n + (p[n] + 1) ** n) % p[n] ** 2
    # print(n, r)
    n += 2

print(f'Answer = {n - 2}')
print(f'time elapsed: {time() - tic2}')
