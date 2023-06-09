"""
Problem 71: Ordered fractions
"""
from time import time

tic = time()
ans = 0
limit = 1000000
(n, d) = (2, 5)
while d <= limit:
    ans = n
    (n, d) = (n + 3, d + 7)
print(ans)
toc = time()
print(f"Time elapsed: {toc - tic}")
