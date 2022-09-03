N = list(map(str, input()))
A = N[:3]
B = N[4:]
a = A
b = B
a[0] = N[2]
b[0] = N[-1]
a[-1] = N[0]
b[-1] = N[4]
# print(a, b)
n1 = 100*int(a[0]) + 10*int(a[1]) + int(a[2])
n2 = 100*int(b[0]) + 10*int(b[1]) + int(b[2])
# print(n1, n2)
if n1 >= n2:
    print(n1)
else:
    print(n2)
    
    
print(max(input()[::-1].split()))
