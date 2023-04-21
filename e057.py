"""Problem 57 - Square root convergents"""
import fractions as fr

ndigit = lambda num: len(str(num))
d = 2
k = 0
for i in range(1000):
    a = str(fr.Fraction(d + 1, d))
    b = a.split('/')
    (num, den) = (int(i) for i in b)
    if ndigit(num) > ndigit(den): k += 1
    d = fr.Fraction(2 * d + 1, d)
print(k)
