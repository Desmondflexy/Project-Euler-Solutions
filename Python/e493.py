import math

p = math.comb(60, 20) / math.comb(70, 20)
ans = 7 * (1 - p)
print(f'{ans:.9f}')
