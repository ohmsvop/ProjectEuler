# Digit factorials
from math import factorial

f = [factorial(i) for i in range(10)]

def check(n):
    digit = map(int, str(n))
    sum_f = sum(f[d] for d in digit)
    if n == sum_f:
        return True
    else:
        return False

candidate = []
limit= f[9] * 7
for i in range(3,limit):
    if check(i):
        candidate.append(i)
