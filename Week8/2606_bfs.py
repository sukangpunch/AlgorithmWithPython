from sys import stdin
from collections import deque

n = int(stdin.readline().strip())
m = int(stdin.readline().strip())

graph = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (n + 1)


def bfs():
    cnt = 0
    q = deque([1])
    visited[1] = True
    while q:
        v = q.popleft()
        for i in range(1, n + 1):
            if visited[i] == False and graph[v][i] == True:
                cnt += 1
                q.append(i)
                visited[i] = True

    return cnt


result = bfs()
print(result)