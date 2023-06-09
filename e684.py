# Invert Digit sum
from time import time
from myfunc import fibs


def s(n):
    """returns the smallest number that has a digit sum of n"""
    return int(str(n % 9) + '9' * (n // 9))


def S(k):
    s_sum = 0
    for n in range(1, k + 1):
        # print(f'{n:>3d} -- {s(n)}')
        s_sum += s(n)
    return s_sum


def func(k):
    n = 1
    d = 0
    s_sum = 0
    while n < k:
        for i in range(1, 10):
            j = str(i) + d * '9'
            # print(f'{n:>3d} -- {j}')
            s_sum += int(j)
            n += 1
            if n > k:
                return s_sum
        d += 1


k = 20
tic = time()
print(S(k))
print(f'time elapsed: {time() - tic}')

tic = time()
print(func(k))
print(f'time elapsed: {time() - tic}')

print(fibs(90))

