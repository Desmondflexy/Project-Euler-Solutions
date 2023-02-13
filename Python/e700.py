a = 1504170715041707
b = 4503599627370517

s = a

while a > 1:
    a, b = a - b % a, a
    s += a

print(s)
