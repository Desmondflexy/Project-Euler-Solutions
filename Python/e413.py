def is_one_child(n):
    if n % 10 == 0: return False
    b = str(n)
    d = len(b)
    child = [int(b[i:j]) % d == 0
             for i in range(d)
                 for j in range(i + 1, d + 1)]
    return sum(child) == 1

def F(N):
    count = 0
    for i in range(N):
        if is_one_child(i):
            count += 1
    return count


