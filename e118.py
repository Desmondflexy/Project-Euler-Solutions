import myfunc as mf
from itertools import permutations
from time import time


def partitions(arr):
    """Generates all possible partitions of an array"""
    n = len(arr)
    for partition_index in range(2 ** (n - 1)):
        partition = []
        subset = ''
        for position in range(n):
            subset += str(arr[position])
            if 1 << position & partition_index or position == n - 1:
                partition.append(int(subset))
                subset = ''
        yield partition


tic = time()
n = range(1, 10)

perms = permutations(n)
perms = filter(lambda x: x[-1] % 2 != 0, list(perms))
count = 0
for perm in perms:
    sequence = partitions(perm)
    new_sequence = mf.find(sequence, lambda x: mf.isorted(x) and all(mf.isprime(i) for i in x))
    count += len(list(new_sequence))

print(f'Answer = {count}\nTime elapsed: {time() - tic} seconds')
