"""
Problem 22: Name scores
"""

from myfunc import wordvalue

book = open("p022_names.txt")
names = book.read().split(',')
book.close()

names.sort()

s = 0
for i in range(len(names)):
    namescore = wordvalue(names[i][1:-1]) * (i + 1)
    s += namescore
print(s)
