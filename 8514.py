a = set()
b = list(int(i) for i in input().split())
for i in range(len(b)):
    if b[i] in a:
        print('YES')

    else:
        print('NO')
        a.add(b[i])
