from collections import Counter
n = int(input())


for i in range(n):
    a, b = map(str, input().split())

    a_count = Counter(a)
    b_count = Counter(b)

    if a_count == b_count:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")

