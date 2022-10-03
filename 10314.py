pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}

#owners = []

#dogs = []

# for i in range(len(pets)):
#        result[pets[i][1:]] = list(pets[i][0].split())

#for owner in pets:
#    owners.append(owner[1:])

#for pet in pets:
#    dogs.append(pet[0].split())

#for pet in pets:

#Пытаемся получить из словаря result ключ pets[i][1:], если его нет в result, ключ туда добавляется со значением []
# и в значение [] добавляется pets[i].[0]
for i in range(len(pets)):
    result.setdefault(pets[i][1:], []).append(pets[i][0])


print(result)
