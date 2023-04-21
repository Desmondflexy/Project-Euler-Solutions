target = 2000000
best_diff = target
best_area = 0

for m in range(1, 100):
    for n in range(m, 100):
        num_rectangles = (m * (m + 1) * n * (n + 1)) // 4
        diff = abs(num_rectangles - target)
        if diff < best_diff:
            best_diff = diff
            best_area = m * n

print(best_area)
