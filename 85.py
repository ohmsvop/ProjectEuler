# Counting rectangles
from __future__ import division
from math import sqrt, floor, ceil

# x(x+1)y(y+1) ~ 8000000

t = 8000000

min_diff = 10000
best_x = 0
best_y = 0

for x in range(1, 3000):
    y = (-1 + sqrt(1 + 4*t/x/(x+1)))/2
    for y_ in [floor(y),ceil(y)]:
        diff = abs(t-x*(x+1)*y_*(y_+1))
        if diff < min_diff:
            min_diff = diff
            best_x = x
            best_y = y_

print best_x, best_y, min_diff
