from sys import stdin

line, length = map(int, stdin.readline().strip().split())

player = []
number = 0
ranking = []
numbers = [0] * (line-1)
cnt = 0

for _ in range(line):
    player.append(stdin.readline().strip())

for play in player:
    cnt = 0
    number = -1
    for i in range(length - 2, 0, -1):
        if play[i] == '.':
            cnt += 1
        elif play[i].isdigit():
            number = int(play[i])
            break
    if number == -1:
        pass
    else:
        numbers[number-1] = cnt

for i in range(len(numbers)):
    print(numbers[i])



