"""
RANDON FIRSTNAMES AND SCORES GENERATOR
This program gets random names from the file 'p022_names.txt'
and assign random scores to each name and then copies the
result to the clipboard to paste into excel.
"""

import random
import pyperclip

with open('p022_names.txt', 'r') as book:
    lst = book.read().split(',')

randomNames = random.sample(lst, k=1000)

maxNameLength = len(max(randomNames, key=lambda i: len(i))) - 2

sn = 0
names = ["S/N\tNAME\tSCORE"]
for name in randomNames:
    sn += 1
    names.append(f'{str(sn)}\t{name[1:-1]}\t{str(random.randint(20, 95))}')

    print(f'{str(sn):>4}\t|\t{name[1:-1]:{maxNameLength}}\t|\t{str(random.randint(20, 95))}')

text = '\n'.join(names)
pyperclip.copy(text)
print(f'copied {sn} results to clipboard!')
