energy = 100
coins = 100
event = input().split("|")
event = "-".join(event)
event = event.split("-")

for i in range(len(event)):
    if i % 2 == 0:
        s = event[i]
        n = event[i + 1]
        gain = 0
        if s == "rest":

            gain = int(n)
            if 100 - energy < gain:
                gain = 100 - energy
            energy += gain
            print(f"You gained {gain} energy.")
            print(f"Current energy: {energy}.")
        elif s == "order":

            if energy - 30 >= 0:
                coins += int(n)
                energy -= 30
                print(f"You earned {n} coins.")
            else:
                energy += 50
                print("You had to rest!")
        else:
            if coins - int(n) >= 0:
                print(f"You bought {s}.")
                coins -= int(n)
            else:
                print(f"Closed! Cannot afford {s}.")
                break
    if i == len(event) - 1:
        print("Day completed!")
        print(f"Coins: {coins}")
        print(f"Energy: {energy}")
