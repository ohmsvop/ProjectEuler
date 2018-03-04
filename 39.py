# Integer right triangles
from collections import Counter

limit = 1000/2

square = [i**2 for i in range(limit)]
square_set = set(square)

perimeter = []
for a in range(1, limit):
    for b in range(1, a):
        c2 = square[a] + square[b]
        if c2 in square_set:
            c = int(c2**0.5)               
            perimeter.append(a+b+c)

p = Counter(perimeter)
print p.most_common(5)
