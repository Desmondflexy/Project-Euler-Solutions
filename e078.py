limit = 1000000
p = [1] + [0] * limit
for n in range(1, limit + 1):
    k = 1
    sign = 1
    pent1 = 1
    pent2 = 2
    while pent2 <= n:
        p[n] += sign * p[n - pent1] + sign * p[n - pent2]
        p[n] %= 1000000
        k += 1
        sign = -sign
        pent1 = k * (3 * k - 1) // 2
        pent2 = k * (3 * k + 1) // 2
    if p[n] == 0:
        print(n)
        break
