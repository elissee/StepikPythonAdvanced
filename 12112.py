import random

n = int(input())    # количество попыток

for i in range(n):
    num = random.randint(1, 6)
    print(num)
