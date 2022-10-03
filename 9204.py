n = int(input())
myset = {input() for i in range(n)}
new_city = input()
if new_city in myset:
    print("REPEAT")
else:
    print("OK")
