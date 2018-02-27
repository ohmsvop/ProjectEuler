# Special Pythagorean triplet

# (a, b, c) = (m**2 - n**2, 2*m*n, m**2 + n**2), m > n > 0

for m in range(2, 30):
    for n in range(1, m):
        a, b, c = m**2 - n**2, 2*m*n, m**2 + n**2
        #print a, b, c
        if a+b+c == 1000:
            print a, b, c, a*b*c
