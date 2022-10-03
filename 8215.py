#n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), \
#                         int(input()), int(input())
n, m, k, x, y, z, t, a = [int(input()) for i in range(8)]
x5 = t

x2 = n + m - x - x5
x4 = n + k - z - x5
x6 = m + k - y - x5

x1 = n - x2 - x4 - x5
x3 = m - x2 - x5 - x6
x7 = k - x4 - x5 - x6

b = x1 + x3 + x7
c = x2 + x4 + x6
d = a - (b + c + x5)

print(b)
print(c)
print(d)
