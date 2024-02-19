time = input()
time = time.split(" ")
time = ":".join(time)
time = time.split(":")


if time[2] == "AM":
    if int(time[0]) == 12 or 0 < int(time[0]) <= 2:
        print("beer time")
elif time[2] == "PM":
    if 1 <= int(time[0]) <= 11:
        print("beer time")
    elif int(time[0]) == 12 or int(time[0]) == 0:
        print("non-beer time")


else:
    print("invalid time")


