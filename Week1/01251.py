from sys import stdin

string = list(stdin.readline().strip())

greedy = []
result = []

for i in range(1, len(string)-1):
    for j in range(i+1, len(string)):
        a = string[:i]
        b = string[i:j]
        c = string[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        greedy.append(a+b+c)

for i in greedy:
    result.append(''.join(i))

print(sorted(result)[0])















