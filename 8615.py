a = set(int(i) for i in input().split())
b = set(int(i) for i in input().split())
c = sorted(a.difference(b))
print(*c)
