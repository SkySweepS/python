wagons = int(input())

train = [0] * wagons
while True:
    passengers = input().split(" ")
    new = [i for i in range(len(train)) if int(passengers[1]) == train[i]]

    if passengers[0] == "End":
        break
    if passengers[0] == "add":
        train[-1] += int(passengers[1])
    elif passengers[0] == "insert":
        for i in range(len(train)):
            if i == int(passengers[1]):
                train[i] += int(passengers[2])

    elif passengers[0] == "leave":
        for i in range(len(train)):
          if int(passengers[1]) == i:
              train[i] -= int(passengers[2])

print(new)
print(train)