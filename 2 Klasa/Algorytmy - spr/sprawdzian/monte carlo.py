import random

random.seed()
n = int(input('n = '))
k = 0
for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        k += 1

p = 4 * k / n
print("pi =", p)
