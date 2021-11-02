n = int(input())
num = []
for i in range(n):
    s = int(input())
    num.append(s)
s = int(input())
answer = 'НЕТ'
# поиск произведения
for i in range(len(num)):
    for j in range(len(num)):
        if i == j:
            continue
        elif s == num[i] * num[j]:
            answer = 'ДА'
            break
print(answer)
