import sys
l = list(map(str, sys.stdin.readline().strip()))
x1 = int(l.count("=")) # =
x2 = int(l.count("-")) # -
x3 = 0 # dz
x4 = 0 # lj
x5 = 0 # nj
for i in range(len(l)-2):
    if (l[i] == "d"):
        if (l[i+1] == "z"):
            if (l[i+2] == "="):
                x3 += 1

for i in range(len(l)-1):
    if (l[i] == "l"):
        if (l[i+1] == "j"):
            x4 += 1
    elif (l[i] == "n"):
        if (l[i+1] == "j"):
            x5 += 1

sum = x1+x2+x3+x4+x5
s = x1, x2, x3 , x4 , x5
print(len(l)-sum)
