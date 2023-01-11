'Problem 52 - Permuted multiples'
import time

tic = time.time()
x = 1
while not (sorted(list(str(2 * x))) == sorted(list(str(3 * x)))
           == sorted(list(str(4 * x))) == sorted(list(str(5 * x)))
           == sorted(list(str(6 * x)))):
    x += 1
print(x)
toc = time.time()
print(toc - tic)
