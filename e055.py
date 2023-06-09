"""Problem 55 - Lychrel numbers"""
reverse = lambda n: int(str(n)[::-1])


def lychrel(n):
    for i in range(50):
        n += reverse(n)
        if n == reverse(n): return False
    return True


print(len([n for n in range(1, 10000) if lychrel(n)]))
