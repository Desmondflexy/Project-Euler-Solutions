"""
Problem 30: Digit fifth powers
Find the sum of all the numbers that can be written as the
sum of fifth powers of their digits.
"""


def sumpow(num, p=5):
    digits = [int(i) for i in str(num)]
    return sum([x ** p for x in digits])


s = 0
for i in range(4000, 200000):
    if i == sumpow(i):
        s += i
print(s)
