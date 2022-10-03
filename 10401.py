n = int(input())

a = []
b = []

my_dict = {}

met = []

for i in range(n):
    x = input().split(': ')
    a.append(x[0].lower())
    b.append(x[1])

my_dict = dict(zip(a, b))

m = int(input())

for i in range(m):
    met.append(input().lower())

for i in met:
    print(my_dict.get(i, "Не найдено"))
