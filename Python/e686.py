# Powers of Two
from math import log
from time import time


def e686():
    counter = 0
    j = 6
    while counter < 678910:
        j += 1
        if log(1.23, 10) < j * log(2, 10) - int(j * log(2, 10)) < log(1.24, 10):
            counter += 1
    print(j)


tic = time()
e686()
print(f'Elapsed time: {time() - tic}')
