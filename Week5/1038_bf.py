# from sys import stdin
#
# N = int(stdin.readline().strip())
#
# cnt = 0
# result = 0
# while 1:
#     check = 1
#     if cnt == N:
#         print(result)
#         break
#     elif N > 1022:
#         print(-1)
#         break
#     else:
#         string = str(result)
#         if len(string) == 1:
#             cnt += 1
#             result += 1
#         else:
#             for i in range(len(string)-1):
#                 if string[i] <= string[i+1]:
#                     check = 0
#             if check:
#                 cnt += 1
#                 result += 1
#             else:
#                 result += 1

from sys import stdin
from itertools import combinations

N = int(stdin.readline().strip())

result = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = ''.join(list(map(str, reversed(list(j)))))
        result.append(int(num))
        print(num)
result.sort()

# if N >= len(result):
#     print(-1)
# else:
#     print(result[N])
