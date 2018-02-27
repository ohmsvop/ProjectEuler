from __future__ import division
from math import sqrt
from math import pi

tri = [(1,1,1),(1,2,2),(1,3,3),(1,4,4),(2,2,2),(2,2,3),(2,3,3),(2,3,4)]
area = []
for t in tri:
    s = (t[0] + t[1] + t[2]) /2
    radius = []
    r1 = sqrt((s-t[0])*(s-t[1])*(s-t[2])/s)
    
    r2 = []
    for i in t:
        r2.append(r1 + 2*r1**3/(s-i)**2 - 2*r1**2/(s-i)**2*sqrt((s-i)**2+r1**2))    
    
    r3 = []
    for i in range(3):
        r3.append(r2[i] + 2*r2[i]**3/(s-t[i]-2*sqrt(r1*r2[i]))**2 - 2*r2[i]**2/(s-t[i]-2*sqrt(r1*r2[i]))**2*sqrt((s-t[i]-2*sqrt(r1*r2[i]))**2+r2[i]**2))
    
    rmax = r2+r3
    rmax.sort()
    area.append( pi*(r1**2 + rmax[-1]**2 + rmax[-2]**2))
    
print (sum(area)/len(area))
