from fractions import Fraction

num1 = input()
num2 = input()

num1f = Fraction(num1)
num2f = Fraction(num2)

amount = num1f + num2f
dif = num1f - num2f
mult = num1f * num2f
div = num1f / num2f

print(num1 + " + " + num2 + " = " + str(amount))
print(num1 + " - " + num2 + " = " + str(dif))
print(num1 + " * " + num2 + " = " + str(mult))
print(num1 + " / " + num2 + " = " + str(div))
