from myfunc import factor
# Problem 47: Distinct primes factors


def factor2(n):
    newlist = []
    dum = []
    f = factor(n)
    for i in range(len(f)):
        p = f[i]
        if p not in dum:
            dum.append(p)
            newlist.append(p**f.count(p))
    return newlist


n = 2
while True:
    a = set(factor2(n))
    if len(a) == 4:
        b = set(factor2(n+1))
        if len(b) == 4 and a.intersection(b) == set():
            c = set(factor2(n+2))
            if len(c) == 4 and a.intersection(c) == set():
                d = set(factor2(n+3))
                if len(d) == 4 and a.intersection(d) == set():
                    break
    n += 1
print(n)

"""
I already had a function that returns a list of prime factors of a number but then I had to
write another factorization function to raise each prime factor to the power of the number of
times it occurs on the list, for example, factor(56) would return [8, 7] and not [2, 2, 2, 7].
"""