from sys import stdin

semester = int(stdin.readline().strip())


result = 0
st = []

class Subject():
    def __init__(self, point, time):
        self.point = point
        self.time = time

for i in range(semester):
    inputs = stdin.readline().strip()
    if len(inputs) == 1 and len(st)>0:
        s = st.pop()
        s.time = s.time-1
        if s.time == 0:
            result +=s.point
        else:
            st.append(s)
    elif len(inputs) == 1 and len(st) == 0:
        continue
    else:
        a,b,c = map(int,inputs.split())
        s = Subject(b, c)
        s.time = s.time -1
        if s.time == 0:
            result +=s.point
        else:
            st.append(s)

print(result)

