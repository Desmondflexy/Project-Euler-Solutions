from myfunc import isprime, num2array
from time import time

def digitSum(n):
  s = 0;
  while n>0:
    s += n%10
    n //= 10
  return s


def isSTruncHarshad(n):
  ds = digitSum(n)
  m = n
  while m>0:
    if m%digitSum(m) != 0: return False
    m //= 10
  return (isprime(n/ds))

start = time()
limit = 10000
s = 0;
for num in range(11,limit,2):
  if isprime(num):
    n = num//10
    if isSTruncHarshad(n):
      print(num)
      s += num
print(s)
stop = time()
print('Elapsed time is',stop-start,'seconds')
