a = set(int(i) for i in input().split())
b = set(int(i) for i in input().split())
c = set(int(i) for i in input().split())

x = (c.difference(a.union(b)))

print(*sorted(x, reverse=True))
