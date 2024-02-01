budget = int(input())
while True:
    price = input()
    if price == "End" and budget >= 0:
        print("You bought everything needed.")
        break
    budget -= int(price)
    if budget < 0:
        print("You went in overdraft!")
        break
    
