from sys import stdin
num = int(stdin.readline().strip())
cnt = 0

for i in range(1,num + 1):
    if i < 100:
        cnt += 1
    elif i >= 100:
        a = list(str(i))
        if a[0] == a[1] and a[1] == a[2]:
            cnt += 1
        elif int(a[0]) - int(a[1]) == int(a[1])-int(a[2]):
            cnt += 1

print(cnt)








