a, b = input().lower(), input().lower()

c = str(''.join(i for i in a if i.isalpha()))
d = str(''.join(i for i in b if i.isalpha()))

c1 = list(c)
d1 = list(d)

c2 = {}
d2 = {}

for i in c:
    if i not in c2:
        c2[i] = 1
    else:
        c2[i] += 1

for i in d:
    if i not in d2:
        d2[i] = 1
    else:
        d2[i] += 1

if c2 == d2:
    print('YES')
else:
    print('NO')
