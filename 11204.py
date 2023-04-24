def build_query_string(dict1):
    st = ''
    dict1 = sorted(dict1.items())
    dict1 = dict(dict1)

    for key, value in dict1.items():
        st += str(key) + '=' + str(value)
        st += '&'
    st = st[:-1]
    return st

print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
