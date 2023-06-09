from time import time

def check2digit(N):
    for i in (0,9,8,7,6,5,4,3,2,1):
        if N%10 != i: return False
        N //= 100
    return True

start = time()
for num in (a + b for a in (30)
            for b in range(1010101000, 1389026600, 100)):
    if check2digit(num**2): break
#    if str(num*num)[::2] == '1234567890': break
print(num)
stop = time()
print('Time elapsed is', stop - start,'sec')
