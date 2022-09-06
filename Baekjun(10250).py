import math
# 입력
T = int(input())
X = []
Y = []
for j in range(T):
    A = list(map(int, input().split()))
    H = A[0]
    W = A[1]
    N = A[2]

    G = math.ceil(N / H)
    R = []
    for i in range(H*(G-1)+1,H*G+1):
        R.append(i)
    Y.append(R.index(N)+1)
    X.append(G)
for i in range(T):
    if X[i] < 10:
        print("{0}0{1}".format(Y[i],X[i]))
    else:
        print("{0}{1}".format(Y[i],X[i]))
