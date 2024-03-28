from sys import stdin
from collections import deque

n, m, h = map(int, stdin.readline().split())

graph = []
for i in range(h):
    mock = []
    for j in range(m):
        mock.append(list(map(int, stdin.readline().split())))
    graph.append(mock)

q = deque()
deq = deque()

for k in range(h):
    for i in range(m):
        for j in range(n):
            if graph[k][i][j] == 1:
                q.append((k, i, j))

day = 0
while q:
    while q:
        deq.append(q.popleft())
    while deq:
        z, x, y = deq.popleft()

        for dz, dx, dy in (-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1):
            nz, nx, ny = z + dz, x + dx, y + dy
            if 0 <= nz < h and 0 <= nx < m and 0 <= ny < n and graph[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                graph[nz][nx][ny] = 1
    if q:
        day += 1

for z in range(h):
    for x in range(m):
        for y in range(n):
            if graph[z][x][y] == 0:
                day = -1

print(day)
