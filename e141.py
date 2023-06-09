from time import time

tic = time()
limit = 10000000
k = 0
i = 2
n = i*i
while n < limit:
    d = 2
    (q, r) = (n//d, n%d)
    while d < q:
        if d*d == q*r:
            print(n, r, d, q)
            k += n
        d += 1  
        (q, r) = (n//d, n%d)
    i += 1
    n = i*i
print(k)
toc = time()
print('Elasped time is', toc-tic)
