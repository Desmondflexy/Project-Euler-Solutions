"""Problem 95 - Amicable chains"""

import numpy as np

N = 1000000

# array with sum of divisors
sum_of_proper_divs = np.ones(N + 1, dtype=int)  
for n in range(2, N // 2 + 1):
    sum_of_proper_divs[2 * n: N + 1: n] += n

m = 0
for n in range(2, N + 1):
    if (sn := sum_of_proper_divs[n]) == 1:
        continue
    chain = [n]
    while sn <= N and sn not in chain:
        chain.append(sn)
        sn = sum_of_proper_divs[sn]
    if sn == 1 or sn >= N:
        for i in chain:
            sum_of_proper_divs[i] = 1
    elif sn == n:
        if len(chain) > m:
            print(n, chain, sn)
            m = len(chain)
        for i in chain:
            sum_of_proper_divs[i] = 1
