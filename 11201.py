nuk_dnk = input()

nd = list(nuk_dnk)

dnk_dict = dict.fromkeys(nd)

for key in dnk_dict:
    if key == 'G':
        dnk_dict[key] = 'C'
    elif key == 'C':
        dnk_dict[key] = 'G'
    elif key == 'T':
        dnk_dict[key] = 'A'
    elif key == 'A':
        dnk_dict[key] = 'U'

for i in nd:
    for key in dnk_dict:
        if i == key:
            print(dnk_dict[key], end='')
