from string import ascii_uppercase
Alpha_l = list(str(ascii_uppercase))
l = list((str(input()).upper()))
A = []

for i in range(len(Alpha_l)):
    A.append(l.count(Alpha_l[i]))
B = A
t1 = max(A)
# print(t1)
t2 = int(A.index(t1))
# print(t2)
B[t2] = 0
t3 = max(B)
# print(t3)

if t1 == t3:
    ans = "?"
if t1 > t3:
    ans = Alpha_l[t2]
print(ans)
