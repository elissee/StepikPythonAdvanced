s = input()

m = [i for i in s.split()]

result = {}
a = []

for letter in m:
    result[letter] = result.get(letter, -1) + 1
    if result.get(letter) > 0:
        a.append(f'{letter}_{result.get(letter)}')
    else:
        a.append(letter)

for i in a:
    print(i, end=' ')
