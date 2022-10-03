#n = int(input())
#words = [set(input().lower()) for _ in range(n)]
#for i in range(len(words)):
#    sum = len(words[i])
n = int(input())
words = [set(input().lower()) for _ in range(n)]
for i in range(len(words)):
    print(len(words[i]))
