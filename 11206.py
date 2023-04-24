n = int(input())

s1 = []
d1 = {}
d2 = {}
st = []
fl = []
actions = {'write': 'W', 'read': 'R', 'execute': 'X'}

# for i in range(n):
    # st = input().split(' ', 1)

for i in range(n):
    for j in input().split(' ', 1):
        st.append(j)
    a = tuple(st)
    s1.append(a)
    a = 0
    st = []
d1 = dict(s1)


m = int(input())
for i in range(m):
    # fl.append(input())
    d2 = {d1[i]: d2[i] for i in range(5)}

print(s1)
print(d1)
print(d2)
