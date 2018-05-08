# Square root convergents

from fractions import Fraction

def next_iteration(n):
    return 1/(n+2)

def compare_nd(fraction):
    n = fraction.numerator
    d = fraction.denominator
    if len(str(n)) > len(str(d)):
        return True
    else:
        return False

sq2 = [Fraction(0)]

for i in range(1000):
    sq2.append(next_iteration(sq2[-1]))

sq2 = [i+1 for i in sq2]
sq2_ngtd = sum(compare_nd(i) for i in sq2)
print sq2_ngtd
