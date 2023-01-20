from myfunc import isprime
from time import time

def isSemiPrime(n):
  if isprime(n): return False
  i = 2
  k = 0
  while i*i <= n:
    if n%i == 0:
      k += 1
      n //= i
      if k > 1: return False
    else: i += 1
  return True

tic = time()
c = 0
for n in range(2,10**6):
  if isSemiPrime(n):
    c += 1
print(c)
toc = time()
print('Time elapsed is', toc-tic) 
