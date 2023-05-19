def greet(name, *args):
    list1 = ["Hello,", name]
    if len(args) == 0:
        return ' '.join(list1) + '!'
    else:
        for i in args:
            list2 = ["and", i]
            list1.extend(list2)

        return ' '.join(list1) + '!'


print(greet('Timur', 'Roman', 'Ruslan'))
print(greet('Timur'))
