quantity = int(input())
days = int(input())
ORNAMENT = 2
SKIRT = 5
GARLAND = 3
LIGHTS = 15

spirit = 0
price = 0

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 10 == 0:
        spirit -= 20
        price += SKIRT + LIGHTS + GARLAND
        if i == days:
            spirit -= 30
    if i % 5 == 0:
        price += LIGHTS * quantity
        spirit += 17
    if i % 15 == 0:
        spirit += 30
    if i % 3 == 0:
        price += (SKIRT + GARLAND) * quantity
        spirit += 13
    if i % 2 == 0:
        price += ORNAMENT * quantity
        spirit += 5

print(f"Total cost: {price}")
print(f"Total spirit: {spirit}")
