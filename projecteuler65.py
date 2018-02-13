e = [2]
for i in range(1,34):
    e.extend([1,i*2,1])


n = 100 - 1 

frac = (1,e[n])
numerator = 1

for i in range(n-1,0,-1):
    frac = (frac[1], e[i]*frac[1]+frac[0])
    numerator = e[i]

res = (e[0]*frac[1]+frac[0],frac[1])

#print res

sumint = 0
for i in str(res[0]):
    sumint += int(i)

print sumint
