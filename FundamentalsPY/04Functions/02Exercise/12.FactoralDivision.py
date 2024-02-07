n1 = int(input())
n2 = int(input())

def factural(n):
    factoral_1 = 1
    for i in range(1, n + 1):
        factoral_1 *= i
    return factoral_1

total = factural(n1) / factural(n2)

print(f"{total:.2f}")