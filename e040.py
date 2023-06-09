"""Problem 40: Champernowme's constant"""

d = ''
a = 1
while len(d) < 1000000:
    d += str(a)
    a += 1

print(int(d[0]) * int(d[9]) * int(d[99]) * int(d[999])
      * int(d[9999]) * int(d[99999]) * int(d[999999]))
