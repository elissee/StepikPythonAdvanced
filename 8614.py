a = set(int(i) for i in input().split())
b = set(int(i) for i in input().split())
a.discard(' ')
b.discard(' ')
c = a.intersection(b)
sorted_numbers = sorted(c)
print(*sorted_numbers)