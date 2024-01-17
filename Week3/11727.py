from sys import stdin

num = int(stdin.readline().strip())

result = [0] * (num + 1)
result[0] = 1
result[1] = 3

if num > 2:
    for i in range(2,num,1):
        result[i] = (result[i-1] + result[i-2] *2) %10007

print(result[num-1])


















