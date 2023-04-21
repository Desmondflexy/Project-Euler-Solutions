def lsqrt(N, num_of_digits):
    "Square root digit by digit long division method"

    A = split_twos(N)
    n = A[0]
    res = 0
    i = 9
    x = i * i
    while x > n:
        i -= 1
        x = i * i
    remainder = n - x
    res = res*10 + i

    # Decimal part
    A.append(0)
    for _ in range(num_of_digits-1):
        n = remainder*100 + A[1]
        m = res*20
        i = 9
        x = (m + i) * i
        while x > n:
            i -= 1
            x = (m + i) * i
        remainder = n - x
        res = res*10 + i

    return res


def split_twos(num: int) -> list:
    'Split the digits of num in twos from right to left.'
    a = []
    while num > 0:
        a.append(num % 100)
        num //= 100
    a.reverse()
    return a


print(lsqrt(2, 100))
