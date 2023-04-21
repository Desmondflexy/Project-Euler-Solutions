import myfunc
import time


def formlen(a, b):
    """Returns number of quadratic primes of the form n*n + a*n + b."""
    n = 0
    while True:
        p = n * n + a * n + b
        if p <= 0:
            return 0
        if myfunc.isprime(p):
            n += 1
        else:
            break
    return n


tic = time.time()
limit = 1000
blist = myfunc.primes(limit)
cmax = 0
for a in range(-limit + 1, limit, 2):
    for b in blist:
        c = formlen(a, b)
        if c > cmax:
            (A, B, cmax) = (a, b, c)
print(A * B)
toc = time.time()
print('Execution time is ' + str(toc - tic))
