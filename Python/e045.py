"""
Problem 45: Triangular, pentagonal, and hexagonal
"""
from time import time

T = lambda n: int(n * (n + 1) / 2)
P = lambda n: int(n * (3 * n - 1) / 2)
H = lambda n: n * (2 * n - 1)


def find_next(pos: tuple) -> tuple:
    """Find the next occurence of T(x) = P(y) = H(z)."""
    tic = time()
    x, y, z = (i + 1 for i in pos)
    while True:
        h = H(z)
        while P(y) <= h:
            p = P(y)
            if p == h:
                while T(x) <= p:
                    t = T(x)
                    if t == p:
                        print(f"T({x}) = P({y}) = H({z}) = {t}")
                        toc = time()
                        print(f"Time elasped: {toc - tic} seconds.")
                        return x, y, z
                    x += 1
            y += 1
        z += 1


find_next((285, 165, 143))
