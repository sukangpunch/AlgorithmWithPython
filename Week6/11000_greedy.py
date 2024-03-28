# from sys import stdin
#
# N = int(stdin.readline().strip())
#
# time = []
# room = []
# cnt = 0
#
# for _ in range(N):
#     time.append(stdin.readline().strip())
#
# times = sorted(time, key=lambda x: int(x.split()[0]))
#
# for i in range(N):
#     st, end = map(int, times[i].split())
#     if len(room) == 0:
#         room.append(end)
#         cnt += 1
#     else:
#         for j in range(len(room)):
#             if room[j] <= st:
#                 room[j] = end
#                 break
#             else:
#                 if len(room) == j+1:
#                     cnt += 1
#                     room.append(end)
#                     break
#                 else:
#                     continue
# print(cnt)

import heapq
from sys import stdin

N = int(stdin.readline().strip())

arr = []
current = []

for _ in range(N):
    start, end = map(int, stdin.readline().split())
    arr.append([start,end])
arr.sort()

heapq.heappush(current, arr[0][1])

for i in range(1, N):
    if arr[i][0] < current[0]:
        heapq.heappush(current,arr[i][1])
    else:
        heapq.heappop(current)
        heapq.heappush(current,arr[i][1])

print(len(current))




