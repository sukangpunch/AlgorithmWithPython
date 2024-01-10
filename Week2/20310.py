from sys import stdin

string = stdin.readline().strip()

zero = 0
one = 0
result = ""

for i in string:
    if i == '0':
        zero +=1
    else:
        one +=1

greedy_0 = zero/2
greedy_1 = one/2

for i in range(len(string)):
    if string[i] == '0' and greedy_0 !=0:
        result += '0'
        greedy_0 -=1
    elif string[i] == '1' and greedy_1 !=0:
        greedy_1 -=1
    elif string[i] == '1' and greedy_1 ==0:
        result += '1'
    else:
        pass

print(result)
