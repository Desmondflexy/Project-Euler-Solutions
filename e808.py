# Problem 808 - Reversible prime squares

from myfunc import isprime, primes
from math import sqrt
from time import time

tic = time()
P = primes(31100101)
print(f'Primes table generated in {time() - tic} seconds')
s = 0
k = 0
for i in P:
    n = i*i
    m = int(str(n)[::-1])
    if (n != m):
        r = sqrt(m)
        if r == int(r) and isprime(r):
            k += 1
            s += n
            print(k, n, int(sqrt(n)))
        if k == 50:
            break
print(s)

print(f'Run time: {time() - tic} seconds')
