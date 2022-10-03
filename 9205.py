m = int(input())
n = int(input())
myset1 = {input() for i in range(m)}
myset2 = [input() for j in range(n)]

for i in range(n):
    if myset2[i] in myset1:
        print("YES")
    else:
        print("NO")
