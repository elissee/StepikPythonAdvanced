import random

n = 7

ticket = []

for i in range(n):
    t = random.randint(1, 50)
    if t not in ticket:
        ticket.append(t)

ticket = sorted(ticket)

for i in ticket:
    print(i, end=' ')
