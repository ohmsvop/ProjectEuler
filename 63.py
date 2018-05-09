# Powerful digit counts

# n >= 10, at least 1 digit more, e.g. 10**3 = 1000

total = 0

for n in range(1, 10):
    p = 1
    while True:
        if len(str(n**p)) == p:
            total += 1
            p += 1
        else:
            break
print total
