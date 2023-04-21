"""
Problem 28: Number spiral diagonals
What is the sum of the numbers on the diagonals in a 1001 by 1001
spiral formed in the same way?
"""

a = 1  # (starting number)
s = a
N = 1001
for n in range(3, N + 1, 2):  # (n is spiral size)
    d = n - 1  # (arithmetic difference)
    v = [a + d, a + 2 * d, a + 3 * d, a + 4 * d]  # (vertices)
    s += sum(v)
    # print(v)
    a = v[3]
print(s)
