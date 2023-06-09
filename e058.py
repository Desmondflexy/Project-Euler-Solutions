"""Problem 58 - Spiral primes"""
import time

import myfunc

tic = time.time()

a = 1
k = 1  # (vertices counter)
p = 0  # (primes counter)
n = 1
R = 0.1
v = 0

while R >= 0.1:
    n += 2
    k += 4
    d = n - 1
    for i in range(1, 5):
        v = a + i * d
        if myfunc.isprime(v):
            p += 1
    a = v
    R = p / k
    # print(n, p, k, R)
    if R < 10 / 100:
        break
print(n)
toc = time.time()
print('Time elapsed:', toc - tic)
