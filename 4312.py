my_list = []
elem = [i for i in input().split()]
my_list.extend(elem)
a = []
for i in my_list:
    if i != len(my_list):
        if my_list[i] ==     my_list[i + 1]:
            a.extend(list[i])
            a.extend(list[i + 1])


print(my_list)

