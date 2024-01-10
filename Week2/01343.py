from sys import stdin

string = list(stdin.readline().strip())

result = []
tmp = []

for i in range(len(string)):
    if string[i] == '.':
        if len(tmp) % 2 == 0 and len(tmp) > 0:
            result.append('BB')
            tmp = []
        elif len(tmp) % 2 != 0:
            print(-1)
            exit(0)
        result.append('.')
    else:
        tmp.append(string[i])
        if len(tmp) % 4 == 0 and len(tmp) > 0:
            result.append('AAAA')
            tmp = []


if len(tmp) % 2 == 0 and len(tmp) > 0:
    result.append('BB')
    tmp = []
elif len(tmp) == 0:
    pass
else:
    print(-1)
    exit(0)

print(''.join(result))




















