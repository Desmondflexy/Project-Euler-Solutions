"""
Problem 14 - Longest Collatz sequence
"""

from time import time

tic = time()

b = {}
for n in range(1, 1000000):
    m, a = n, 1
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        if n in b:
            a += b[n]
            break
        a += 1
    b[m] = a
print(max(b.items(), key=lambda x: x[1]))
toc = time()
print(f"Elapsed time: {toc - tic} seconds.")
