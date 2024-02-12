# from sys import stdin
#
# r, c = map(int, stdin.readline().strip().split())
#
# ches = [[] for i in range(r)]
#
# for i in range(r):
#     ches[i] = (stdin.readline().strip().split())

from sys import stdin

n, m = map(int, stdin.readline().strip().split())
board = []
result = []

for _ in range(n):
    board.append(stdin.readline().strip())

for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
        result.append(draw1)
        result.append(draw2)

print(min(result))




















