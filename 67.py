f = open("data/67.txt")
summ = [0]

for l in f.readlines():  
    newline = [int(num) for num in l.split()]
    history = []
    for i in summ:
        history.append(i)
        
    summ[0] = history[0] + newline[0]        
    for i in range(1,len(newline)-1):
        summ[i] = max(history[i-1]+newline[i],history[i]+newline[i])
    if len(newline) >1:
        summ.append(history[-1]+newline[-1])
       
print max(summ)
    
