import heapq
from sys import stdin

n = int(stdin.readline().strip())
m = int(stdin.readline().strip())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    #s : 시작노드, e 끝노드, v 가중치
    s, e, v = map(int, stdin.readline().split())
    # s에서 시작, e끝인 간선의 가중치  v를 나타냄
    graph[s].append((e, v)) #해당 그래프에 start에 해당하는 끝 노드와 가중치가 dict 형식으로 박힘
start, end = map(int, stdin.readline().split())


def dijkstra(graph, start):
    distances = [int(1e9)] * (n + 1)
    distances[start] = 0
    queue = []
    #지금까지 발견된 가장 짧은 거리에 노드에 대해서 먼저 계산 할 수 있게 함.
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


result = dijkstra(graph, start)
print(result[end])
