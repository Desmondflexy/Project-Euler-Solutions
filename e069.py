from myfunc import factor
# factor(n) lists the prime factors of n


def foo(n):
    'n/phi(n) function'
    P = set(factor(n))
    y = 1
    for i in P:
        y *= (1 - 1/i)
    return 1/y


fmax = 0
for n in range(30, 1000001, 30):
    f0 = foo(n)
    if f0 > fmax:
        fmax = f0
        nmax = n
print(nmax)

"""
I noticed that after 2 and 6, the other maximums were multiples of 30,
so I used 30 as step size to iterate faster. Runs in 0.3 seconds.

Note - The answer is simply the maximal product of consecutive primes while the
product is less than a million.
"""