import math
# 입력
N = int(input())
A = [a for a in range(0,int(N))]
B = [int(math.ceil(N-(3*A[b]))/5) for b in range(len(A))]
print(A)
print(B)
C = [3*A[c] + 5*B[c] for c in range(len(A))]
print(C)
d = C.index(N)
if A[d] < 0:
    print(-1)
elif B[d] < 0:
    print(-1)
else: 
    sum = A[d] + B[d]
    print(sum)
