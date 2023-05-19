def mean(*args):
    amount = 0
    count = 0
    for i in args:
        if type(i) == int or type(i) == float:
            amount += i
            count += 1

    if count != 0:
        return amount/count
    else:
        return 0
