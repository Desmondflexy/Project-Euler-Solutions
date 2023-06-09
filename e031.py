"""
Problem 31: Coin sums
"""

import time

tic = time.time()
n = 0
m = 200
for k200 in range(m // 200 + 1):
    for k100 in range(m // 100 + 1):
        for k50 in range(m // 50 + 1):
            for k20 in range(m // 20 + 1):
                for k10 in range(m // 10 + 1):
                    for k5 in range(m // 5 + 1):
                        for k2 in range(m // 2 + 1):
                            for k1 in range(m + 1):
                                if sum([k1, 2 * k2, 5 * k5, 10 * k10,
                                        20 * k20, 50 * k50, 100 * k100,
                                        200 * k200]) == 200:
                                    n += 1
                                    # print([k200,k100,k50,k20,k10,k5,k2,k1])
print(n)
toc = time.time()
print(toc - tic)
input('Press ENTER key to exit.')
