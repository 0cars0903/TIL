T = int(input())
ans = []
for i in range(T):
    A = str()
    Test =list(map(str, input()))  
    a = int(Test[0])
    B = Test[2:]
    P = []
    for j in range(len(B)):
        C = (((B[j])*a))
        A = A + str(C)
    ans.append(A)
for x in range(T):
    print(ans[x], end='' "\n")
