N = int(input())
for i in range(N):
    OX = input()
    l = len(OX)
    A = []
    sum = 0
    result = 0
    for n in range(l):
        if OX[n] == "O":
            sum = sum + 1
            A.append(int(sum))
            # print(A)
        elif OX[n] == "X":
            sum = 0
            A.append(int(sum))
            # print(A)
        result += A[n]
    print(result)