f = open("triangles.txt")
summ = 0

for a in f.readlines():
    a = [float(i) for i in a.split(",")]
    x = a[::2]
    y = a[1::2]
    side = 0
    for i in range(-2,1):
        if x[i] == x[i+1]:
            if (-x[i])*(x[i+2]-x[i])>=0:
                side +=1
            print x,y
        else:
            # y=mx+b
            m = (y[i]-y[i+1])/(x[i]-x[i+1])
            b = y[i] - m * x[i]
            if (y[i+2]-m*x[i+2]-b)*(-b) >=0 :
                side +=1            
    if side == 3:
        summ +=1

print summ
