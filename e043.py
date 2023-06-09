from itertools import permutations
from time import time

tic = time()
# Generates all permutations
a = permutations('0123456789')
b = [''.join(num) for num in a]

div = (2, 3, 5, 7, 11, 13, 17)
# Check triplets for divisibility
for k in range(7, 0, -1):
    b = [b[i] for i in range(len(b)) if int(b[i][k:k+3]) % div[k-1] == 0]
print(sum([int(i) for i in b]))
toc = time()
print('Execution time is', toc-tic)
