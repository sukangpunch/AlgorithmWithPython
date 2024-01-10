from sys import stdin
num = stdin.readline().strip()
problem = list(map(int,stdin.readline().strip().split()))
problem.sort()
result = 0
check = 0
#이전에 저장한 check
com = 0

for i in range(len(problem)-1):
    target = (problem[i] + problem[i+1])//2
    #현재 i ~i+1 부분과 인접한 다른 문제의 난이도 차이의 합
    check = (target - problem[i]) + (problem[i+1] - target)

    if target == problem[i]:
        pass
    elif check > com:
        com = check
        result = target

if result == 0:
    print(-1)
    exit(0)

print(result)


