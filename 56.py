# Powerful digit sum

def digit_sum(a, b):
    return sum(int(s) for s in str(a**b))

max_digit_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        d = digit_sum(a,b)
        if d > max_digit_sum:
            max_digit_sum = d

print max_digit_sum
