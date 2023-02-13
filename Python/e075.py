from math import sqrt

A = []
limit = 100
L = 12
b = 4
while L < limit:
  for a in range(3,b):
    c = sqrt(a**2 + b**2)
    if c == int(c):
      if L not in A:
        A.append(int(L))
      L = a + b + c
  b += 1
print((A))
