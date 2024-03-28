from sys import stdin
from collections import deque

n = int(stdin.readline().strip())
graph = []

for _ in range(n):
    graph.append(list(map(int, stdin.readline().strip())))


def bfs():
    visited = [[False] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if not visited[r][c] and graph[r][c]:
                cnt = 1
                q = deque([(r, c)])
                visited[r][c] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = True
                            cnt += 1
                result.append(cnt)


result = []
bfs()
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])
