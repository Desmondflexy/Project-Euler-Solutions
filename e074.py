from math import factorial
from time import time


def sumfac(n):
    """Sum of factorial of digits of n."""
    return sum([factorial(int(i)) for i in str(n)])


def length(startnum):
    """Returns length of digit factorial chain."""
    c = [startnum]
    n = sumfac(startnum)
    while n not in c:
        c.append(n)
        n = sumfac(n)
    return len(c)


tic = time()
k = 0
for N in range(1, 1000000):
    if length(N) == 60:
        k += 1
print(k)
toc = time()
print(f'Time elapsed: {toc - tic}')
# Ans = 402, 79sec
