from sys import stdin
num = int(stdin.readline().strip())

bar = stdin.readline().split()
bar_size = 0
result = 0
for i in range(num):
    bar_size +=int(bar[i])

bar.sort(reverse=True)

for i in range(num):
    bar_size = bar_size-int(bar[i])
    result += bar_size * int(bar[i])

print(result)






