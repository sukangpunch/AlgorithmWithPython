from sys import stdin

num = int(stdin.readline().strip())

result = [0 for i in range(num+1)]

for i in range(2,num + 1):
    result[i] = result[i-1] + 1
    if i % 3 == 0:
        result[i] = min(result[i], result[i//3] + 1)
    if i % 2 == 0:
        result[i] = min(result[i], result[i//2] + 1)

print(result[num])









