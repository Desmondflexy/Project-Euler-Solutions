"""
Problem 37 - Truncatable primes
"""
from math import sqrt


def isprime(n):
    """Primality testing"""
    if n < 0: return print('input is negative')
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    for f in range(5, int(sqrt(n)) + 1, 6):
        if n % f == 0 or n % (f + 2) == 0: return False
    return True


(n, count, s) = (11, 0, 0)
while count < 11:
    if isprime(n):
        a = str(n)
        k = 1
        for i in range(1, len(a)):
            nleft = int(a[i:])
            nright = int(a[:i])
            if isprime(nleft) and isprime(nright):
                k += 1
            else:
                break
        if k == len(a):
            s += n
            count += 1
            print(n, count)
    n += 2
print(s)
