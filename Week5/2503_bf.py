# from sys import stdin
#
# num = int(stdin.readline().strip())
#
# answer = []
# strike = []
# ball = []
#
# for _ in range(num):
#     a, b, c = stdin.readline().strip().split()
#     answer.append(a)
#     strike.append(b)
#     ball.append(c)
#
# result = []
# for i in range(1,10):
#     for j in range(1,10):
#         for k in range(1,10):
#             result.append(str(i)+str(j)+str(k))
#
# for i in range(num):
#     for j in range(len(result)):

from itertools import permutations
from sys import stdin

N = int(stdin.readline().strip())
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(data, 3))

for _ in range(N):
    n, s, b = map(int, stdin.readline().split())
    n = list(str(n))
    rmcnt = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= rmcnt
        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
            elif n[j] in num[i]:
                ball += 1
        if(strike != s) or (ball != b):
            num.remove(num[i])
            rmcnt += 1 #조합 리스트를 처음 원소부터 각각 비교해주기 위함, 인덱스가 꼬이지 않기 위함

print(len(num))