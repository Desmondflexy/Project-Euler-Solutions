"""
Problem 29: Distinct powers
"""

ylist = []
for a in range(2, 101):
    for b in range(2, 101):
        y = a ** b
        if y not in ylist:
            ylist.append(y)
print(len(ylist))
