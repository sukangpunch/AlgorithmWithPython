from sys import stdin
n,me,p = map(int,stdin.readline().split())

if n == 0:
    print(1)
else:
    scores = list(map(int, stdin.readline().split()))

    if n == p and scores[-1] >= me:
        print(-1)
    else:
        result =n+1
        for i in range(n):
            if scores[i] <= me:
                result = i+1
                break
        print(result)





