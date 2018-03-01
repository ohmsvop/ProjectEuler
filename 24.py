# Lexicographic permutations

from math import factorial

f = [factorial(i) for i in range(9, 0, -1)]

limit = 1000000
r = limit-1
n = []
for i in f:
    n.append(r/i)
    r = r % i

s = "0123456789"
p = ""
for i in n:
    p += s[i]
    s = s[:i] + s[i+1:]
print p + s
