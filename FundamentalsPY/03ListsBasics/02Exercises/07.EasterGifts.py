gifts = input().split(" ")

while True:
    command = input()
    if command == "No Money":
        break
    command = list(command.split(" "))

    if "OutOfStock" in command:
        for i in range(len(gifts)):
            if command[1] == gifts[i]:
                gifts[i] = "None"
    elif "Required" in command:
        for i in range(len(gifts)):
            if i == int(command[2]):
                gifts[i] = command[1]
    elif "JustInCase" in command:
        gifts[-1] = command[1]

while "None" in gifts:
    gifts.remove("None")

print(" ".join(gifts))
