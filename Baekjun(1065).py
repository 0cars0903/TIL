def d(n):
    A = list(map(int, str(n)))
    return A
N = int(input())
# A = d(N)
# print(A)
temp = []
for i in range(1,N+1):
    temp.append(i)
    if i >=100:
        if abs(d(i)[0] - d(i)[1]) != abs(d(i)[2]-d(i)[1]):
            temp.remove(i)
        if (d(i)[0] == d(i)[2]) & (d(i)[1] != d(i)[2]):
            temp.remove(i)
    result = len(temp)
print(result)
