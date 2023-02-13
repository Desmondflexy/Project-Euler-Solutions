"""Problem 53 - Combinatoric selctions"""
import math
import time

tic = time.time()
count = 0
for n in range(1, 101):
    for r in range(2, n - 1):
        c = math.comb(n, r)
        if c > 1000000:
            count += 1
print(count)
toc = time.time()
print('Time elapsed is', toc - tic)
