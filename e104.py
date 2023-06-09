"""
Problem 104: Pandigital Fibonacci ends
"""
from time import time

from myfunc import ispandigital

tic = time()
first_9digits = 0
last_9digits = 0
f = (7778742049, 12586269025)
i = 51
while not (ispandigital(first_9digits) and ispandigital(last_9digits)):
    x = sum(f)
    f = f[1], sum(f)
    s = str(x)
    last_9digits = s[-9:]
    first_9digits = s[:9]
    i += 1
k = i - 1
print(f'Answer = {k}')
print(f'time elapse: {time() - tic}')
