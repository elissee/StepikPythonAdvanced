m = int(input())
n = int(input())
i_set = {input() for j in range(n)}


for i in range(m - 1):
    ni = int(input())
    b = {input() for a in range(ni)}
    i_set.intersection_update(b)

print(*sorted(i_set), sep='\n')

