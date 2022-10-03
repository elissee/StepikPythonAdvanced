m, n = int(input()), int(input())
m_set = {input() for i in range(m)}
n_set = {input() for i in range(n)}

x = (len(m_set - n_set))
print(x)
