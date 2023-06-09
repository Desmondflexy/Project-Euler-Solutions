"""
Problem 5: Smallest multiple
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all
the numbers from 1 to 20?
"""
from time import time

tic = time()
B = list(range(1, 21))
p = 1
n = 2
while not all([elem == 1 for elem in B]):
    if any([elem % n == 0 for elem in B]):
        for index in [i for (i, x) in enumerate(B) if x % n == 0]:
            B[index] = B[index] // n
        p *= n
    else:
        n += 1
print(p)
print(f'Time elapsed: {tic - time()}')
