from sys import stdin
import math


def isPrime(x):
    if x < 2 :
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


num = int(stdin.readline().strip())
number = []
for _ in range(num):
    number.append(int(stdin.readline().strip()))

for i in range(num):
    while 1:
        if isPrime(number[i]):
            print(number[i])
            break
        else:
            number[i] += 1
