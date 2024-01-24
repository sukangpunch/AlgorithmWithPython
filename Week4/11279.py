from sys import stdin
import heapq

num = int(stdin.readline().strip())

input = []
heap = []

for _ in range(num):
    input.append(int(stdin.readline().strip()))

for i in range(num):
    if input[i] == 0 and len(heap)>0:
        print(-heapq.heappop(heap))

    elif input[i] ==0 and len(heap) == 0:
        print(0)
    else:
        heapq.heappush(heap,-input[i])









