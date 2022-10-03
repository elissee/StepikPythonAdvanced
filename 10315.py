s = input()

m = [i.strip('.,!?:;-').lower() for i in s.split()]

result = {}

a = []

for word in m:
# цикл for перебирает все элементы списка m и для каждого элемента с помощью метода get() мы получаем либо его значение
# из словаря result, либо значение по умолчанию, равное 0. К данному значению прибавляется единица, и результат
# записывается обратно в словарь по нужному ключу
    result[word] = result.get(word, 0) + 1
n = min(result.values())
for key, value in result.items():
    if value == n:
        a.append(key)
a.sort()

print(a[0])
