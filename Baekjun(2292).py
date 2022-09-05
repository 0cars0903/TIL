import math
X = int(input())

# X가 속한 껍질
if X == 1:
    l = 1
    print(l)
else:
    x = math.sqrt((12*X-15))
    x = int(((x / 6) + 0.5))
    l = x + 1
    print(l)
