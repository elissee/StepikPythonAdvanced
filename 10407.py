my_code = input()
n = int(input())

d = {}

d_my_code = dict((letter, str(my_code.count(letter))) for letter in set(my_code))

for i in range(n):
    x = input().split(': ')
    d.setdefault(x[1], x[0])

for i in my_code:
    print(d[d_my_code[i]], end='')
