# Permuted multiples

def check_same_digit(n):
    multiple = 6
    p = [set(str(n*i)) for i in range(1, multiple+1)]
    for i in range(multiple-1):
        if p[i] != p[i+1]:
            return False
    return True

n = 0
while True:
    n += 1
    if check_same_digit(n):
        print n
        break
