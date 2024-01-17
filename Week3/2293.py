from sys import stdin

n, k = map(int,stdin.readline().strip().split())

coins = []
for _ in range(n):
    coins.append(int(stdin.readline().strip()))

result = [0 for i in range(k+1)]
result[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        result[i] += result[i-coin]

print(result[k])






