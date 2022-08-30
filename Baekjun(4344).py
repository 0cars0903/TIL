N = int(input())
for i in range(N):
    A = input().split()
    B = []
    C = []
    sum = 0
    for i in range(len(A)-1):
        b = int(A[i+1])
        sum += int(A[i+1])
        B.append(b)
    # print(B) 
    avg = int(sum/int(len(B)))
    # print(avg) 
    for i in range(len(B)):
        if B[i] > avg:
            C.append(B[i])
    # print(C) 
    X = round(float((len(C)/len(B))*100),3)
    # print(X) 
    print(f"{X:.3f}%") # 소수점 3자리까지 표현 하기
