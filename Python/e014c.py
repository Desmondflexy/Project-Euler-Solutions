from time import time
from functools import cache
from operator import itemgetter

tic = time()


@cache
def collatz_n(n: int) -> int:
    if n <= 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz_n(n // 2)
    return 1 + collatz_n((3 * n) + 1)


print(max(enumerate(collatz_n(n) for n in range(1000000)), key=itemgetter(1)))
toc = time()
print(f"Elapsed time: {toc - tic} seconds.")
