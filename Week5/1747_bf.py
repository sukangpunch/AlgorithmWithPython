from sys import stdin
import math


def isPrime(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


N = int(stdin.readline().strip())
result = 0
cnt = N
while 1:
    if N == 1:
        N += 1
        continue
    if str(N) == str(N)[::-1]:
        if isPrime(N):
            result = N
            break
        else:
            N += 1
    else:
        N += 1

print(result)