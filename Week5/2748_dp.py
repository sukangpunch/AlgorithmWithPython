from sys import stdin


num = int(stdin.readline().strip())

pibo = [0, 1]

for i in range(2, num+1):
    pibo.append(pibo[i-1]+pibo[i-2])

print(pibo[num])


