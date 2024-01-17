from sys import stdin

number = int(stdin.readline().strip())

pibo = []

for i in range(2):
    pibo.append(i)

for i in range(2,number+1,1):
    pibo.append(pibo[i-1]+pibo[i-2])

print(pibo[number])



