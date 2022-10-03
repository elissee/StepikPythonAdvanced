m_set = {i for i in input().split()}
n_set = {i for i in input().split()}

x = m_set.union(n_set)
print(*sorted(x))
