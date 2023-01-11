"""Problem 76 - Counting summations"""

# def part(n, m):
#     if n <= 1:
#         return 1
#     if m > n:
#         return part(n, n)
#     s = 0
#     for k in range(1, m + 1):
#         s += part(n - k, k)
#     return s


# print(part(100, 99))

target = 5
partitions = [1] + [0] * target
for i in range(1, target + 1):
    for j in range(i, len(partitions)):
        partitions[j] += partitions[j - i]
print(partitions[target] - 1)
