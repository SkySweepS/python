TICKET_PRICE = 150
items = input().split("|")
items = "->".join(items)
items = items.split("->")
budget = float(input())
prices = []
for i in range(len(items)):
    if i % 2 == 0:
        s = items[i]
        n = items[i + 1]
        n = float(n)
        if s == "Clothes":
            if n <= 50 and budget - n >= 0:
                budget -= n
                prices.append(n)
        elif s == "Shoes" and n <= 35 and budget - n >= 0:
            budget -= n
            prices.append(n)
        elif s == "Accessories" and n <= 20.50 and budget - n >= 0:
            budget -= n
            prices.append(n)
str_price = []
total_price = 0.0
profit = 0
for i in range(len(prices)):
    num = prices[i]
    total_price += float(num)
    profit += float(num) * 1.4
    str_price.append(float(num) * 1.4)
total_profit = profit - total_price
final = budget + profit

for i in str_price:
    print(f"{i:.2f}", end=" ")
print()
print(f"Profit: {total_profit:.2f}")
if final >= TICKET_PRICE:
    print("Hello, France!")
else:
    print("Not enough money.")