# import sys
#
# input = sys.stdin.readline
#
# string = list(input().strip())
# M = int(input().strip())
#
# curser = len(string)
#
# for i in range(M):
#     command = input().strip()
#     if len(command) > 1:
#         ans, add = command.split()
#         if ans == 'P':
#             string.insert(curser, add)
#             curser += 1
#     else:
#         if command == 'L' and curser != 0:
#             curser -= 1
#         elif command == 'D' and curser != len(string):
#             curser += 1
#         elif command == 'B' and curser != 0:
#             string.pop(curser-1)
#             curser -= 1
#
# print(''.join(string))

from sys import stdin
left = list(stdin.readline().strip())
right = []

for _ in range(int(stdin.readline().strip())):
    command = list(stdin.readline().split())
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])
answer = left + right[::-1]
print(''.join(answer))