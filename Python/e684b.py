mod = 10 ** 9 + 7


def S(n):
    d = n // 9
    k = n % 9
    ret = pow(10, d, mod) * (n + 6 - 9 * d + k * (k + 1) // 2) - n - 6
    return ret % mod


def main():
    a, b = 0, 1
    ret = 0
    for i in range(2, 91):
        a, b = b, a + b
        ret += S(b)
    print(ret % mod)
