from sys import stdin
from collections import deque

num = int(stdin.readline().strip())

dq = deque()

for _ in range(num):
    instruct = stdin.readline().strip()
    if len(instruct) < 3:
        if int(instruct) == 3:
            if dq:
                print(dq.popleft())
            else:
                print(-1)
        elif int(instruct) == 4:
            if dq:
                print(dq.pop())
            else:
                print(-1)
        elif int(instruct) == 5:
            print(len(dq))
        elif int(instruct) == 6:
            if dq:
                print(0)
            else:
                print(1)
        elif int(instruct) == 7:
            if dq:
                print(dq[0])
            else:
                print(-1)
        else:
            if dq:
                print(dq[-1])
            else:
                print(-1)
    else:
        a,b = map(int,instruct.strip().split())
        if a == 1:
            dq.appendleft(b)
        else:
            dq.append(b)









