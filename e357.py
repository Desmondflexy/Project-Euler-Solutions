# Prime generating integers
from myfunc import divisors, isprime
from time import time

limit = 10000

tic = time()

print(sum([n for n in range(1, limit) if all([isprime(d + n // d) for d in divisors(n)])]))

print(f'Time elapsed: {time() - tic}')

# tic = time()
# s = 0
# for n in range(1, limit):
#     D = divisors(n)
#     if all([isprime(d + n // d) for d in D]):
#         s += n
# print(s)
# print(f'Time elapsed: {time() - tic}')

# Unable to complete for n = 100_000_000
