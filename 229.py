string = input()
res = list(string)
count = 0
count_max = 0
for i in range(len(res)):
    if res[i] == 'О':
        if count > count_max:
            count_max = count
        count = 0
    elif res[i] == 'Р':
        count += 1
if count > count_max:
    count_max = count
print(count_max)
