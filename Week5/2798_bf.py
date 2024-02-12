from sys import stdin

N, M = map(int,stdin.readline().strip().split())

number = list(map(int,stdin.readline().strip().split()))
result = []


for i in range(N):
    a = number[i]
    for j in range(i+1,N):
        b = number[j]
        for k in range(j+1,N):
            c = a + b + number[k]
            result.append(c)

pre = abs(result[0]-M)
col = 0
for i in range(1,len(result)):
    now = abs(result[i]-M)
    if result[i] <= M and pre > now:
        pre = now
        col = result[i]

print(col)




