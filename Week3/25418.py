from sys import stdin

now, after = map(int,stdin.readline().strip().split())

cnt = 0

while now != after:
    if after % 2 == 0 and now <= after // 2:
        after //=2
        cnt +=1
    elif after % 2 !=0 and now <= after -1:
        after -=1
        cnt +=1
    else:
        after -=1
        cnt +=1


print(cnt)






