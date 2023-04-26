from decimal import *

# Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.

num = Decimal(input())
min_tuple = 0
max_tuple = 0

num_tuple = num.as_tuple()

if num > -1 and num < 1:
    min_tuple = 0
    max_tuple = max(num_tuple.digits)
    print(max_tuple + min_tuple)
else:
    max_tuple = max(num_tuple.digits)
    min_tuple = min(num_tuple.digits)
    print(max_tuple + min_tuple)
