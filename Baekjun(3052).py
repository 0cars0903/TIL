B = []
lst = []
for i in range(10):
    a = int(input())
    b = a % 42
    if (b in lst) == False:
        lst.append(b)
print(len(lst))

# short
print(len({int(i)%42for i in open(0)}))
