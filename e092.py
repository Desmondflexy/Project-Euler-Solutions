# Problem 92: Square digits chains

from time import time

tic = time()
# add square of digits
def f(n): return sum(int(i)**2 for i in str(n))


count = 0
for start in range(1, 10000000):
    n = start
    while not (n == 1 or n == 89):
        n = f(n)
    if n == 89:
        count += 1
print(f'Arrived at eigthy-nine {count} times.')

print(f'Time elapsed: {time() - tic} seconds')
