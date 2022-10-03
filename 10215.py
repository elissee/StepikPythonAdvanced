s = input()
symbols = {'1': '.,?!:', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV',
           '9': 'WXYZ', '0': ' '}

a = list(s.upper())
x = []

for i in a:
    for key, value in symbols.items():
        if i in value:
            x.append(key * (value.index(i) + 1))

for i in x:
    print(i, end='')
