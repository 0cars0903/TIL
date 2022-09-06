import math
# 입력
T = int(input())
A = []
B = []
C = []
for j in range(T):
    K = int(input()) # 층수
    N = int(input()) # 호수
    P = [i for i in range(1, N+1)] # 0th floor

    for x in range(K):
        for y in range(1,N):
            P[y] += P[y-1]

    print(P[-1])
