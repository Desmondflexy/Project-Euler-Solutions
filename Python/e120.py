# """
# Problem 120: Square remainders
# """
#
#
# def rem(a, n):
#     rmax = 0
#     nmax = 0
#     for i in range(1, n + 1):
#         r = ((a - 1) ** i + (a + 1) ** i) % (a ** 2)
#         if r > rmax:
#             (rmax, nmax) = (r, i)
#     return rmax, nmax
#
#
# s = 0
# for a in range(3, 1001):
#     r = rem(a, 1000)
#     s += r[0]
# print(s)
#
# # not correct
