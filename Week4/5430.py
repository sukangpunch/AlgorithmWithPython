from sys import stdin
from collections import deque

t = int(input())

for i in range(t):
    p = stdin.readline().rstrip()
    n = int(input())
    arr = stdin.readline().strip()[1:-1].split(",") #이걸 몰랐네
    queue = deque(arr)

    rev= 0
    flag = 0
    if n == 0:
        queue=[]
    for j in p:
        if j == 'R':
            rev +=1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")

