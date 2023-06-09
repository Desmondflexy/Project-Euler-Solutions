# Problem 800 - Hybrid Integers
from myfunc import primes
from time import time

tic = time()
Primes = primes(10_000_000)
print(f'Primes generated in {time() - tic} seconds.')

z = 10000
limit = z**z
flag = False
k = 0
for p in Primes:
    for q in Primes:
        if p != q:
            n = p**q * q**p
            if n > limit:
                flag = True
                break
            k += 1
            # print(f'{k :4d}: {str(n)[-10:]}')
    if flag:
        break

print(p, q, k)
