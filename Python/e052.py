'Problem 52 - Permuted multiples'
import time

tic = time.time()
x = 1
while not (sorted(str(2 * x)) == sorted(str(3 * x))
           == sorted(str(4 * x)) == sorted(str(5 * x))
           == sorted(str(6 * x))):
    x += 1
print(x)
toc = time.time()
print(toc - tic)
