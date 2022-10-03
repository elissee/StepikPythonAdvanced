myset1 = {int(i) for i in input().split()}
myset2 = {int(i) for i in input().split()}
myset3 = myset1.intersection(myset2)

if len(myset3) == 0:
    print("BAD DAY")
else:
    print(*sorted(myset3, reverse=True))
