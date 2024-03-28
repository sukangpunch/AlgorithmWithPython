from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, stdin.readline().split())))

q = deque()
deq = deque()

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            q.append((i, j))

day = 0
while q:
    while q:
        deq.append(q.popleft())
    while deq:
        x, y = deq.popleft()
        for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx, ny))
    if q:
        day += 1

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            day = -1

print(day)





