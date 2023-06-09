'''
Problem 25: 1000-digit Fibonacci number
'''

a, f = 1, 1
length = 0
nth = 2
while length<1000:
    nth = nth + 1
    a, f = f, a + f
    length = len(str(f))
print(nth)
