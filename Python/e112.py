"""
Problem 112: Bouncy numbers
"""
from time import time


def ascending(num: list):
    for i in range(1, len(num)):
        if num[i] < num[i - 1]:
            return False
    return True


def descending(num: list):
    for i in range(1, len(num)):
        if num[i] > num[i - 1]:
            return False
    return True


tic = time()

n = 100
k = 0
prop = 0
while prop < 0.99:
    x = [int(i) for i in str(n)]
    if not (descending(x) or ascending(x)):
        k += 1
    prop = k / n
    n += 1
print(f'Answer: {n - 1}')
print(f'time elapsed: {time() - tic}')
