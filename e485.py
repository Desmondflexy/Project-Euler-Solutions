from myfunc import sqrt

def d(n):
    'Counts divisors of a number'
    k = 0
    z = int(sqrt(n))
    for i in range(1, z + 1):
        if n % i == 0: k += 2
    if z * z == n: k -= 1
    return k

def M(n, k):
    return max([d(j) for j in range(n, n + k)])

def S(u, k):
    return sum([M(n, k) for n in range(1, u - k + 2)])

print(S(1000, 10))
