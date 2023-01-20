from math import sqrt
from myfunc import isprime
from time import time

def pd(n):
    '''Sums the proper divisors of a number'''
    s = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            a, b = i, n//i
            s += a + b
    if a == b: s -= b
    return s - n

def achain(n, limit):
    chain = []
    i = n
    while i not in chain:
        chain.append(i)
        i = pd(i)
        if i == 0 or i > limit or i < n: return None
    return chain

tic = time()
limit = 1000000
maxlen = 0
for n in range(1, limit):
    c = achain(n, limit)
    if c != None:
        print(c)
        length = len(c)
        if length > maxlen:
            maxlen = length
            smallest = min(c)
print('Smallest member of the longest chain is', smallest)
toc = time()
print('Time elapsed is', toc - tic)
