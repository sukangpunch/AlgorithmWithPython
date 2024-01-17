from sys import stdin

line,length = map(int, stdin.readline().strip().split())

player = [stdin.readline() for _ in range(line)]

rank = 1
vis = [0]*10
for j in range(length-2,0,-1):
    flag = 0
    for i in range(line):
        if player[i][j] != '.' and vis[int(player[i][j])] == 0:
            vis[int(player[i][j])] = rank
            flag = 1
        if flag == 1:
            rank += 1
for i in vis:
    if i != 0:
        print(i)















        

