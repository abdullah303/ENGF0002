from random import random

def estimate_pi(precision):
    hits, total = 0, 0
    for i in range(precision):
        x, y = random(), random()
        if (x-0.5)**2 + (y-0.5)**2 <= 0.25:
            hits += 1
        total += 1
    return 4*(hits/total)

print(estimate_pi(10))
print(estimate_pi(100))
print(estimate_pi(1000))
print(estimate_pi(10000))
print(estimate_pi(100000))
