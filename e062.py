"""
Problem 62: Cubic permutations
"""
from time import time
tic = time()
d = {}
x = 1
permutations = 5
while permutations not in [i[0] for i in d.values()]:
    p = x**3
    a = ''.join(sorted(str(p)))
    d.setdefault(a, [0, p])
    d[a][0] += 1  # example --> d = {'123': [1, p]}
    x += 1

for i in d.items():
    if i[1][0] == permutations:
        print(i[1][1])
toc = time()
print(f"Time elapsed: {toc - tic} seconds.")
