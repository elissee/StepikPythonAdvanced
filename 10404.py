n = int(input())

a = []

dict1 = {}

for i in range(n):
    x = input()
    a.append(x)

s = input()

for i in a:
    d = i.split()
    dict1.setdefault(d[0], d[1])
    dict1.setdefault(d[1], d[0])

for key in dict1:
    if s == key:
        print(dict1[key])
