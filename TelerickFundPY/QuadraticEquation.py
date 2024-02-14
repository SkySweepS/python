import math
a = float(input())
b = float(input())
c = float(input())

D = b * b - 4 * a * c

x1 = (-b - math.sqrt(D)) / (2 * a)
x2 = (- b + math.sqrt(D)) / (2 * a)


print(f"x1={x1 + 0:.1f}")
print(f"x2={x2 + 0:.1f}")