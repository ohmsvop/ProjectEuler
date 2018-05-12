# Diophantine equation
from utils import continued_fraction, is_square
from fractions import Fraction

def approximation(expansion, n):
    a0 = expansion[0]
    a1 = expansion[1:]
    frac = Fraction(0)
    l = len(expansion) - 1
    for i in range(n-1, -1, -1):
        frac = 1/(a1[i%l] + frac)
    return a0 + frac

def solve_diophantine_equation(D):
    n = 0
    expansion = continued_fraction(D)
    while True:
        frac = approximation(expansion, n)
        x = frac.numerator
        y = frac.denominator
        if x**2 - D*y**2 == 1:
            return x, y
            break
        n += 1

x_max = 0
D_max = 0
for D in range(1000):
    if is_square(D):
        continue
    x,y = solve_diophantine_equation(D)
    if x > x_max:
        x_max = x
        D_max = D

print D_max
