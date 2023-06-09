"""
Problem 102: Triangle containment
"""


def area(points: list) -> float:
    """Computes area of triangle given points x,y coordinates"""
    x1, y1, x2, y2, x3, y3 = points
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) / 2)


k = 0
with open('p102_triangles.txt') as book:
    for line in book:
        xy = [int(i) for i in line.strip().split(',')]
        s = 0
        for i in range(0, 6, 2):
            p = xy[:]
            p[i] = 0
            p[i + 1] = 0
            s += area(p)
        if s == area(xy):
            k += 1
print(k)
