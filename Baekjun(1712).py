import math
A, B, C = list(map(int, input().split()))
if (C - B) > 0:
    if (A / (C-B)) >= 0: 
        N = int(A / (C-B)) + 1
else:
    N = -1
print(N)
