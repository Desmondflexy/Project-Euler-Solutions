from time import time
import math


def method1():
    count = 0
    for d in range(2, 12001):
        for n in range(1, d):
            if math.gcd(n, d) == 1:
                if 3 * n > d and 2 * n < d:
                    count += 1
    print(count)


def method2():
    a = 1/3
    b = 1/2
    count = 0
    for d in range(2, 12001):
        for n in range(int(d/3), int(d/2) + 1):
            if math.gcd(d, n) == 1:
                c = n/d
                if c > a and c < b:
                    count += 1
    print(count)


tic = time()
method2()
print(f"Time elapsed: {time() - tic} seconds")

# 37 seconds
