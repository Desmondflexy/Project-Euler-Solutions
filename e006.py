"""
Problem 6: Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
"""

natural_numbers = range(1, 101)
a = sum([i ** 2 for i in natural_numbers])
b = sum([i for i in natural_numbers])
print(b ** 2 - a)
