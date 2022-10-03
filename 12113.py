import random

length = int(input())    # длина пароля

for i in range(length):
    password1 = random.randint(65, 90)
    password2 = random.randint(97, 122)
    choice = random.randint(0, 1)
    if choice == 0:
        print(chr(password1), end='')
    elif choice == 1:
        print(chr(password2), end='')
