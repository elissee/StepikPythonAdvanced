n = int(input())

d = {}
a = []
b = []
for i in range(n):
    x = input().lower().split()
    a.append(x)
    d.setdefault(x[1], []).append(x[0])

m = int(input())

for i in range(m):
    x = input().lower()
    b.append(x)

for i in b:
    if i in d:
        [print(i, end=' ') for i in d[i]]
        print()
    else:
        print('абонент не найден')
