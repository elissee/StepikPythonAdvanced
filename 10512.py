words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {i: [ord(j) for j in i] for i in words}

# for i in words:
#     for j in i:
#         print(ord(j))
#
# print(result)
