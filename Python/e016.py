from time import time

tic = time()
print(sum([int(i) for i in str(2**1000)]))
toc = time()

print(toc - tic)
