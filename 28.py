# Number spiral diagonals
# 1  3  5  7  9 13 17 21 25 31
# 1 +2 +2 +2 +2 +4 +4 +4 +4 +6 +6 +6 +6 ...

limit = 1001

a = 1
total = a
for b in range(2, limit, 2):
    for i in range(4):
        a += b
        total += a

print total
