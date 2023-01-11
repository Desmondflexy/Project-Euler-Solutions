from time import time

tic = time()
d = {}
for startnum in range(1, 1000001):
    n = startnum
    c = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n in d:
            c += (d[n])
            break
        else:
            c += 1
    d[startnum] = c

print(max(d, key=lambda x: d[x]))
toc = time()
print(f"Elapsed time: {toc - tic} seconds.")
