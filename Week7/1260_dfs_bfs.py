from sys import stdin
from collections import deque

N, M, V = map(int, stdin.readline().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

visitedDFS = [False] * (N + 1)
visitedBFS = [False] * (N + 1)


def BFS(V):
    q = deque([V])
    visitedBFS[V] = True
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, N + 1):
            if visitedBFS[i] == False and graph[V][i] == True:
                q.append(i)
                visitedBFS[i] = True


def DFS(V):
    visitedDFS[V] = True
    print(V, end=" ")
    for i in range(1, N + 1):
        if graph[V][i] == True and visitedDFS[i] == False:
            DFS(i)

DFS(V)
print()
BFS(V)
