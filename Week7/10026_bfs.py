from sys import stdin
from collections import deque


def search(graph):
    res = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                q = deque([(x, y)])
                visited[x][y] = True
                while q:
                    ax, ay = q.popleft()
                    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                        nx, ny = dx + ax, dy + ay

                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            if graph[ax][ay] == graph[nx][ny]:
                                visited[nx][ny] = 1
                                q.append((nx, ny))

                res += 1
    return res


N = int(stdin.readline().strip())
graph = [list(stdin.readline().strip()) for _ in range(N)]
nomal_search = search(graph)

for i in range(N):
    for j in range(N):
        if graph[i][j] == "R":
            graph[i][j] = "G"

blind_search = search(graph)
print(nomal_search, blind_search)
