import time
from myfunc import primes, isprime
start = time.time()
n, maxlen = 1000000, 0
Set = primes(3943)
newb = 2
for a in range(4):
    for b in range(newb, len(Set)):
        subset = Set[a:b]
        s = sum(subset)
        if isprime(s) and s < n and len(subset) > maxlen:
            length = len(subset)
            sumprime = s
            maxlen = length
            newb = b
print(sumprime)
stop = time.time()
print('Time elapse is', (stop - start), 'seconds')

# ANSWER = 997651
