# Sub-string divisibility

primes = [2,3,5,7,11,13,17]

candidate = ["{:03d}".format(i) for i in range(0,1000)]

def add_one_digit(candidate, p):
    # add one digit and check divisibility
    new_candidate = []
    for i in candidate: 
        for j in range(10):
            d = int(i[-2:] + str(j)) 
            if d % p == 0:
                new_candidate.append(str(i)+str(j))
    return new_candidate

def remove_multiple_digit(candidate):
    new_candidate = [c for c in candidate if len(set(c)) == len(c)]
    return new_candidate

for p in primes:
    candidate = add_one_digit(candidate, p) 
    candidate = remove_multiple_digit(candidate)

print sum(int(c) for c in candidate)
