# Problems 38: Pandigital multiples

def concatprod(b, n):
    'Returns the concatenated product of b and (1,2,...n)'
    p = ''
    for i in range(1, n+1):
        p += str(b*i)
    return int(p)


def ispandigital(p):
    'Checks if a number is 1 to 9 pandigital'
    li = [int(i) for i in str(p)]
    r = range(1, 10)
    length = len(r)
    if len(li) != length:
        return False
    li.sort()
    i = 0
    while i < length and li[i] == r[i]:
        i += 1
    if i != length:
        return False
    return True


P = []
for b in range(1, 50000):
    for n in range(1, 10):
        p = concatprod(b, n)
        if p < 123456789:
            continue
        elif p > 987654321:
            break
        if ispandigital(p):
            P.append(p)
print(max(P))
