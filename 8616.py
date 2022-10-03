n = int(input())
a = set(input())
b = list(set(input()) for i in range(n-1))
for i in range(n-1):
    a.intersection_update(b[i])
print(*sorted(a))

