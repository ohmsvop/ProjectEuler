# Even Fibonacci numbers

# 1,2,3,5,8,13,21,34,55...
# o,e,o,o,e,o,o,e,o...

# n7 = n6 + n5 = (n5 + n4) + (n4 + n3) 
#    = (n4 + n3) + 2n4 + (n2 + n1) 
#    = 4n4 + n1

limit = 4000000
f = [2,8]

while True:
    newf = f[-1]*4 + f[-2]
    if newf <= limit:
        f.append(newf)
    else:
        break

print sum(f)
