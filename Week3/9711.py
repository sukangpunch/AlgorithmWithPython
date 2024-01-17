#내 코드에서 1번쨰와 2번째 피보나치 수에 대한 예외를 처리 하지 않았었다.

from sys import stdin

num = int(stdin.readline().strip())
p = 0
q = 0
ps = []
qs = []

result = []
pre = 0

for i in range(num):
    p, q = map(int, stdin.readline().strip().split())
    ps.append(p)
    qs.append(q)

def fibo(number,pre):
    if pre == 0:
        result.append(1)
        result.append(1)
        for i in range(2,number):
            result.append(result[i-1]+result[i-2])
    elif number > pre:
        for i in range(pre,number):
            result.append(result[i-1]+result[i-2])

    return result[number-1]


for i in range(num):
    if (ps[i] == 1 or ps[i] == 2) and qs[i] == 1:
        print("Case #{}: {}".format(i+1,0))
        continue
    elif ps[i] == 1 or ps[i] == 2:
        print("Case #{}: {}".format(i+1,1))
        continue
    a = fibo(ps[i],pre)
    if pre < ps[i]:
        pre = ps[i]
    b = a % qs[i]
    string = "Case #{}: {}".format(i+1,b)
    print(string)








