'Problem 56 - Powerful digit sum'
s2 = 0
for a in range(1,101):
    for b in range(1,101):
        s1 = sum([int(i) for i in str(a**b)])
        if s1>s2:
            s2 = s1
print(s2)
