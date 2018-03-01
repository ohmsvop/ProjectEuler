# Non-abundant sums

from utils import sum_proper_divisor

limit = 28123
abundant = []
for i in range(1, limit+1):
    d = sum_proper_divisor(i)
    if d > i:
        abundant.append(i)

sum_of_two_abundant = []

for i in abundant:
    for j in abundant:
        k = i+j
        if k <= limit:
            sum_of_two_abundant.append(k)

sum_of_two_abundant = set(sum_of_two_abundant)
n = 0
total = 0
for i in range(1, limit+1):
    if i not in sum_of_two_abundant:
        total += i
        n += 1
print total, n
