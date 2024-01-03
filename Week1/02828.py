import sys
from sys import stdin
n,m = map(int, sys.stdin.readline().split())
j = int(stdin.readline())
left = 1
right = m
apples =[]
cnt = 0

for _ in range(j):
    apples.append(int(stdin.readline()))
for apple in apples:
    if left <= apple and right >= apple:
        pass
    elif left > apple:
        cnt +=(left-apple)
        right -=(left-apple)
        left = apple
    else:
        cnt +=(apple - right)
        left +=(apple -right)
        right = apple
print(cnt)