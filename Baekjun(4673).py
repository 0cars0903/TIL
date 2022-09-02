def d(A):
    N = list(map(int, str(A)))
    num = A + sum(N)
    return num

# def d(N):
#     a = int(N / 1000)
#     A = int(N % 1000)
#     b = int(A / 100)
#     B = int(A % 100)
#     c = int(B / 10)
#     C = int(B % 10)
#     d = C
#     num = N + a + b + c + d
#     return num  
  
X = [x for x in range(1,10000)]
for i in range(1,10000):
    cal = d(i)
    if cal in X:
        X.remove(cal)
for i in range(len(X)):
    print(X[i])
