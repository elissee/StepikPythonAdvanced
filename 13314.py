import cmath

n = int(input())
z1 = complex(input())
z2 = complex(input())
z_1 = z1.conjugate()
z_2 = z2.conjugate()

result = z1 ** n + z2 ** n + z_1 ** n + z_2 ** (n + 1)

print(result)
