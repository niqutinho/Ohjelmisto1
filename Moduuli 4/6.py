import random

N = int(input())

n = 0
i = 0

while i < N:

    x = 2 * random.random() - 1
    y = 2 * random.random() - 1

    if x ** 2 + y ** 2 < 1:
        n += 1

    i += 1

pi_likiarvo = 4 * n / N

print(f"Approximation of pi: {pi_likiarvo:.4f}")