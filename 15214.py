def print_products(*args):
    count = 1
    list = []
    list_num = []
    if len(args) == 0:
        return "Нет продуктов"
    else:
        for i in args:
            if type(i) == str and len(i) != 0:

                list.append(i)
                count += 1
    return list

print(print_products())
print(print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True))

