import math

perimeter_sum = 0

for a in range(2, 500_000):
    b1 = math.ceil(math.sqrt(a ** 2 - ((a - 1) / 2) ** 2))
    b2 = math.floor(math.sqrt(a ** 2 - ((a + 1) / 2) ** 2))
    for b in range(b1, b2 + 1):
        area = (a * b) // 2
        if 2 * area == a * (a - 1) or 2 * area == a * (a + 1):
            perimeter = 2 * a + b
            if perimeter <= 1_000_000_000:
                perimeter_sum += perimeter

print(perimeter_sum)
