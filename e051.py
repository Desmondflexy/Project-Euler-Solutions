from itertools import product
from time import time

from myfunc import primes

Primes = primes(1000)  # All primes below 1000
tic = time()


def isprime(number: int):
    for i in Primes:
        if number == i:
            return True
        if number % i == 0:
            return False
    return True


def fam(number: str):
    """Replaces the wildcard (*) in a number with the same digit to yield a prime value family."""
    f = []
    for i in range(0, 10):
        m = int(number.replace("*", str(i)))
        if len(str(m)) == 6:
            f.append(m)
    return f


def nprimes(lst: list):
    """number of primes in a list"""
    count = 0
    for i in lst:
        if isprime(int(i)):
            count += 1
    return count


def primes_only(lst: list):
    """returns a list of only primes from the original list"""
    pl = []
    for i in lst:
        if isprime(i):
            pl.append(i)
    return pl


# generate all possible n digit long wildcard patterns
allpatterns = product(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*"], repeat=6)  # trying 6 digits

# make a list containing only patterns with at least one *
patterns = []
for p in allpatterns:
    ph = "".join(list(p))
    if "*" in ph:
        patterns.append(ph)

# get number of primes in each pattern's family
for ph in patterns:
    n = nprimes(fam(ph))
    if n > 6:
        print(f"{n} primes found in {ph}. They are {primes_only(fam(ph))}")
    if n > 7:
        break

print(f'Time elapsed: {time() - tic}')
