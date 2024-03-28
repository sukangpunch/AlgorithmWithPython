# from sys import stdin
# from collections import Counter
#
# N, M = map(int, stdin.readline().strip().split())
# words = []
# for _ in range(N):
#     words.append(stdin.readline().strip())
# counter = Counter(words)
#
# keys = []
# counts = []
#
# for key, count in counter.most_common():
#     if len(key) > 10 or len(key) < M:
#         continue
#     keys.append(key)
#     counts.append(count)
#
# for i in range(len(keys)-1):
#     for j in range(i+1, len(keys)):
#         if counts[i] == counts[j]:
#             if len(keys[i]) < len(keys[j]):
#                 tmp = keys[i]
#                 keys[i] = keys[j]
#                 keys[j] = tmp
#             elif len(keys[i]) == len(keys[j]):
#                 if keys[i] > keys[j]:
#                     tmp = keys[i]
#                     keys[i] = keys[j]
#                     keys[j] = tmp
#
# for i in range(len(keys)):
#     print(keys[i])

import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
word_list = {}

for _ in range(N):
    word = input().strip()

    if len(word) < M:
        continue
    else:
        if word in word_list:
            word_list[word] += 1
        else:
            word_list[word] = 1


word_list = sorted(word_list.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
print(word_list)
for i in word_list:
    print(i)