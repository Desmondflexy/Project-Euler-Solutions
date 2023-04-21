"""
Problem 21: Amicable numbers
"""
from myfunc import divisors

def sumdivs(num):
    'Sum of divisors of n minus n'
    return sum(divisors(num)) - num

S = 0
for a in range(2, 10000):
    b = sumdivs(a)
    if sumdivs(b) == a and a != b:
        S += a
print(S)
