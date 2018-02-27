# 1000-digit Fibonacci number

F = [1,1]
n = 2

for i in range(10000):
    F.append(F[0] + F[1])
    F.pop(0)
    n += 1    
    if len(str(F[-1])) == 1000:
        break
print n
