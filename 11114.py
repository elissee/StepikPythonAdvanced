my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21],
           'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42],
           'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}

# for i in my_dict.values():
#     for j in range(len(i)):
#         print(i[j])
#         if i[j] > 20:
#            del i[j]
new_values = []

for key in my_dict:
    for i in range(len(my_dict[key])):
        if my_dict[key][i] <= 20:
            new_values.append(my_dict[key][i])
    my_dict[key] = new_values
    new_values = []
