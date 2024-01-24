from sys import stdin

input = stdin.readline()
a,b = map(int, input.strip().split())

al = set(map(int,input.strip().split()))
bl = set(map(int,input.strip().split()))

stl = al - bl
result = list(stl)
result.sort()

size = len(result)
if size == 0:
    print(size)
else:
    print(size)
    for i in range(size):
        print(result[i], end=' ')

