a, b = list(input()), list(input())

d1 = {}
d2 = {}

#создаем словарь "буква: количество"
for i in a:
    if i not in d1:
        d1[i] = 1
    else:
        d1[i] += 1

for i in b:
    if i not in d2:
        d2[i] = 1
    else:
        d2[i] += 1

#сравниваем словари
if d1 == d2:
    print('YES')
else:
    print('NO')
