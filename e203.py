import math
from myfunc import primes
f = math.factorial

def squarefree(n):
  p = primes(int(math.sqrt(n)))
  q = [i*i for i in p]
  X = [n%i!=0 for i in q]
  return all(X)

def pascal(row):
  n = row - 1
  return [int(f(n)/f(r)/f(n-r)) for r in range(n//2 + 1)]

limit = 51
B = []
for n in range(1,limit+1):
  A = pascal(n)
  for i in A:
    if i not in B:
      B.append(i)
print(sum([i for i in B if squarefree(i)]))
