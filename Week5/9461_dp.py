from sys import stdin

num = int(stdin.readline().strip())

size = []
rect = [0,1,1,1,2,2]
result = []

for i in range(num):
    size.append(int(stdin.readline().strip()))

for i in range(num):
    rect = [0,1,1,1,2,2]
    for j in range(6, size[i]+1):
        rect.append(rect[j-1]+rect[j-5])
    result.append(rect[size[i]])

for i in range(num):
    print(result[i])






