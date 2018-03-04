# Pandigital multiples

def pandigital(n):
    n = str(n)
    if len(n) != 9:
        return False
    for i in range(1, 10):
        if str(i) not in n:
            return False
    return True

candidate = []
for i in range(2, 10000):
    n = 1
    si = ""
    while True:
        si += str(n*i)
        if len(si) >= 9:
            break
        n += 1
    if pandigital(si):
        candidate.append(si)

print max(candidate)
