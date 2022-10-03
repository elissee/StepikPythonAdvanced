z = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a = set(int(i) for i in input().split())
b = set(int(i) for i in input().split())
c = set(int(i) for i in input().split())

x = z.difference(a.union(b, c))

print(*sorted(x))
