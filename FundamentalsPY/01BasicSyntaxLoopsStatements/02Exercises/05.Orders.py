n = int(input())
total = 0
for i in range(1, n+1):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if not 1 <= capsules <= 2000 or not 1 <= days <= 31 or not 0.01 <= price <= 100.00:
        continue
    else:
        print(f"The price for the coffee is:" + " ${:.2f}".format(price * days * capsules))
        total += price * days * capsules

print("Total: "  "${:.2f}".format(total))
