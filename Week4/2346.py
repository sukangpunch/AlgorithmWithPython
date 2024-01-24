from sys import stdin
from collections import deque

num = int(stdin.readline().strip())

#balloon = list(map(int,stdin.readline().strip().split()))

balloons = {}

for i, value in enumerate(stdin.readline().split()):
    balloons[i+1] = int(value)

balloon = deque(balloons)
now = 0

for i in range(num):
    if i == 0:
        a = balloon.popleft()
        now = balloons[a]
        print(a,end=' ')
    else:
        if now > 0:
            for j in range(now-1):
                b = balloon.popleft()
                balloon.append(b)
            c = balloon.popleft()
            now = balloons[c]
            print(c,end=' ')
        else:
            for j in range(-now):
                b = balloon.pop()
                balloon.appendleft(b)
            c = balloon.popleft()
            now = balloons[c]
            print(c,end=' ')















