def f(n):
    i = 0
    X = True
    while X:
        i = i + 1
        m = i*n
        X = all([int(i) for i in str(m)])>2
    return m
