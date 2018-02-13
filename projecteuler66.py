from __future__ import division
square = [i**2 for i in range(1,30)]
D = range(1,100+1)
for i in square:
    try:
        D.remove(i)
    except:
        pass

for i in range(len(square)):
    for j in range(i):
        D_rem = (square[i] - 1) % square[j]
        if (square[i] - 1) % square[j] == 0:
            print "%d^2 - %d * %d^2 = 1" % (i+1,((square[i] - 1) / square[j]),j+1)
            try:
                D.remove(((square[i] - 1) / square[j]))
            except:
                pass
print D
        