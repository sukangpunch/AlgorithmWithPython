from sys import stdin
semester, major, credit = map(int,stdin.readline().strip().split())

majors = []
subject = []
cnt = 6
remain = 8 - semester

for _ in range(10):
    a,b = map(int, stdin.readline().strip().split())
    majors.append(a)
    subject.append(b)


for i in range(remain):
    if cnt - majors[i] >= 0:
        major += majors[i]*3
        credit += majors[i]*3
        if cnt - majors[i] >= subject[i]:
            credit += subject[i]*3
        else:
            credit += (cnt-majors[i])*3

if major >=66 and credit >= 130:
    print("Nice")
else:
    print("Nae ga wae")









