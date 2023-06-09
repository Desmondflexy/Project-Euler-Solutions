from myfunc import ispandigital
from time import time

tic = time()
prod = []
for a in range(1, 100):
    for b in range(100, 10000):
        c = a*b
        p = str(a)+str(b)+str(c)
        if 123456789 <= int(p) <= 987654321 and ispandigital(p):
            if c not in prod:
                prod.append(c)
        elif int(p) > 987654321:
            break
print(sum(prod))
toc = time()
print('Elapsed time is', toc - tic)
