"""
Problem 99 - Largest exponential
"""
from math import log
from time import time

tic = time()
with open("p099_base_exp.txt") as book:
    max_ab = 0
    n_line = 0
    n = 1
    for line in book:
        x = line.strip().split(',')
        (a, b) = (int(i) for i in x)
        ab = b * log(a)
        if ab > max_ab:
            max_ab = ab
            n_line = n
        n += 1

print(n_line)
print(f'time elapsed: {time() - tic}')
