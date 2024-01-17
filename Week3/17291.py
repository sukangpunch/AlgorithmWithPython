from sys import stdin

n = int(stdin.readline().strip())

death = [0 for _ in range(21)]
num = [0 for _ in range(21)]

num[1] = 1
death[4] = 1

for i in range(2,21):
    if i == n+1:
        break
    birth = num[i-1]
    num[i] = num[i-1] * 2 - death[i]

    if i%2 == 0:
        if i+4 <=20:
            death[i+4] += birth
    else:
        if i+3 <=20:
            death[i+3] +=birth

print(num[n])















# from sys import stdin
#
# num = int(stdin.readline().strip())
#
# result = []
# born = []
# cnt = 0
# result.append(0)
# result.append(1)
# born.append(0)
# born.append(1)
#
# for i in range(2,num+1):
#
#     if i % 2 ==0 and cnt % 4 !=0:
#         result.append(result[i-1]*2)
#         born.append(result[i-1]*2 - result[i-2])
#         cnt +=1
#     elif i % 2 == 0 and cnt !=0 and cnt % 4 == 0:
#         result.append(result[i-1]*2 - born[i-4])
#         born.append(result[i - 1] * 2 - result[i - 2])
#         cnt +=1
#     elif i % 2 !=0 and cnt % 3 != 0:
#         result.append(result[i - 1] * 2)
#         born.append(result[i - 1] * 2 - result[i - 2])
#     elif i % 2 !=0 and cnt % 3 ==0:
#         result.append(result[i-1]*2 - born[i-3])
#         born.append(result[i-1]*2 - result[i-2])
#         cnt +=1
#
# print(result[num])

