from fractions import Fraction

n = int(input())

amount = Fraction()

for i in range(1, n + 1):
    num = Fraction(1, i**2)
    amount += num
print(amount)
