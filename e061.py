"""
Problem 62: Cubic permutations
"""
from time import time

tic = time()
d = {}
x = 1
permutations = 5
while permutations not in [i[0] for i in d.values()]:
    p = x ** 3
    a = ''.join(sorted(str(p)))
    d.setdefault(a, [0, p])
    d[a][0] += 1  # e.g --> d = {'123': [1, p]}
    x += 1

for i in d.items():
    if i[1][0] == permutations:
        print(i[1][1])

# copied>>
# a = {}
# i = 1
# while True:
#     n3 = str(i * i * i)
#     s = ''
#     for c in '0123456789':
#         s += chr(n3.count(c))
#     a.setdefault(s, []).append(n3)
#     if len(a[s]) == 5:
#         print('Result:', a[s][0])
#         break
#     i += 1

# copied>>
# cache = {}
# n = 345
# while True:
#     sorted_nb = "".join(sorted(str(n**3)))
#     if sorted_nb not in cache:
#         cache[sorted_nb] = []
#     cache[sorted_nb].append(n ** 3)
#     if len(cache[sorted_nb]) == 5:
#         print(min(cache[sorted_nb]))
#         break
#
#     n += 1
toc = time()
print(f"Time elapsed: {toc - tic} seconds.")
