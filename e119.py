"""
Problem 119: Digit power sum
"""


def sumdig(n):
    """Sum of digits"""
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


A = []
for b in range(2, 101):
    for p in range(2, 15):
        a = b ** p
        if sumdig(a) == b:
            A.append(a)
A.sort()
print(A[29])
