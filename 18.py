# Maximum path sum I

data = open("data/18.txt").read()
data = data.split("\n")
data = [map(int,row.split()) for row in data]

candidate = [data[0]]
n = len(data)
for i in range(1,n):
    candidate.append([])
    candidate[-1].append(candidate[i-1][0]+data[i][0])
    for j in range(i-1):
        candidate[-1].append(max(candidate[i-1][j]+data[i][j+1], candidate[i-1][j+1]+data[i][j+1]))
    candidate[-1].append(candidate[i-1][-1]+data[i][-1])


print max(candidate[-1])
