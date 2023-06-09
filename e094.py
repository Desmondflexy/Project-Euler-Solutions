from math import sqrt
from time import time

def hero(sides):
    'Calculates area of a triangle'
    (a, b) = sides
    return b/4 * sqrt(4*a*a - b*b)


tic = time()
s = 4
limit = 1_000_000_000
flag = False
for a in range(2, limit):
    for b in (a-1, a+1):
        sides = (a, b)
        area = hero(sides)
        if area == int(area):
            perimeter = 2*a + b
            if perimeter > limit:
                flag = True
                break
            else:
                s += perimeter
                print(f'{perimeter:15d}')
    if flag == True:
        break

print(f"Answer: {s}")
print(f'Time elapsed: {time() - tic}')
    
# taking too long..., , might take several days
