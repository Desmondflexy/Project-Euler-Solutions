def d(k):
    sum = 0
    for i in range(1,k//2+1):
        if k%i==0: sum += i
    return sum+k

def S(N):
    sum = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            sum += d(i*j)
    return sum
