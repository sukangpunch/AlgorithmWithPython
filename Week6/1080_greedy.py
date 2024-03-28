from sys import stdin

N, M = map(int, stdin.readline().strip().split())

matrix1 = []
matrix2 = []

for _ in range(N):
    matrix1.append(list(map(int,stdin.readline().strip())))

for _ in range(N):
    matrix2.append(list(map(int,stdin.readline().strip())))

print(matrix1)
print(matrix2)

def check(i,j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            if matrix1[x][y] == 0:
                matrix1[x][y] = 1
            else:
                matrix1[x][y] = 0

cnt = 0

if (N < 3 or M < 3) and matrix1 != matrix2:
    cnt = -1
else:
    for r in range(N-2):
        for c in range(M-2):
            if matrix1[r][c] != matrix2[r][c]:
                cnt += 1
                check(r, c)
if cnt != -1:
    if matrix1 != matrix2:
        cnt = -1

print(cnt)





