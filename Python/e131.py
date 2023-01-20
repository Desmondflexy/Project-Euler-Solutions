from myfunc import isprime
from math import sqrt

limit = 100
p = 7
x = 2
k = 0
while p<limit:
  for n in range(1,x):
    c = x**3
    p = c/(n*n) - n
    if isprime(p):
      print(c,n,p)
      k += 1
      break
  x += 1
