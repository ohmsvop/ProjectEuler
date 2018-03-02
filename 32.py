# Pandigital products

def check(s):
    if s.count("0") != 0:
        return False
    for i in range(1,10):
        if s.count(str(i)) != 1:
            return False
    return True

candidate = []
for i in range(10000):
    for j in range(100):
        k = i * j
        if check(str(i)+str(j)+str(k)):
            candidate.append((i,j,k))

product_sum = sum(set(k for _,_,k in candidate))
