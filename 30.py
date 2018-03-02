# Digit fifth powers
from itertools import product

power = 5
digit_power = [i**power for i in range(10)]

candidate = []
for i in range(10, 1000000):
    sum_p = 0
    for s in str(i):
        sum_p += digit_power[int(s)]
    if sum_p == i:
        candidate.append(i)

print sum(candidate)
        

