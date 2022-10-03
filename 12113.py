import random

length = int(input())    # длина пароля

for i in range(length):
    password = random.randint(65, 90)
    print(chr(password), end='')
