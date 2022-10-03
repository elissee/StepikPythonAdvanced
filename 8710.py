#a = set(input().split() for i in input().split())
#a, b, c = set(input().split()), set(input().split()), set(input().split())
a = set(int(i) for i in input().split())
b = set(int(i) for i in input().split())
c = set(int(i) for i in input().split())
#вывести множество x, которое есть у a и b, но которых нет у c
#посмотреть тему про включение множеств
x = (a.intersection(b)).difference(c)
print(*sorted(x, reverse=True))
