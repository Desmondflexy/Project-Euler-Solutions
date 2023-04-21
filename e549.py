# Problem 549 - Divisibility of factorials

import math


def s(k):
    m = 1
    while True:
        if math.factorial(m) % k == 0:
            break
        m += 1
    return m


def S(n):
    c = 0
    for k in range(2, n + 1):
        c += s(k)
    return c


print(S(int(1e4)))

# taking forever
