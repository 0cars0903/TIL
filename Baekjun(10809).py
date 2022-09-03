from string import ascii_lowercase
Alpha_list = list(ascii_lowercase)
N = str(input())
A = []
for i in range(len(Alpha_list)):
    A.append(N.find(Alpha_list[i]))
for i in range(len(A)):
    print(A[i], end=' ')
