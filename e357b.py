from myfunc import isprime
from math import sqrt
from time import time

def isvalid(n):
  for d in range(1,int(sqrt(n))+1):
    if n%d==0:
      if not(isprime(d+n//d)): return False
  return True

start = time()
limit = 1000000
s = 1
for n in range(2,limit+1,4):
  if isvalid(n):
    s += n
print(s)
stop = time()
print('time elapsed is ',stop-start)

