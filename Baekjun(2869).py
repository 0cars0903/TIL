A, B, V = list(map(int, input().split()))
night = 0
L = A - B
day = 0
if ((V-B) % L) == 0:
    day = int((V-B) / L)
if ((V-B) % L) != 0:
    day = int((V-B) / L) + 1
print(day)
