# Problem 45: Triangular, pentagonal, and hexagonal
from time import time

tic = time()
def T(n): return int(n * (n + 1) / 2)
def P(n): return int(n * (3 * n - 1) / 2)
def H(n): return n * (2 * n - 1)


def find_next(pos: tuple) -> tuple:
    """Find the next occurence of T(x) = P(y) = H(z)."""
    x, y, z = (i + 1 for i in pos)
    while True:
        h = H(z)
        while P(y) <= h:
            p = P(y)
            if p == h:
                while T(x) <= p:
                    t = T(x)
                    if t == p:
                        return x, y, z
                    x += 1
            y += 1
        z += 1


print(f'Answer: {T(find_next((285, 165, 143))[0])}')
print(f"Time elasped: {time() - tic :.4f} seconds.")
