st = input().split()

numbers = {}

for s in st:
    numbers[s] = numbers.get(s, 0) + 1
    print(numbers[s], end=' ')

