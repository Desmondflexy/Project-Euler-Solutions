"""
Problem 13: Work out the first ten digits of the sum of the
following one-hundred 50-digit numbers.
"""

large = open('e013.txt')
s = 0
for i in range(100):
    a = int(next(large).strip())
    s += a
print(str(s)[0:10])
large.close()
