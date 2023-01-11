"""
Problem 7: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10001st prime number?
"""
import myfunc

(counter, n) = (1, 2)  # 1st prime number is 2
while counter < 10001:
    n += 1
    if myfunc.isprime(n):
        counter += 1
print(f"10001st prime number is {n}")
