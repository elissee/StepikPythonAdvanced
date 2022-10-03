a = set(int(i) for i in input().split())
b = set(int(i) for i in input().split())
c = set(int(i) for i in input().split())

union_x = a.union(b, c)
intersection_x = a.intersection(b, c)

x = union_x.difference(intersection_x)

print(union_x)
print(intersection_x)

print(*sorted(x))
