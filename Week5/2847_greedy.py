from sys import stdin

N = int(stdin.readline().strip())

level = []
for _ in range(N):
    level.append(int(stdin.readline().strip()))

cnt = 0

for i in range(N-1, 0, -1):
    if level[i] <= level[i-1]:
        tmp = level[i-1] - level[i] + 1
        cnt += tmp
        level[i-1] -= tmp

print(cnt)





