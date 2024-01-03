hubo = int(input())
me = int(input())
list = []
cnt = 0

for i in range(hubo-1):
     com = int(input())
     list.append(com)

#내림차순 정렬
list.sort(reverse=True)

if hubo == 1:
    print(0)
else:
    while list[0] >= me:
        me +=1
        list[0] -=1
        cnt +=1
        list.sort(reverse=True)
    print(cnt)


