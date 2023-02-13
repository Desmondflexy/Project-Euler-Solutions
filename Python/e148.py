def fun(row):
  '''Counts the number of entries not divisible by 7 in a row'''
  n = row-1
  p = 1
  while True:
    a = n%7 + 1
    p = p*a
    if n<7: break
    n = n//7
  return p

k = 0
for row in range(1,1000000001):
  k += fun(row)
print(k)
