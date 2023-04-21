"""
Problem 8: The four adjacent digits in the 1000-digit number
that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number
that have the greatest product. What is the value of this product?
"""

import myfunc as mf

book = open('e008.txt')
number = list(book)
book.close()

digit = [int(number[0][i]) for i in range(0, 1000)]
products = [mf.prod(digit[k:k + 13]) for k in range(0, 1000 - 13)
            if 0 not in digit[k:k + 13]]

print(max(products))
