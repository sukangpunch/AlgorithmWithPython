from sys import stdin
from collections import deque


def dfs(area, rain):
    res = 0
    visited = [[0 for i in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and area[r][c] > rain:
                q = deque([(r, c)])
                visited[r][c] = True
                res += 1
                while q:
                    x, y = q.popleft()
                    for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
                        nx, ny = dx + x, dy + y

                        if 0 <= nx < N and 0 <= ny < N:
                            if area[nx][ny] > rain and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))

    return res


N = int(stdin.readline().strip())
area = [list(map(int, stdin.readline().split())) for _ in range(N)]
#max_height, min_height = max(max(area)), min(min(area))

max_land = 1

for rain in range(0, 101):
    land = dfs(area, rain)
    max_land = max(max_land, land)
print(max_land)

#------------------------------------------------------------------------

# from collections import deque
# from sys import stdin
#
# n = int(stdin.readline().strip())
# graph = []
# max_land = 0
#
# for i in range(n):
#     graph.append(list(map(int, stdin.readline().split())))
#     for j in range(n):
#         if graph[i][j] > max_land:
#             max_land = graph[i][j]
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
#
# def bfs(a, b, value, visited):
#     q = deque()
#     q.append((a, b))
#     visited[a][b] = 1
#
#     while q:
#         x, y = q.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if graph[nx][ny] > value and visited[nx][ny] == 0:
#                     visited[nx][ny] = 1
#                     q.append((nx, ny))
#
#
# result = 0
# for i in range(max_land):
#     visited = [[0] * n for i in range(n)]
#     cnt = 0
#
#     for j in range(n):
#         for k in range(n):
#             if graph[j][k] > i and visited[j][k] == 0:
#                 bfs(j, k, i, visited)
#                 cnt += 1
#     if result < cnt:
#         result = cnt
# print(result)
