m, n = int(input()), int(input())
m_set = {input() for i in range(m)}
n_set = {input() for i in range(n)}

x = m_set.symmetric_difference(n_set)

if len(x) > 0:
    print(len(x))
else:
    print("NO")
