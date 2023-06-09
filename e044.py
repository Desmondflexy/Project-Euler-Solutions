import time
t1 = time.perf_counter()
max = 3000  # Adjust as needed

p = {(i*((3*i)-1) // 2): i for i in range(1, max)}

for j in p:
    for k in p:
        if (j < k and j + k in p and k - j in p):
            print(f'{p[j]} and {p[k]} have sum {j + k} and difference {abs(j - k)}')

t2 = time.perf_counter()
print(f'Elapsed time: {(t2-t1):0.4f} sec')
