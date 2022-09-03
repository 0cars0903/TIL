from string import ascii_uppercase
import sys
Ascii = list(ascii_uppercase)
txt = list((sys.stdin.readline().strip()))
l = len(txt)
sum = 0
a = [0, 1]
a.append(Ascii[:3])
a.append(Ascii[3:6])
a.append(Ascii[6:9])
a.append(Ascii[9:12])
a.append(Ascii[12:15])
a.append(Ascii[15:19])
a.append(Ascii[19:22])
a.append(Ascii[22:])

for i in range(int(l)):
    # print(txt[i])
    for j in range(2,10):
        # print(a[j])
        if txt[i] in a[j]:
            sum = sum + j
print(sum+1*int(l))
