s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana ' \
    'orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon ' \
    'strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit ' \
    'barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit ' \
    'strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot ' \
    'barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince ' \
    'barley lime grapefruit pomegranate barley'

result = {}
a = []
for word in s.split():
    result[word] = result.get(word, 0) + 1
m = max(result.values())
for key, value in result.items():
    if value == m:
        a.append(key)
a.sort()
print(a[0])
