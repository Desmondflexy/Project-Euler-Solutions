from myfunc import primes, isprime
Set = primes(50)
count = 0
for a in range(len(Set)-1):
    for b in range(a+2,len(Set)+1):
        subset  = Set[a:b]
        if isprime(sum(subset)):
            count += 1
            print(subset)
print(count)
