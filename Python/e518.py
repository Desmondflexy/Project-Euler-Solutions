from myfunc import primes
from time import time

tic = time()
limit = 10000
A = primes(limit)
L = len(A)
s = 0
for i in range(L - 1):
    for j in range(i + 1, L):
        c = (A[j] + 1) ** 2 / (A[i] + 1) - 1
        if c < limit:
            if c in A:
                s += A[i] + A[j] + c
        else: break

print(s)
toc = time()
print('Elapsed time is', toc - tic)
