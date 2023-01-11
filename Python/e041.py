"""Problem 41: Pandigital prime"""

import myfunc

for i in range(9876543211, 1234567890, -2):
    if myfunc.isprime(i):
        print(i)
