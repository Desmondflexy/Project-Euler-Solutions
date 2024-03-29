"""
Problem 4: A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
print(max([x * y for x in range(900, 999) for y in range(900, 999) if str(x * y) == str(x * y)[::-1]]))
