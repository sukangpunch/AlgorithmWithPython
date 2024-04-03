from sys import stdin
from collections import deque

#n -> 수빈이의 위치, k -> 동생의 위치
n, k = map(int, stdin.readline().split())
#동생과 수빈이가 있을 수 있는 최대의 좌표
limit = 100001
#최대로 있을 수 있는 좌표만큼 time list 생성
time = [0] * limit


#x -> 수빈이 위치, y -> 동생 위치
def bfs(x, y):

    q = deque()
    if x == 0: # 0 인 경우 * 우선순위가 들어가면, 무한으로 0을 곱하는 경우를 막기 위해
        q.append(1) #0이면 무조건 1부터 시작 하게
    else:
        q.append(x)

    while q:
        x = q.popleft()
        if y == x:
            return time[x]

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < limit and time[nx] == 0:
                if nx == 2 * x:
                    time[nx] = time[x]
                    q.appendleft(nx)
                else:
                    time[nx] = time[x] + 1
                    q.append(nx)


if n == 0:
    if k == 0:
        print(0)
    else:
        print(bfs(n, k) + 1)
else:
    print(bfs(n, k))