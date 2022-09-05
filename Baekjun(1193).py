import math
X = int(input()) 
x = int(8*X + 1)
x = math.ceil(math.sqrt(x) - 1)

if x == 2:
    g = 1
elif (x % 2) == 0:
    g = int((x / 2))
else: 
    g = int((x / 2) + 1)

g_last = int((g*(g+1))/2) 
g1 = g_last - g + 1 
l = X - g1 + 1 

if (g % 2) == 0:
    A = 1 + (l - 1)
    B = g - (l - 1)
else: 
    A = g - (l - 1)
    B = 1 + (l - 1)

print("{0}/{1}".format(A,B))
