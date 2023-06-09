from myfunc import primes
from time import time

def factor(n):
    'Returns the distinct prime factors of a number'
    i = 2
    f = []
    while i*i <= n:
        if n%i: i += 1
        else:
            n //= i
            if i not in f: f.append(i)
    if n > 1 and n not in f: f.append(n)
    return f


def M(p,q,N):
    for i in range(N,0,-1):
        if factor(i)==[p,q]: return i
    else: return 0

start = time()
N = 100
c = []
a = primes(N//2)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]*a[j]>N: break
        b = M(a[i],a[j],N)
        if b not in c: c.append(b)
print(sum(c))

stop = time()
print(stop-start)
