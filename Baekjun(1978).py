import math

# 수의 개수
N = int(input())
C = [] # 2 저장
E = [] # 소수가 아닌 수 저장

# X개의 수
X = list(map(int, input().split()))
X.sort()

# 집합 정렬
if 1 in X:
    del X[X.index(1)]
if 2 in X:
    del X[X.index(2)]
    C.append(2)
 # 소수찾기
if len(X) == 0:
    sum = len(C)
if len(X) >= 1:
    for i in range(0,len(X)):
        l = X[i]
        while l > 2:
            l -= 1
            if X[i] % l == 0:
                e = X[i]
                E.append(e)
                break
                
sum = len(X) - len(E) + len(C)
print(sum)
