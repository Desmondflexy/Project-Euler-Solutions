import math
from time import time
import myfunc


def main1():
    A = []
    limit = 100
    L = 12
    b = 4
    while L < limit:
        for a in range(3, b):
            c = math.sqrt(a**2 + b**2)
            if c == int(c):
                if L not in A:
                    A.append(int(L))
                L = a + b + c
        b += 1
    print((A))


def main2():
    Limit = int(1.5*10**6)
    A = [0] * Limit
    n = 1
    M = math.floor(-n/2 + math.sqrt((n/2)**2 + Limit/2))

    while n < M:
        # update M
        M = math.floor(-n/2 + math.sqrt((n/2)**2 + Limit/2))

        # Make coprime sieve
        # l = length of sieve
        l = M - n
        sieve = [True]*l
        if n > 1:
            pf = myfunc.factor(n)
            for p in pf:
                for i in range(p - 1, l, p):
                    sieve[i] = False
        # delete the odd m if n is odd
        if n % 2 == 1:
            for i in range(1, l, 2):
                sieve[i] = False

        for i in range(l):
            if sieve[i]:
                # add 1 to all elements of A with index a multiple of perimeter
                m = i + n + 1
                perimeter = 2*m*(m+n)
                for p in range(perimeter - 1, Limit, perimeter):
                    A[p] = A[p] + 1
        n += 1

    print(sum([a for a in A if a == 1]))


tic = time()
main2()
print(f"Time elapsed: {time() - tic} seconds")
