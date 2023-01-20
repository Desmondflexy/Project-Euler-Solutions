import math

def GetDivisorsAmount(n):
    nDivisorsCounter = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0: nDivisorsCounter += 1
    return nDivisorsCounter

print("Answer: ", sum([1 for n in range(2, 10**7)
                       if GetDivisorsAmount(n)
                       == GetDivisorsAmount(n + 1)]))
