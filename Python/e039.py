"""
Problem 39: Integer right triangles
"""
from time import time

tic = time()
Plist = {}
for b in range(4, 3000):
    for a in range(1, b):
        c = (a ** 2 + b ** 2) ** (1 / 2)
        if int(c) == c:
            p = a + b + c
            if p > 1000:
                break
            if p in Plist:
                Plist[p] += 1
            else:
                Plist[p] = 1

print(max(Plist, key=Plist.get))
print(f"time elapsed: {time() - tic}")
