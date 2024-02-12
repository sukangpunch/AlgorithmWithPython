from sys import stdin

N, L = map(int, stdin.readline().strip().split())

problem = list(map(int,stdin.readline().strip().split()))
problem.sort()
check = []
temp = 0
cnt = 0

for i in range(N):
    if len(check) == 0:
        check.append(problem[i]+L-1)
        cnt +=1
    else:
        for j in range(len(check)):
            if check[j] >= problem[i] >= check[j]-L:
                temp = 0
                pass
            else:
                temp = 1
        if temp:
            check.append(problem[i] + L - 1)
            cnt += 1

print(cnt)














