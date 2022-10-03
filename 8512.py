n = int(input())
num = [input().lower() for _ in range(n)]
sum1 = ''.join(num)
sum2 = set(sum1)
print(len(sum2))
