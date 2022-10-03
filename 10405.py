n = int(input())

a = []
d = {}
b = []

for i in range(n):
    x = input().split()
    a.append(x)
    d[x[0]] = x[1:]

m = int(input())

for i in range(m):
    x = input()
    for key in d:
        if x in d[key]:
            b.append(key)

for i in range(len(b)):
    print(b[i])
