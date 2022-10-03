m, n = int(input()), int(input())
m_n_list = [input() for i in range(m + n)]
m_n_set = set(m_n_list)

if (len(m_n_list) > len(m_n_set)):
    if (len(m_n_list) == 2*len(m_n_set)):
        print("NO")
    else:
        print(len(m_n_set) - (len(m_n_list) - len(m_n_set)))
elif (len(m_n_list) < len(m_n_set)):
    print(len(m_n_set) - (len(m_n_set) - len(m_n_list)))
elif (len(m_n_list) == len(m_n_set)):
    print(len(m_n_set))
