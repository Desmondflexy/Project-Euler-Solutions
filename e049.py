from myfunc import isprime
# Problem 49: Prime permutations

def isperm(s1,s2):
    '''Returns True if the string s1 and s2 are
    permutations of one another'''
    a = list(s1)
    b = list(s2)
    a.sort()
    b.sort()
    return a == b

found = False
for a in range(1111,10000,2):
    if a == 1487: continue
    if isprime(a):
        sA = str(a)
        d = 2
        while 2*d < (9999-1111):
            b = a + d
            sB = str(b)
            if isperm(sA,sB) and isprime(b):
                c = a + 2*d
                sC = str(c)
                if isperm(sA,sC) and isprime(c):
                    number = sA+sB+sC
                    found = True
                    break
            d +=2
    if found: break
print(number)

"""
Ok first, I had no idea that the common difference between the terms in sequence would also be 3330.
Given that the arithmetic sequence is a, a + d, a + 2d, I tested for all 4-digit numbers in
arithmetic sequence from 1111 to 9999 if they are prime numbers and also permutations of one another
by iterating a and d, skipping 1487 of course. The looping terminates when it finds the 4-digit number.
Runs in 0.93 seconds.
"""