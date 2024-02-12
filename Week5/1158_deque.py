from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().strip().split())

permutation = [i for i in range(1, n+1)]
permutation_deque = deque(permutation)
result = []

while len(permutation_deque) !=0:
    for _ in range(k-1):
        temp = permutation_deque.popleft()
        permutation_deque.append(temp)
    result.append(permutation_deque.popleft())

result_string = '<' + ', '.join(map(str,result)) + '>'
print(result_string)







