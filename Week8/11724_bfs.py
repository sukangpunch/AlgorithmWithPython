from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (n + 1)


def bfs():
    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            q = deque([i])
            visited[i] = True

            while q:
                v = q.popleft()
                for j in range(1, n + 1):
                    if graph[v][j] == True and not visited[j]:
                        q.append(j)
                        visited[j] = True
            cnt += 1

    return cnt


result = bfs()
print(result)
