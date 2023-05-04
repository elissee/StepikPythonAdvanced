from fractions import Fraction
from math import factorial

n = int(input())

amount = 0

for i in range(1, n + 1):
    num = Fraction(1, factorial(i))
    amount += num
print(amount)
