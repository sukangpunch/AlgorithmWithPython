from sys import stdin
import heapq

v, e = map(int, stdin.readline().split())
k = int(stdin.readline().strip())

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))


def dijkstra(graph, start):
    distances = [int(1e9)] * (v + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        dist, node = heapq.heappop(queue)

        if distances[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])

    return distances


result = dijkstra(graph, k)
for i in range(1, v + 1):
    if result[i] < int(1e9):
        print(result[i])
    else:
        print("INF")
