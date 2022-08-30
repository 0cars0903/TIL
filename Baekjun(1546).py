N = int(input())
A = map(int, input().split())
A = list(A)
B = []
M = int(max(A))
for i in range(N):
    b = (int(A[i])/M)*100
    B.append(b)
# print(B)
result = sum(B)
print(float(result/N))

# short
n,*l=map(int,open(0).read().split())
print(sum(l)*100/max(l)/n)
