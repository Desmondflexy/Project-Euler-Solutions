'''
Problem 24: Lexicographic permutations
'''

from itertools import permutations
from myfunc import array2num

print(array2num(list(permutations(range(10)))[1000000-1]))


## OR, CHECK THIS OUT!
## ans = list(permutations(range(10)))[999999]
## for k in ans:
##     print(k,end='')
