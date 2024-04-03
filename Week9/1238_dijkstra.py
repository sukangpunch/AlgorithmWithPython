from sys import stdin
import heapq

n, m, x = map(int, stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))


def dijkstra(graph, s, e):
    result = 0
    for v in s, e:
        distances = [int(1e9)] * (n + 1)
        distances[v] = 0
        q = []
        heapq.heappush(q, [distances[v], v])
        while q:
            dist, node = heapq.heappop(q)
            if distances[node] < dist:
                continue
            for next_node, next_dist in graph[node]:
                distance = next_dist + dist
                if distances[next_node] > distance:
                    distances[next_node] = distance
                    heapq.heappush(q, [distance, next_node])
        if v == s:
            result += distances[e]
        else:
            result += distances[s]
    return result


result = []

#각 학생들 기준으로 파티에 갔다 + 왔다 의 사이즈가 가장 큰 학생을 찾는 것
for i in range(1, n + 1):
    result.append(dijkstra(graph, i, x))

result.sort(reverse=True)
print(result[0])
