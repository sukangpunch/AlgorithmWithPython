from sys import stdin
from collections import deque

T = int(stdin.readline().strip())
graph = [[]]
result = []
for _ in range(T):
    m, n, k = map(int, stdin.readline().split())
    graph = [[False] * m for _ in range(n)]

    for i in range(k):
        x, y = map(int, stdin.readline().split())
        graph[y][x] = True

    visited = [[False] * m for _ in range(n)]
    cnt = 0
    check = 0

    for y in range(n):
        for x in range(m):
            if not visited[y][x] and graph[y][x]:
                q = deque([(x, y)])
                visited[y][x] = True
                while q:
                    ax, ay = q.popleft()
                    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                        nx, ny = ax + dx, ay + dy

                        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx]:
                            visited[ny][nx] = True
                            q.append((nx, ny))
                cnt += 1
    result.append(cnt)

for i in result:
    print(i)













