import sys
print = sys.stdout.write

num = int(input())


for i in range(num):
    if num % 2 == 0:
        for j in range(num//2):
            print("* ")
        print("\n ")
        for j in range(num - num//2):
            print("* ")
    elif num % 2 != 0:
        for j in range(num//2+1):
            print("* ")
        print("\n ")
        for j in range(num - (num//2+1)):
            print("* ")
    print("\n")