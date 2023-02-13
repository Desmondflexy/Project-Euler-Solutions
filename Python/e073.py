# """
# Problem 73 - Counting fractions in a range
# """
# import sympy
#
#
# def fareylength(n):
#     """Returns length of a farey sequence."""
#     return 1 + sum(sympy.sieve.totientrange(1, n)) - 2
#
#
# def fareyindex(h, k, n):
#     """Finds the index of h/k in a farey sequence of order-n."""
