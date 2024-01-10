from sys import stdin
string = list(stdin.readline().strip())
make = list(stdin.readline().strip())

for i in range(len(make)):
    if make[-1] == 'A':
        make.pop()
    elif make[-1] == 'B':
        make.pop()
        make.reverse()
    if string == make:
        print(1)
        exit(0)

print(0)