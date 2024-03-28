# from sys import stdin
# from collections import deque
#
#
# def bfs(start, end):
#     q = deque([start])
#     visited = [False] * (n + 1)
#     cnt = 0
#
#     while q:
#         node = q.popleft()
#         visited[node] = True
#
#         if end in llist[node] and start in llist[node]:
#             return cnt
#         elif end in llist[node]:
#             return cnt + 1
#
#         for i in llist[node]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = True
#         cnt += 1
#     return -1
#
#
# n = int(stdin.readline().strip())
# start, end = map(int, stdin.readline().split())
# m = int(stdin.readline().strip())
#
# llist = [[] for _ in range(n + 1)]
#
# for _ in range(m):
#     a, b = map(int, stdin.readline().split())
#     llist[a].append(b)
#     llist[b].append(a)
#
# for i in llist:
#     i.sort()
#
# print(bfs(start, end))

N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
result = []

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(v, num):
    num += 1
    visited[v] = True

    if v == B:
        result.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)


dfs(A, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)
