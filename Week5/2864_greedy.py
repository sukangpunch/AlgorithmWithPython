from sys import stdin

A, B = stdin.readline().strip().split()

AB_max = int(A.replace("5", "6")) + int(B.replace("5","6"))
AB_min = int(A.replace("6", "5")) + int(B.replace("6","5"))

print(AB_min,end=" ")
print(AB_max)




