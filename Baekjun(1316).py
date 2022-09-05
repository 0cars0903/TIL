import sys
N = int(input())
B = [] # 그룹문자가 아닌 글자 모임
C = [] # 입력받은 글자 모임
for i in range(N):
    l = sys.stdin.readline().lower().strip()
    C.append(l)
    for j in range(len(l)-1):
        x1 = l[j] # str
        x2 = l[j+1:] # list
        if (x1 in x2) & (x2[0] != x1):
            B.append(l)
            break
print(len(C)-len(B))
