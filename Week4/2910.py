from sys import stdin
from collections import Counter

n, c = map(int, stdin.readline().strip().split())
bindo = list(map(int, stdin.readline().strip().split()))

cnt = Counter(bindo)
keys = cnt.keys()
result = cnt.most_common()

for key, value in result:
    for i in range(value):
        print(key, end=" ")
